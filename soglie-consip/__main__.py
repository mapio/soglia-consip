from urllib import urlopen
from re import sub
from sys import exit

from bs4 import BeautifulSoup

URL = 'https://www.timinternet.it/timmobile/private/wp.do'

def clean(e):
	return sub( r'<[^>]+>', '', u' '.join(map(lambda _: unicode(_).strip(), e.contents)))

data = urlopen( URL ).read()
soup = BeautifulSoup(data, 'html.parser')

try:
	info, _, traffico = soup.find_all('table')[:3]
except ValueError:
	exit('soglie_consip: errore di esecuzione, potresti non essere sotto rete TIM/Consip')	


linea, contratto = info.find_all('tr')[:2]
print u'\t'.join( map( clean, linea.find_all('td') ) )
print u'\t'.join( map( clean, contratto.find_all('td') ) )

tipo, dettagli, residui, totali, scandenza = traffico.find_all('tr')[1].find_all('td')
print 'Tipo', clean(tipo)
print 'Aggiornato il', clean(dettagli)
print 'Residui', u' '.join(clean(residui).split())
print 'Totali', u' '.join(clean(totali).split())
