#!/usr/bin/env python
"""Payyans is a python program to convert the data written for ascii fonts in ascii format to the Unicode format"""
from distutils.core import setup

doclines = __doc__.split("\n")
setup(name='payyans',
      version='0.4',
      description=doclines[0],
      long_description = "\n".join(doclines[:]),
      platforms = ["Linux"],
      author='Santhosh Thottingal, Nishan Naseer',
      author_email='santhosh.thottingal@gmail.com , nishan.naseer@gmail.com',
      url='http://smc.org.in/Payyans',
      license = 'http://www.gnu.org/copyleft/gpl.html',
      packages=['payyans'],
      data_files=[('/usr/share/payyans/maps',['maps/karthika.map']),
		   ('/usr/bin',['payyans/payyans']),
		    ('/usr/share/payyans/docs',['docs/README','docs/LICENSE','docs/ChangeLog'])]
      )
