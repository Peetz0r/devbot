#!/usr/bin/python3

import sys, requests, bs4, urllib, re

user = sys.argv[1]
nick = user.split('!')[0]
msg = sys.argv[3]

command, args = msg.partition(' ')[::2]

s = requests.Session()
s.headers = {'User-agent': 'DevBot (https://github.com/Peetz0r/DevBot)'}

if(command == '.cup-a-soup'):
	print('Ja, het is 4 uur, tijd voor cup-a-soup tomaat!')
elif(command == '.php'):
	args = args.replace('::', '.')
	r = s.get('https://secure.php.net/manual-lookup.php', params={'lang': 'en', 'pattern': args})
	soup = bs4.BeautifulSoup(r.text, 'html.parser')
	if(len(r.history) == 0):
		print(re.sub('[\s+]+', ' ', 'Geen exact resultaat gevonden, wel o.a. ' + ', '.join(list(soup(id='quickref_functions')[0].stripped_strings)[:5])))
	else:
		print(re.sub('[\s+]+', ' ', soup(class_='refpurpose')[0].get_text() + ' | https://php.net/' + urllib.parse.quote_plus(args)))

