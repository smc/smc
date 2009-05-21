# -*- coding: utf-8 -*-
#        Author : Ashik Salahudeen <aashiks@gmail.com>
#        Licensed under :
#        ----------------------------------------------------------------------------
#        "THE CAPPUCHINO LICENSE" (Revision 42):
#        <aashiks@gmail.com> wrote this file. You can do whatever you want with this 
#        stuff as long as you retain this notice and as long as you agree to give this 
#        stuff to whoever wants it. If we meet some day, and you think
#        this stuff is worth it, you can buy me a cappuchino in return -- Aashik 
#        ----------------------------------------------------------------------------
# fortune configs -o for offensive
# cookie files : from fortune -f
# maxlength
# 

#TODO : Create a configuration dialogue to handle various config options.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from PyKDE4.kdecore import KProcess 


class FortuneCookie(plasmascript.Applet):

    # The all important label : This is the only control in our plasmoid
    label = Plasma.Label
    mytimer = QTimer
    process = KProcess
    fortunecommand="fortune"
    fortunecookies="fortune-ml"
    offensive="-o"
    #Every half an hour
    mytimeout = 1800000
    #process = 
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)
 
    def init(self):
        #There is no configuration dialogue for this applet
        self.setHasConfigurationInterface(False)
        
        #This applet will always retain its Initial aspect ratio
        self.setAspectRatioMode(Plasma.KeepAspectRatio)
        
        #Get the current theme and use the default background ("widgets/background") and background hints 
        self.theme = Plasma.Svg(self)
        self.theme.setImagePath("widgets/background")
        self.setBackgroundHints(Plasma.Applet.DefaultBackground)
 
        #The applet layout is horizontal
        self.layout = QGraphicsLinearLayout(Qt.Vertical, self.applet)
        #Create a new label
        self.label = Plasma.Label(self.applet)
        
        # Add the label to the layout so it will be displayed 
        self.layout.addItem(self.label)
        self.setLayout(self.layout)

        # setup the process
        self.process=KProcess(self)
        self.process.setShellCommand(self.fortunecommand + " " + self.fortunecookies)
        self.process.setOutputChannelMode(KProcess.MergedChannels)
        # When the command outputs something , get it 
        QObject.connect( self.process, SIGNAL("readyReadStandardOutput()"), self.gotsomeoutput );
    
        #setup timer
        self.mytimer=QTimer(self)
        # We don't want this to timeout all by itself..
        self.mytimer.setSingleShot(True)

        # When the timer times out, execute this
        QObject.connect(self.mytimer,SIGNAL("timeout()"), self.TimeOut)

        # start the timer
        self.process.start()
        self.mytimer.start(self.mytimeout)
        # Set the default applet size
        self.resize(180,130)
    
    def gotsomeoutput(self):
        outputstring = str(self.process.readAllStandardOutput())
        self.label.setText(unicode(outputstring,"utf-8"))
        self.mytimer.start(self.mytimeout)
        
    def TimeOut(self):
        # execute the fortune command and get its output
        if self.process.state() == QProcess.NotRunning:
            self.process.start()
        else:
            return

    # On mouse click , change the quote
    def mousePressEvent(self, event):
        print "Test"
        self.mytimer.start(0)


def GetFortuneCookies(): 
    #TODO: Get a list of fortunecookies, if any
    return ""
  # Start this applet
def CreateApplet(parent):
        return FortuneCookie(parent)