#!/usr/bin/python3

import sys, requests, bs4, urllib, re, datetime

user = sys.argv[1]
nick = user.split('!')[0]
msg = sys.argv[3]

command, args = msg.partition(' ')[::2]

s = requests.Session()
s.headers = {'User-agent': 'DevBot (https://github.com/Peetz0r/DevBot)'}

if(command in('cup-a-soup', '.cupasoup')):
	d = datetime.datetime.now()
	if(d.hour in (3, 15) and d.minute >= 50):
		print('Het is bijna 4 uur. Zet je waterkoker alvast aan!')
	elif(d.hour in(4, 16)):
		print('Ja, het is 4 uur, tijd voor cup-a-soup tomaat!')
	else:
		print('Nee! Dan maar een kopje thee.')
elif(command in('.thee', '.tea')):
	print('Tea, Earl Grey, hot!')
elif(command in('.koffie', '.coffee')):
	print('Koffie is voor mietjes. Echte hackers drinken mate!')
elif(command == '.mate'):
	print('Hoe Club Mate in twintig jaar het favoriete drankje werd van hackers en ravers | http://motherboard.vice.com/nl/read/hoe-club-mate-in-twintig-jaar-het-favoriete-drankje-werd-van-hackers-en-ravers')
elif(command == '.yolt'):
	print('ohai r3boot!')
elif(command == '.tosti'):
	print('Is het tijd voor een tosti? HET IS ALTIJD TIJD VOOR EEN TOSTI!')
elif(command == '.php'):
	args = args.replace('::', '.')
	r = s.get('https://secure.php.net/manual-lookup.php', params={'lang': 'en', 'pattern': args})
	soup = bs4.BeautifulSoup(r.text, 'html.parser')
	if(len(r.history) == 0):
		print(re.sub('[\s+]+', ' ', 'Geen exact resultaat gevonden, wel o.a. ' + ', '.join(list(soup(id='quickref_functions')[0].stripped_strings)[:5])))
	else:
		print(re.sub('[\s+]+', ' ', soup.select('.refpurpose, .partintro .para')[0].get_text() + ' | https://php.net/' + urllib.parse.quote_plus(args)))
elif(command == '.py'):
#	import importlib, inspect
#	try:
#		print(help(args))
#		args_split = args.split('.', 1)
#		if(len(args_split) == 1):
#			print(inspect.getdoc(eval('importlib.import_module(args_split[0])')))
#		else:
#			print(inspect.getdoc(eval('importlib.import_module(args_split[0]).'+args_split[1])))
#	except:
#		print('DevBot\'s python kon "' + args + '" niet vinden.')
		print('.py staat nu even uit. Vraag Peetz0r waarom')

