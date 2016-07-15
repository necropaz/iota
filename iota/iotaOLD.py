import sys
import json
import urllib2
import os

class IOTA:
	def __init__(self, seed):
		self.seed = seed
		try:
			self.txCounter=len(sendRequest({'command':'getTransfers', 'seed': self.seed, 'securityLevel': 1})['transactions']-1
		except:
			self.txCounter=0
	
	def sendRequest(self, command):
		try:
			self.stringified = json.dumps(command)
			self.request = urllib2.Request(url="http://localhost:14265", data=self.stringified, headers={'content-type':'application/json'})
			return json.loads(urllib2.urlopen(request).read())
		except:
			return "Can not reach IRI or you not enter a string. Please start IOTA."

	def searchTransaction(self, address=None):
		if address!=None:
			self.transaction=sendRequest({'command':'findTransactions', 'addresses':[address]})
			try:
				self.length=len(self.transaction['hashes'])-1
				self.data=self.transaction['hashes'][self.length].encode('ascii')
			except:
				self.data=self.transaction
		elif self.seed!=None:
			self.transaction=sendRequest({'command':'getTransfers', 'seed': self.seed, 'securityLevel': 1})
			try:
				self.length=len(self.transaction['transactions'])-1
				self.data=self.transaction['transactions'][self.length]['hash'].encode('ascii')
			except:
				self.data=self.transaction
		else:
			self.data="Check your seed or address."
		return self.data			
			
	def searchNewTransaction(self, address=None):
		if address!=None:
			self.transaction=sendRequest({'command':'findTransactions', 'addresses':[address]})
			try:
				self.length=len(self.transaction['hashes'])-1
				self.data=self.transaction['hashes'][self.length].encode('ascii')
			except:
				self.data=self.transaction
		elif self.seed!=None:
			self.transaction=sendRequest({'command':'getTransfers', 'seed': self.seed, 'securityLevel': 1})
			try:
				self.length=len(self.transaction['transactions'])-1
				if self.length!=self.txCounter:
					self.data=self.transaction['transactions'][self.length]['hash'].encode('ascii')
					self.txCounter=self.txCounter+1
				else:
					self.data="No new Transaction."
			except:
				self.data=self.transaction
		else:
			self.data="Check your seed or address."
		return self.data

	def searchMessage(self, transaction, i=0 ):
		self.bundle=sendRequest({'command':'getBundle', 'transaction': transaction})
		try:
			self.data=messageDecode(str(self.bundle['transactions'][i]['signatureMessageChunk']))
			self.string=self.data.split('}')
			self.data=self.string[0]+'}'
		except:
			self.data=self.bundle
		return self.data

	def sendMessage(self, address, message, value):
		self.message=messageEncode(message)
		command = {'command':'transfer', 'seed': seed , 'address': address, 'value' : value, 'message': self.message , 'securityLevel': 1, 'minWeightMagnitude': 13}
		self.data=sendRequest(command)
		return self.data

	def byteToTryte(self, byte):
		self.availValues = "9ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		try:
			self.byte=ord(byte)
			self.firstValue = self.byte % 27
			self.secondValue = (self.byte - self.firstValue) / 27
			self.trytesValue = self.availValues[self.firstValue] + self.availValues[int(self.secondValue)]
		except:
			self.trytesValue="Failure in byteToTryte. Make sure your input is an ASCII character."
		return self.trytesValue

	def tryteToByte(self, tryte):
		self.availValues = "9ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		try:
			self.firstValue = self.availValues.rfind(tryte[0])
			self.secondValue = self.availValues.rfind(tryte[1])
			self.byte=(self.secondValue*27)+self.firstValue
			self.data=str(chr(self.byte))
		except:
			self.data="Something went Wrong in tryteToByte. Make sure your input  is a Tryte."
		return(self.data)

	def messageEncode(self, message):
		self.encoded=""
		for self.i in message:
			self.encoded= self.encoded + self.byteToTryte(self.i)
		return self.encoded

	def messageDecode(self, trytes):
		self.decoded=""
		for self.i in range(0,len(trytes)-1,2):
			self.decoded= self.decoded + self.tryteToByte(trytes[self.i],trytes[self.i+1])
		return self.decoded
