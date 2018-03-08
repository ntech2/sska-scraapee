# https://www.youtube.com/watch?v=XQgXKtPSzUI 9.11.2017 dzivoklu cena/kvm/riga projekts

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import csv




#raxtam failinj
filename = "sssell.csv"
f = open(filename, "w")
headers = "Link, Pic, Address, Rooms, Sqrm, Floor, Type, Price\n"
#headers = "Link, Pic, Text, Address, Rooms, Sqrm, Floor, Type, Price\n" rusky jezik nerabotaet
f.write(headers)
lastpage = input('Ievadi pedejaas lapas numuru - https://www.ss.com/lv/real-estate/flats/riga/all/sell/page55.html :::\n')
lastpage = int(lastpage)
lastpage = lastpage+1
for i in range(1, lastpage):
	k = str(i)
	my_url= 'https://www.ss.com/lv/real-estate/flats/riga/all/sell/page' + k + '.html'
	


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

		f.write ("http://ss.com" + con_link + "," + con_pic.replace(".th2.", ".800.") + ","  + con_addr.replace(",", ".").replace("А", "A").replace("а", "a").replace("к", "k").replace("с", "c") + "," + con_rooms.replace(",", ".") + "," + con_sqrm + "," + con_floor + "," + con_type.replace(",", ".") + "," + con_monet.replace(",", "") + "\n")
	print("Writing page" +k)
		
	
	#if my_url == 'https://www.ss.com/lv/real-estate/flats/riga/all/hand_over/':
	#	print('tis page not exist')
	#	break
	#tis not working

f.close()
print("the end! VISI PARDOSANAS SLUDINAJUMI SAGLABATI!")