# https://www.youtube.com/watch?v=XQgXKtPSzUI 9.11.2017 dzivoklu cena/kvm/riga projekts

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import csv

#noradam lapu,kuru kachat
#my_url= 'https://www.ss.com/lv/real-estate/flats/riga/all/'
my_url= 'https://www.ss.com/lv/real-estate/flats/riga/all/hand_over/page2.html'



#atvert connection ar lapu, nokachat html un saglabat ka variable uclient
uClient = uReq(my_url)

#saglabajam variabli page_html un tajaa saglabajam visu nokacato contentu
page_html = uClient.read()

#aizveram sesiju
uClient.close()

# parsojam html un saglabajam rezultatu kaa page_soup
page_soup = soup(page_html, "html.parser")

#dabuu dzivokla ierakstu. Vajag izlabot velak. nez vai tr_4 ar regex ir pareiz
containers = page_soup.findAll("tr",{"id": re.compile('tr_4.*')})

#raxtam failinj
filename = "ssflats.csv"
f = open(filename, "w")
headers = "Link, Pic, Address, Rooms, Sqrm, Floor, Type, Price\n"
#headers = "Link, Pic, Text, Address, Rooms, Sqrm, Floor, Type, Price\n" rusky jezin nerabotaet
f.write(headers)


#loopinjsh tekosai lapai
for container in containers:



	con_link = container.a["href"]
	con_pic = container.img["src"]
	con_txt = container.div.a.text.strip()
	title_container = container.findAll("td",{"class" : 'msga2-o pp6'})
	#nultajaa vajag izdomaat, ka atdalit atseviski rajonu, jo tur pa vidu ir br tags
	con_addr = title_container[0].text.strip()
	con_rooms = title_container[1].text.strip()
	con_sqrm = title_container[2].text.strip()
	con_floor = title_container[3].text.strip()
	con_type = title_container[4].text.strip()
	con_monet = title_container[5].text.strip()


	#test print vai viss gucchi
	#print("con_link: " + con_link)
	#print("con_pic: " + con_pic)
	#print("con_txt: " + con_txt)
	#print("con_addr: " + con_addr)
	#print("con_rooms: " + con_rooms)
	#print("con_sqrm: " + con_sqrm)
	#print("con_floor: " + con_floor)
	#print("con_type: " + con_type)
	#print("con_monet: " + con_monet)


	f.write ("http://ss.com" + con_link + "," + con_pic.replace(".th2.", ".800.") + ","  + con_addr.replace(",", ".") + "," + con_rooms.replace(",", ".") + "," + con_sqrm + "," + con_floor + "," + con_type.replace(",", ".") + "," + con_monet.replace(",", "") + "\n")
print("Donezo!")
f.close()