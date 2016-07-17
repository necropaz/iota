import sys
import json
import urllib2
import os

class iota:

	def sendRequest(self, command):
		try:
			self.stringified = json.dumps(command)
			self.request = urllib2.Request(url="http://localhost:14265", data=self.stringified, headers={'content-type':'application/json'})
			return json.loads(urllib2.urlopen(self.request).read())
		except Exception as e:
			self.error="Can't reach the IOTA Node."+str(e)
			print(self.error)
			return None

	def __init__(self, seed, address=None):
		self.seed = seed
		self.address=address
		self.error=""
		try:
			self.txCounter=len(self.sendRequest({'command':'getTransfers', 'seed': self.seed, 'securityLevel': 1})['transfers'])-1
		except:
			self.txCounter=0
		if address!=None:	
			try:
				self.txAddress=len(self.sendRequest({'command':'getTransfers', 'addresses': [self.address]})['hashes'])-1
			except:
				self.txAddress=0

	def searchTransaction(self, address=None):
		if address!=None:
			self.transaction=self.sendRequest({'command':'findTransactions', 'addresses':[address]})
			try:
				self.length=len(self.transaction['hashes'])-1
				self.data=self.transaction['hashes'][self.length].encode('ascii')
				return self.data
			except Exception as e:
				self.error="No transaction with this address."+str(e)
				return None
		elif self.seed!=None:
			self.transaction=self.sendRequest({'command':'getTransfers', 'seed': self.seed, 'securityLevel': 1})
			try:
				self.length=len(self.transaction['transactions'])-1
				self.data=self.transaction['transactions'][self.length]['hash'].encode('ascii')
				return self.data
			except Exception as e:
				self.error="No transaction with this seed."+str(e)
				return None
		else:
			self.error="Check your Seed."
			return None		
			
	def searchNewTransaction(self, address=None):
		if address!=None:
			self.transaction=self.sendRequest({'command':'findTransactions', 'addresses':[address]})
			try:
				self.length=len(self.transaction['hashes'])-1
				if self.length!=self.txAddress:
					self.data=self.transaction['hashes'][self.length].encode('ascii')
					self.txAddress=self.txAddress+1
				else:
					self.error="No new transaction."
					self.data=False
				return  self.data
			except Exception as e:
				self.error="No transaction with this address."+str(e)
				return None
		elif self.seed!=None:
			self.transaction=self.sendRequest({'command':'getTransfers', 'seed': self.seed, 'securityLevel': 1})
			try:
				self.length=len(self.transaction['transfers'])-1
				if self.length!=self.txCounter:
					self.data=self.transaction['transfers'][self.length]['hash'].encode('ascii')
					self.txCounter=self.txCounter+1
				else:
					self.error="No new transaction."
					self.data=False
				return self.data
			except Exception as e:
				self.error="No transaction with this seed."+str(e)
				return  None
		else:
			self.error="Check your Seed."
			return self.data

	def searchMessage(self, transaction, i=0 ):
		self.bundle=self.sendRequest({'command':'getBundle', 'transaction': transaction})
		try:
			self.data=self.messageDecode(str(self.bundle['transactions'][i]['signatureMessageChunk']))
			self.string=self.data.split('}')
			self.data=self.string[0]+'}'
			return self.data
		except Exception as e:
			self.error="No Message with this transaction."+str(e)
			print(self.error)
			return None

	def checkConformation(self, transaction, i=0 ):
		self.bundle=self.sendRequest({'command':'getBundle', 'transaction': transaction})
		try:
			self.persistence=self.bundle['transactions'][i]['persistence']
			return self.persistence
		except Exception as e:
			self.error="No Message with this transaction."+str(e)
			print(self.error)
			return None

	def sendMessage(self, address, message, value):
		while True:
			self.message=self.messageEncode(message)
			self.command = {'command':'transfer', 'seed': self.seed , 'address': address, 'value' : value, 'message': self.message , 'securityLevel': 1, 'minWeightMagnitude': 13}
			self.data=self.sendRequest(self.command)
			if len(self.data)==2:
				break
			sel.error="The tangle is not solid."
		return self.data

	def genAddress(self):
		while True:
			self.command = {'command':'generateNewAddress', 'seed': self.seed, 'securityLevel': 1, 'minWeightMagnitude': 13}
			self.data=self.sendRequest(self.command)
			try:
				self.address=self.data['address']
				break
			except:
				sel.error="The tangle is not solid."
		return self.address

	def byteToTryte(self, byte):
		self.availValues = "9ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		try:
			self.byte=ord(byte)
			self.firstValue = self.byte % 27
			self.secondValue = (self.byte - self.firstValue) / 27
			self.trytesValue = self.availValues[self.firstValue] + self.availValues[int(self.secondValue)]
			return self.trytesValue
		except Exception as e:
			self.error="Failure in byteToTryte."+str(e)
			print(self.error)
			return None

	def tryteToByte(self, tryte):
		self.availValues = "9ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		try:
			self.firstValue = self.availValues.rfind(tryte[0])
			self.secondValue = self.availValues.rfind(tryte[1])
			self.byte=(self.secondValue*27)+self.firstValue
			self.data=str(chr(self.byte))
			return self.data
		except Exception as e:
			self.error="Failure in tryteToByte."+str(e)
			print(self.error)
			return None

	def messageEncode(self, message):
		self.encoded=""
		try:
			for self.i in message:
				self.encoded= self.encoded + self.byteToTryte(self.i)
			return self.encoded
		except Exception as e:
			self.error="Failure in messageEncode."+str(e)
			print(self.error)
			return None

	def messageDecode(self, trytes):
		self.decoded=""
		try:
			for self.i in range(0,len(trytes)-1,2):
				self.decoded= self.decoded + self.tryteToByte(trytes[self.i]+trytes[self.i+1])
			return self.decoded
		except Exception as e:
			self.error="Failure in messageDecode."+str(e)
			print(self.error)
			return None
