slackbuild
==========

find package from slackbuilds.org and build

----------------------
Installation:

Requirement: BeautifulSoup

give execute permission for slackbuild.py

make link to slackbuild.py:

ln -s <location of slackbuild.py> /bin/slackbuild

Now "slackbuild" is ready to use.

----------------------
Use:

Type the name of package which you want to make or if you could find it yourself in slackbuilds.org and slackbuild could not find, Just enter the URL for him.

----------------------
Example:

to install inkscape by slackbuild:

#slackbuild
#Pakcage name or url:inkscape

and it will find inkscape and then start to build the package.

if slackbuld could not find package from slackbulids.org and you, yourself found, just put the url instead of package name. for example for 'libsigc' slackbulid can not find the url himself. Just give him the URL:

#slackbuild
#Pakcage name or url:http://slackbuilds.org/repository/14.0/libraries/libsigc++/
