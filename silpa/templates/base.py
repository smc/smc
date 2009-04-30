#! /usr/bin/env python
# -*- coding: utf-8 -*-

def getBaseHTML():
	content = """\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<!--
Copyright: Daemon Pty Limited 2006, http://www.daemon.com.au
Community: Mollio http://www.mollio.org $
License: Released Under the "Common Public License 1.0", 
http://www.opensource.org/licenses/cpl.php
License: Released Under the "Creative Commons License", 
http://creativecommons.org/licenses/by/2.5/
License: Released Under the "GNU Creative Commons License", 
http://creativecommons.org/licenses/GPL/2.0/
-->
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Silpa- The Indian Language Computing project</title>
<link rel="stylesheet" type="text/css" href="css/main.css" media="screen" />
<link rel="stylesheet" type="text/css" href="css/print.css" media="print" />
<!--[if lte IE 6]>
<link rel="stylesheet" type="text/css" href="css/ie6_or_less.css" />
<![endif]-->
<script type="text/javascript" src="js/common.js"></script>
</head>
<body id="type-f">
<div id="wrap">

	<div id="header">

		<div id="site-name">Silpa</div>
		<div id="search">
			<form action="">
			<label for="searchsite">Site Search:</label>
			<input id="searchsite" name="searchsite" type="text" />
			<input type="submit" value="Go" class="f-submit" />
			</form>
		</div>

		<ul id="nav">
		<li class="active"><a href="#">Home</a></li>
		<li class="active"><a href="#">About</a>
		</li>
		<li class="active"><a href="#">Documentation</a>
			<ul>
			<li class="first"><a href="#">Language Detection</a></li>

			<li><a href="#">Spellcheck</a></li>
			<li><a href="#">Text to Speech</a></li>
			</ul>
		</li>
		<li class="active"><a href="#">Links</a>
		<li class="active"><a href="#">License</a>
		</ul>

	</div>
	
	<div id="content-wrap">
	
		<div id="utility">

			<ul id="nav-secondary">
			<li class="first"><a href="?action=Detect+Language">Language Detection</a></li>
			<li><a href="?action=spellcheck">Spellcheck</a></li>
			<li class="active"><a href="#">Font Conversion</a>
				<ul>
				<li class="first"><a href="?action=To+Unicode">Ascii to Unicode</a></li>
				<li><a href="?action=To+Ascii">Unicode to Ascii</a></li>
				</ul>
			</li>
			<li><a href="#">Lemmatizer</a></li>
			<li><a href="#">Normalizer</a></li>

			<li class="last"><a href="#">Sort</a></li>
			</ul>
		</div>
		
		<div id="content">
		
			<div id="breadcrumb">
			 
			$$SILPA_BREADCRUMB$$
			
			</div>
			<hr />
			<div class="featurebox">
			<h3>Welcome to Silpa!</h3>
			<p><strong>Silpa stands for Swathanthra Indian Language Processing Applications. Silpa is a single place in the web
			where you can use the exising free(dom) software langauge processing applications easily. Silpa is in development and if you 
			are intersted in contributing just drop a mail to <a href="mailto:santhosh.thottingal@gmail.com">Santhosh</a>  </p>
			</div>
			$$SILPA_CONTENT$$
			
		
		
		<div id="sidebar">

			<div class="featurebox">
			<h3>Welcome to Silpa!</h3>
			<p><strong>Silpa stands for Swathanthra Indian Language Processing Applications. Silpa is a single place in the web
			where you can use the exising free(dom) software langauge processing applications easily. Silpa is in development and if you 
			are intersted in contributing just drop a mail to <a href="mailto:santhosh.thottingal@gmail.com">Santhosh</a>  </p>
			</div>
			
	 
		</div>

		
		<div id="poweredby"><a href="http://smc.org.in">SMC</a></div>
		
	</div>
	
</div>
</body>
</html>

"""
	
	return  content

if __name__ == '__main__':
	print getBaseHTML()
