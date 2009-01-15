#!/usr/bin/env python
"""Chathans is a GUI for the ASCII to Unicode converter, Payyans.It is written in PyGTK. """
from distutils.core import setup

doclines = __doc__.split("\n")
setup(name='chathans',
      version='0.2',
      description=doclines[0],
      long_description = "\n".join(doclines[:]),
      platforms = ["Linux"],
      requires = ["payyans"],
      author='Rajeesh K Nambiar',
      author_email='rajeeshknambiar@gmail.com',
      url='http://wiki.smc.org.in/Chathans',
      license = 'http://www.gnu.org/copyleft/gpl.html',
      packages=['src'],
      data_files=[('/usr/bin',['src/chathans']),
	       ('/usr/share/doc/chathans-0.2',['doc/README','doc/LICENSE'])]
      )
