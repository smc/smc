# OpenOffice utils.
#
# Based on code from:
#   PyODConverter (Python OpenDocument Converter) v1.0.0 - 2008-05-05
#   Copyright (C) 2008 Mirko Nasato <mirko@artofsolving.com>
#   Copyright (C) 2009 Rajeesh K Nambiar <rajeeshknambiar@gmail.com>
#   Licensed under the GNU LGPL v2.1 - or any later version.
#   http://www.gnu.org/licenses/lgpl-2.1.html
#

import sys
import os
import time
import atexit


OPENOFFICE_PORT = 2002

# Find OpenOffice.
_oopaths=(
        ('/usr/lib64/ooo-2.0/program',   '/usr/lib64/ooo-2.0/program'),
        ('/opt/openoffice.org3/program', '/opt/openoffice.org/basis3.0/program'),
     )

for p in _oopaths:
    if os.path.exists(p[0]):
        OPENOFFICE_PATH    = p[0]
        OPENOFFICE_BIN     = os.path.join(OPENOFFICE_PATH, 'soffice')
        OPENOFFICE_LIBPATH = p[1]

        # Add to path so we can find uno.
        if sys.path.count(OPENOFFICE_LIBPATH) == 0:
            sys.path.insert(0, OPENOFFICE_LIBPATH)
	    # This is required for loadComponentFromURL
            os.putenv('URE_BOOTSTRAP','vnd.sun.star.pathname:' + OPENOFFICE_PATH + '/fundamentalrc')
        break


import uno
from com.sun.star.beans import PropertyValue
from com.sun.star.connection import NoConnectException


class OORunner:
    """
    Start, stop, and connect to OpenOffice.
    """
    def __init__(self, port=OPENOFFICE_PORT):
        """ Create OORunner that connects on the specified port. """
        self.port = port


    def connect(self, no_startup=False):
        """
        Connect to OpenOffice.
        If a connection cannot be established try to start OpenOffice.
        """
        localContext = uno.getComponentContext()
        resolver     = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext)
        context      = None
        did_start    = False

        n = 0
        while n < 6:
            try:
                context = resolver.resolve("uno:socket,host=localhost,port=%d;urp;StarOffice.ComponentContext" % self.port)
                break
            except NoConnectException:
                pass

            # If first connect failed then try starting OpenOffice.
            if n == 0:
                # Exit loop if startup not desired.
                if no_startup:
                     break
                self.startup()
                did_start = True

            # Pause and try again to connect
            time.sleep(1)
            n += 1

        if not context:
            raise Exception, "Failed to connect to OpenOffice on port %d" % self.port

        desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)

        if not desktop:
            raise Exception, "Failed to create OpenOffice desktop on port %d" % self.port

        if did_start:
            _started_desktops[self.port] = desktop

        return desktop


    def startup(self):
        """
        Start a headless instance of OpenOffice.
        """
        args = [OPENOFFICE_BIN,
                '-accept=socket,host=localhost,port=%d;urp;StarOffice.ServiceManager' % self.port,
                '-norestore',
                '-nofirststartwizard',
                '-nologo',
                '-headless',
                ]
        env  = {'PATH'       : '/bin:/usr/bin:%s' % OPENOFFICE_PATH,
                'PYTHONPATH' : OPENOFFICE_LIBPATH,
                }

        try:
            pid = os.spawnve(os.P_NOWAIT, args[0], args, env)
        except Exception, e:
            raise Exception, "Failed to start OpenOffice on port %d: %s" % (self.port, e.message)

        if pid <= 0:
            raise Exception, "Failed to start OpenOffice on port %d" % self.port


    def shutdown(self):
        """
        Shutdown OpenOffice.
        """
        try:
            if _started_desktops.get(self.port):
                _started_desktops[self.port].terminate()
                del _started_desktops[self.port]
        except Exception, e:
            pass



# Keep track of started desktops and shut them down on exit.
_started_desktops = {}

def _shutdown_desktops():
    """ Shutdown all OpenOffice desktops that were started by the program. """
    for port, desktop in _started_desktops.items():
        try:
            if desktop:
                desktop.terminate()
        except Exception, e:
            pass


atexit.register(_shutdown_desktops)


def oo_shutdown_if_running(port=OPENOFFICE_PORT):
    """ Shutdown OpenOffice if it's running on the specified port. """
    oorunner = OORunner(port)
    try:
        desktop = oorunner.connect(no_startup=True)
        desktop.terminate()
    except Exception, e:
        pass


def oo_properties(**args):
    """
    Convert args to OpenOffice property values.
    """
    props = []
    for key in args:
        prop       = PropertyValue()
        prop.Name  = key
        prop.Value = args[key]
        props.append(prop)

    return tuple(props)
