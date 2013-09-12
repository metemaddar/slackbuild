pname = raw_input("Pakcage name or url:")

pname = pname.replace(" ","")
cats = ('academic','accessibility','audio','business','desktop','developement',
'games','graphics','ham','haskell','libraries','misc','multimedia','network','office','perl','python','ruby','system')

from urllib import urlopen
from BeautifulSoup import BeautifulSoup
from os import system
url = "http://slackbuilds.org/repository/14.0/%(cat)s/%(package)s/"
def findurl(cats1,url1,package):
	for i in cats1:
		print "check",i
		url2 = url1 % {'package':package,'cat':i}
		#print url2
		pagecontent = urlopen(url2).read()
		if not("404" in pagecontent or "Not Found" in pagecontent):
			return url2
		print "Not true"
#print findurl(cats,url,pname)
if 'http' in pname:
	url = pname
	if pname.split('/')[-1] != '':
		pname = pname.split('/')[-1]
	else:
		pname = pname.split('/')[-2]
	print 'pname =',pname
else:
	url = findurl(cats,url,pname)

def pkgurl(url):
	soup = BeautifulSoup(urlopen(url).read())
	soup = soup.find("div",{"class":"section center"})
	urls = soup.findAll("a")
	urls = (urls[1].get("href"),urls[2].get("href"))
	#print urls
	return urls

#url = url % {'package' :'glibmm','cat':'libraries'}

def install(pname,urls):
	print urls[0]

	system("wget %(url1)s;tar xzf %(pname)s.tar.gz;" % {'url1': urls[1],'pname':pname,'url2':urls[0]})
	system("cd %(pname)s;wget %(url2)s;./%(pname)s*d" % {'pname':pname,'url2':urls[0]})

install(pname,pkgurl(url))
pkgurl(url)

class package():
	url = ""
	def __init__(url2):
		#url = findurl(
		pass
#print url
#s = urlopen(url).read()
#if "404" in s or "Page Not Found" in s:
#	print "404 Not found"
