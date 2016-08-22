#!/usr/bin/python2

from __future__ import print_function

from twisted.application.internet import ClientService
from twisted.internet.defer import Deferred
from twisted.internet.endpoints import clientFromString
from twisted.internet.protocol import ClientFactory
from twisted.internet.task import react
from twisted.internet import defer, reactor, ssl
from twisted.python import log
from twisted.words.protocols.irc import IRCClient

import sys, subprocess32

log.startLogging(sys.stdout)

class DevBot(IRCClient):
	nickname = 'DevBot'

	def connectionMade(self):
		print('connection made')
		IRCClient.connectionMade(self)

	def connectionLost(self, reason):
		print('connection lost:', reason)
		IRCClient.connectionLost(self, reason)

	def signedOn(self):
		print('signed on')
		self.join('##hackenkunjeleren')

	def joined(self, channel):
		self.msg(channel, 'ohai')

	def privmsg(self, user, channel, msg):
		print(user)
		print(channel)
		print(msg)
		if(msg.startswith('.')):
			print('go!')
			out = subprocess32.check_output(['./backend.py', user, channel, msg])
			print('done, got this:')
			print(out)
			self.notice(channel, out.splitlines()[0])

	def kickedFrom(self, channel, user, msg):
		print('kicked, quitting')
		self.quit()

class DevBotFactory(ClientFactory):
	protocol = DevBot
	IRCClient.deferred=Deferred()

def main(reactor):
	ircEndpoint = clientFromString(reactor, "tls:chat.freenode.net:6697")

	myReconnectingService = ClientService(ircEndpoint, DevBotFactory())
	myReconnectingService.startService()

	return IRCClient.deferred

react(main, [])

print('done')
