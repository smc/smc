#!/usr/bin/env python
"""Payyans is a python program to convert the data written for ascii fonts in ascii format to the Unicode format"""
from distutils.core import setup

doclines = __doc__.split("\n")
setup(name='payyans',
      version='0.7',
      description=doclines[0],
      long_description = "\n".join(doclines[:]),
      platforms = ["Linux"],
      author='Santhosh Thottingal, Nishan Naseer, Rajeesh K Nambiar',
      author_email='santhosh.thottingal@gmail.com , nishan.naseer@gmail.com, rajeeshknambiar@gmail.com',
      url='http://smc.org.in/Payyans',
      license = 'http://www.gnu.org/copyleft/gpl.html',
      packages=['payyans'],
      data_files=[('/usr/share/payyans/maps',['maps/karthika.map','maps/indulekha.map','maps/revathi.map']),
		   ('/usr/bin',['payyans/payyans']),
	       ('/usr/share/doc/payyans-0.6',['docs/README','docs/LICENSE','docs/ChangeLog'])]
      )
