<?php
  exit();
  $page_title = "KDE 4.3.0 Caizen Release Announcement";
  $site_root = "../";
  include "header.inc";
  include "helperfunctions.inc";
?>

Also available in:
<?php
  $release = '4.3';
  include "../announce-i18n-bar.inc";
?>

<!-- // Boilerplate -->

<h3 align="center">
  KDE Community Delivers Incremental Innovations With New KDE 4.3 Release
</h3>

<p align="justify">
  <strong>
    KDE 4.3 (Codename: <i>"Caizen"</i>) Delivers Incremental Innovations to the Free Desktop Users and Software Developers
  </strong>
</p>

<p align="justify">
6 August, 2009. The <a href=http://www.kde.org/>KDE Community</a> today announces the immediate availability of <i>"Caizen"</i>, (a.k.a KDE 4.3), bringing many improvements to the user experience and development platform. KDE 4.3 continues to refine the unique features brought in previous releases while bringing new innovations. With the 4.2 release aimed at the majority of end users, KDE 4.3 offers a more stable and complete product for the home and small office.
</p>
<p align=justify>
  The KDE community has <strong>fixed over 10,000 bugs</strong> and <strong>implemented almost 2,000 feature requests</strong> in the last 6 months. Close to 63,000 changes were checked in by a little under 700 contributors. Read on for an overview of the changes in the KDE 4.3 Desktop Workspace, Application Suites and the KDE 4.3 Development Platform.
</p>

<div  align="center" style="width: auto; margin-top: 20px; margin-botton: 20px;">
<a href="screenshots/desktop.png"><img src="screenshots/desktop_thumb.png" align="center" width="504" height="315"  /></a><br />
<em>The KDE 4.3 Desktop</em></div>

<h3>
  Desktop Improves Performance And Usability
</h3>
<br>
<p align=justify>
    The KDE Desktop Workspace provides a powerful and complete desktop experience that features excellent integration with Linux and UNIX operating systems. The key components that make up the KDE Desktop Workspace include:
<ul>
  <li>
    <strong>KWin</strong>, a powerful window manager that provides modern 3D graphical effects
  </li>
  <li>
    <strong>The Plasma Desktop Shell</strong>, a cutting-edge desktop and panels system that features productivity enhancements and online integration through customizable widgets
  </li>
  <li>
    <strong>Dolphin</strong>, a user-friendly, network- and content-aware file manager
  </li>
  <li>
    <strong>KRunner</strong>, a search and launch system for running commands and finding useful information
  </li>
  <li>
    easy access to desktop and system controls through <strong>SystemSettings</strong>.
  </li>
</ul>
Below you can find a short list of improvements to the KDE Desktop Workspace.
<ul>
  <li>
    The <a href="http://plasma.kde.org">Plasma Desktop Shell</a> introduces a <b>new default theme</b>, Air. Air looks much lighter and fits better with the default application theme. Plasma also has seen large <b>performance improvements</b>. Memory usage has been reduced, and animations are smoother. <b>Activities can now be tied to virtual desktops</b>, allowing users to have different widgets on each of their desktops. Furthermore, Plasma has improved upon its <b>job and notification management</b>. Running jobs are grouped in a single progress bar to prevent the popup of too many dialogs. Animations are used to signify that jobs are still running by smoothly sliding dialogs into the systemtray and animating the notification icon. Smaller changes in Plasma include <b>fully configurable keyboard shortcuts</b> and more extensive keyboard navigation, the ability to create a plasma widget when you drag or copy content on the desktop and many <b>new and improved Plasma widgets</b>. The folderview widget now allows the user to <b>peek into a folder by hovering it</b> and the <b>new Translatoid widget</b> translates words and sentences right on your desktop using Google Translate. Furthermore, KRunner made its <b>plugin features easier to discover</b> by having a 'help' button showing the syntax of commands in the result area. <b>Actions also have a small configuration</b> allowing for example to start applications under another user account.<br>
    <br>
    </li>
  <li>
    The file manager Dolphin shows <b>small previews of files within a folder</b> and video thumbnails to help the user identify items. The <b>trash can now be configured</b> from the Dolphin Settings menu, and various configurable limitations on the trash size help make sure the disk does not fill up with deleted files. The menu which is shown on a right mouseclick on a item is configurable and the configuration dialog in general has been redesigned to be <b>easier to use</b>. The new <b>network:/ location</b> shows other computers and services on the network (currently limited to those announced by DNS-SD/zeroconf protocols, more will be supported in future versions).<br>
    <br>
  </li>
  <li>
    Further refinements to the workspace tools make it easier to work with your computer. A <b>faster SystemSettings</b> introduces an <b>optional treeview </b>for the configuration and several improvements to settingsdialogs. <b>New effects</b> like 'Sheet' and "Slide Back" and <b>better performance</b> in <b>KWin </b>make window management more smooth, while integration with the Plasma themes creates a more consistent look. <b>Klipper</b>, a tool which keeps a history of things copied to the clipboard, can now <b>act intelligently on the content</b>. It automatically determines a list of applications which can handle a object copied to the clipboard and allows the user to start them right away.<br>
    <br>
  </li>
</ul>
</p>
<div  align="center" style="width: auto; margin-top: 20px; margin-botton: 20px;">
<embed src="http://blip.tv/play/hIsigZW3agI" type="application/x-shockwave-flash" width="480" height="390" allowscriptaccess="always" allowfullscreen="true"></embed>
<br>
<a href="http://blip.tv/file/get/Jospoortvliet-KDE43DesktopWorkspaceDemo820.ogv">Ogg Theora version</a></div>
<h3>
  Applications Leap Forward
</h3>
<p align=justify>
A great number of sophisticated applications are provided by the KDE community which take full advantage of the powerful KDE Application Framework. A selection of these applications are included in the KDE Software Distribution, divided up by category into various Application Suites. These include:
</p>
<ul>
  <li>
    KDE Network Applications
  </li>
  <li>
    KDE Multimedia
  </li>
  <li>
    KDE Graphics Tools
  </li>
  <li>
    KDE PIM Suite (for personal information management and communication)
  </li>
  <li>
    KDE Educational Applications
  </li>
  <li>
    KDE Games
  </li>
  <li>
    KDE Utilities
  </li>
  <li>
    KDE Software Development Platform
  </li>
</ul>
<p align=justify>
Together they form a comprehensive set of desktop essentials that run on most modern operating systems. Below you will find a selection of improvements to some of these Application Suites.
</p>
<ul>
  <li>
    The <strong>KDE Utilities</strong> have seen many improvements. Among other things, <b>KGpg</b>, the privacy tool used for encryption and signing files and emails <b>integrates Solid</b> for detecting the availability of a network connection and has improved its <b>key import dialog</b>. <b>Ark</b>, a file compression and decompression application now <b>supports LZMA/XZ</b>, has improved support for zip, rar and 7zip and works better with drag'n'drop. KDELirc, a frontend for the <b>Linux Infrared Remote Control system</b> (LIRC), has been ported to KDE 4 and is included again. <b>Okteta</b>, the KDE hex editor gained a <b>checksum tool,</b> a filesystem browser sideview and a bookmarks sidebar. <strong>Lokalize</strong>, the KDE translation tool, introduces support for scripts, new fileformats and the<b> translation of ODF documents</b>.<br>
    <br>
  </li>
  <li>
    The <b>KDE games</b> now use a similir <b>Egyptian-style theme</b> in many of the games. KGoldrunner introduces a new game,<b> "Curse of the Mummy"</b> and improves gameplay with more accurate pause, resume and recording and replaying of games. KMahjongg introduces 70 new user-submitted levels and a <b>new game</b>, KTron, has been introduced. Some games introduced <b>new features</b> like the Vaporizer action in Killbots and a better AI in Bovo. Thanks to work on file loading and saving the state of scalable images many games<b> start and run faster.</b><br>
    <br>
  </li>
  <li>
    The <strongKDE Personal Information Management</strong> applications have seen improvements in various area's like performance and stability. Instant messenger <b>Kopete </b>introduces an improved contact list and KOrganizer can sync with <b>Google Calendar</b>. Kmail supports inserting inline images into email and the <b>Alarm notifier </b>gained export functionality, drag and drop and has an improved configuration.<br>
    <br>
  </li>
</ul>
<div  align="center" style="width: auto; margin-top: 20px; margin-botton: 20px;">
<a href="screenshots/games.png"><img src="screenshots/games_thumb.png" align="center" width="504" height="315"  /></a><br />
<em>Some Egyptian themes</em></div>
<ul>
  <li>
    In case something goes wrong with a KDE application and it crashes, the <b>new Bug Report Tool</b> will make it easier for the user to contribute to the stability of KDE. The bug report tool provides a three-star rating of the quality of the data it gathered on the crash. It also gives hints on how to improve the quality of the crash data and the bug report itself while guiding the user through the process of reporting. During the Beta cycles for this release the new bug report tool has already proven itself by the increased quality of bug reports.<br>
  </li>
</ul>
</p>
<div class="ii gt" id=:7r>
</div>
<h3>
  Platform Accelerates Development
</h3>
<p align=justify>
The KDE community brings many innovations for application developers to the forefront in the KDE Application Framework. Building on the strengths of Nokia's Qt library, this integrated and consistent framework has been crafted in direct response to the needs of real-world application developers.
</p>
<p align=justify>
The KDE Application Framework helps developers create robust applications efficiently by streamlining the complexity and tedious tasks usually associated with application development. Its use by KDE applications provides a compelling showcase for its flexibility and utility.
</p>
<p align=justify>
Liberally licensed under the LGPL (allowing for both proprietary and open source development) and cross-platform (Linux, UNIX, Mac and MS Windows), it contains among other things a powerful component model (<b>KParts</b>), network  transparent data access (<b>KIO</b>) and flexible configuration management. Dozens of useful widgets ranging from file dialogs to font selectors are provided and the framework also offers semantic search integration <b>(Nepomuk</b>), hardware awareness (<b>Solid</b>) and multimedia access (<b>Phonon</b>). Read on for a list of improvements to the KDE Application Framework.
</p>
<ul>
  <li>
    The KDE 4.3 Application Framework introduces the beginnings of <a href="http://www.socialdesktop.org/">Social Desktop</a> integration, bringing the worldwide Free Software community to the desktop. Offering an <strong>open collaboration, sharing and communication platform</strong>, the Social Desktop initiative aims to allow people to share their knowledge withouth giving up control to an external organisation. The platform currently offers a <strong>DataEngine</strong> for plasma applets supporting aspects of Social Desktop.<br>
    <br>
  </li>
  <li>
    The <strong>new system tray protocol</strong> developed in collaboration with the <a href="http://www.freedesktop.org/wiki/">Free Desktop initiative</a> is a long-overdue overhaul of the old systray specification. The old systemtray using small embedded windows did not allow for any kind of control by the systemtray over its contents, limiting the flexibility for the user and application developer at the same time. While the new systemtray supports both the old and new standard, application developers are encouraged to upgrade their applications to the new specifications. For more information <a href="http://www.notmart.org/index.php/Software/Systray_finally_in_action">check this blog</a> or find more information <a href="http://techbase.kde.org/Projects/Plasma/NewSystemTray">on TechBase</a>.<br>
    <br>
  </li>
  <li>
    The Plasma Desktop Shell introduces a <strong>Geolocation DataEngine</strong> using libgps and HostIP which allows plasmoids to easily respond to the location of the user. Other <strong>new DataEngines</strong> provide acces to <strong>Akonadi resources</strong> (including mail and calendar), <a href="">Nepomuk</a> metadata and keyboard state besides the various improvements to existing DataEngines. Read about using and discovering DataEngines <a href="http://techbase.kde.org/Development/Tutorials/Plasma/DataEngines">on TechBase</a>.<br>
    <br>
  </li>
  <li>
    The KDE Application Platform introduces a <strong>PolicyKit wrapper</strong> making it easy for developers who want their application to perform privileged actions in a secure, consistent and easy way. Provided are an authorization manager and an authentication agent, and an easy library for developers to use. Read <a href="http://techbase.kde.org/Development/Tutorials/PolicyKit/Introduction">here on TechBase</a> for a tutorial!<br>
    <br>
  </li>
  <li>
    <strong>Akonadi</strong>, the Free Desktop PIM storage solution has been deemed <strong>ready for more widespread usage</strong>. Besides the availability of the DataEngine for plasma, application developers are encouraged to have a look at <a href="http://techbase.kde.org/Projects/PIM/Akonadi">the TechBase page</a> if their application needs access to or store chat logs, email, blogs, contacts, or any other kind of personal data. As a cross-desktop technology Akonadi can provide access to any kind of data and is designed to handle high volumes, thus allowing for a wide range of usecases.<br>
    <br>
  </li>
</ul>
</p>

<div  align="center" style="width: auto; margin-top: 20px; margin-botton: 20px;">
<a href="screenshots/social.png"><img src="screenshots/social_thumb.png" align="center" width="504" height="315"  /></a><br />
<em>Social desktop and other online services in action</em></div>

<h4>
    Spread the Word and See What Happens
</h4>
<p align="justify">
The KDE Community encourages everybody to <strong>spread the word</strong> on the Social Web.
Submit stories to news sites, use channels like delicious, digg, reddit, twitter,
identi.ca. Upload screenshots to services like Facebook, FlickR,
ipernity and Picasa and post them to appropriate groups. Create screencasts and
upload them to YouTube, Blip.tv, Vimeo and others. Do not forget to tag uploaded
material with the <em>tag <strong>kde</strong></em> so it is easier for everybody to find the
material, and for the KDE team to compile reports of coverage for the KDE 4.3
announcement. <strong>Help us spreading the word, be part of it!</strong></p>

<p align="justify">
You can follow what is happening around the KDE 4.3 release on the social web live on
the brand-new <a href="http://buzz.kde.org"><strong>KDE Community livefeed</strong></a>. This site aggregates what happens on 
identi.ca, twitter, youtube, flickr, picasaweb, blogs and many other social networking sites 
in real-time. The livefeed can be found on <strong><a href="http://buzz.kde.org">buzz.kde.org</a></strong>.
</p>

<center>
<table border="0" cellspacing="2" cellpadding="2">
<tr>
    <td>
        <a href="http://digg.com/software/KDE_4_3_released"><img src="buttons/digg.gif" /></a>
    </td>
    <td>
        <a href="http://www.reddit.com"><img src="buttons/reddit.gif" /></a>
    </td>
    <td>
        <a href="http://www.twitter.com"><img src="buttons/twitter.gif" /></a>
    </td>
    <td>
        <a href="http://www.identi.ca"><img src="buttons/identica.gif" /></a>
    </td>
</tr>
<tr>
    <td>
        <a href="http://www.flickr.com/photos/tags/kde43/"><img src="buttons/flickr.gif" /></a>
    </td>
    <td>
        <a href="http://www.youtube.com/results?search_query=kde43"><img src="buttons/youtube.gif" /></a>
    </td>
    <td>
        <a href="http://www.facebook.com"><img src="buttons/facebook.gif" /></a>
    </td>
    <td>
        <a href="http://delicious.com/tag/kde43"><img src="buttons/delicious.gif" /></a>
    </td>
</tr>
</table>
<style="font-size: 5pt"><a href="http://microbuttons.wordpress.com">microbuttons</a></style>
</center>

<h4>
  Installing KDE 4.3.0
</h4>
<p align="justify">
 KDE, including all its libraries and its applications, is available for free
under Open Source licenses. KDE can be obtained in source and various binary
formats from <a
href="http://download.kde.org/stable/4.3.0/">http://download.kde.org</a> and can
also be obtained on <a href="http://www.kde.org/download/cdrom.php">CD-ROM</a>
or with any of the <a href="http://www.kde.org/download/distributions.php">major
GNU/Linux and UNIX systems</a> shipping today.
</p>
<p align="justify">
  <em>Packagers</em>.
  Some Linux/UNIX OS vendors have kindly provided binary packages of KDE 4.3.0
for some versions of their distribution, and in other cases community volunteers
have done so.
  Some of these binary packages are available for free download from KDE's <a
href="http://download.kde.org/binarydownload.html?url=/stable/4.3.0/">http://download.kde.org</a>.
  Additional binary packages, as well as updates to the packages now available,
will become available over the coming weeks.
</p>

<p align="justify">
  <a name="package_locations"><em>Package Locations</em></a>.
  For a current list of available binary packages of which the KDE Project has
been informed, please visit the <a href="/info/4.3.0.php">KDE 4.3.0 Info
Page</a>.
</p>

<p align="justify">
Performance problems with the <em>NVidia</em> binary graphics driver have been
<a href="http://techbase.kde.org/User:Lemma/KDE4-NVIDIA">resolved</a> in the
latest releases of the driver available from NVidia.
</p>

<h4>
  Compiling KDE 4.3.0
</h4>
<p align="justify">
  <a name="source_code"></a>
  The complete source code for KDE 4.3.0 may be <a
href="http://download.kde.org/stable/4.3.0/src/">freely downloaded</a>.
Instructions on compiling and installing KDE 4.3.0
  are available from the <a href="/info/4.3.0.php#binary">KDE 4.3.0 Info
Page</a>.
</p>

<?php
  include($site_root . "/contact/about_kde.inc");
?>

<h4>Press Contacts</h4>

<?php
  include($site_root . "/contact/press_contacts.inc");
  include("footer.inc");
?>
