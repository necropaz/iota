# iota - Python package

This is a package for python which can be
used to handle with the IOTA API. It is very easy to install it with pip (for more go to installation). To run the  package it is required to run a IOTA instance (IRI.jar or the IOTA Wallet).
When you run an instance from the iota class you have special values which let you error handling or help other things.

## What I need to run an iota instance?

- [ ] Install the latest IOTA release from : [IOTA Node](https://github.com/IOTAledger/iota-gui-beta/releases)
- [ ] the python package sys, json, urllib2 and os are required

## Installation

To install the package it is very easy if you have installed pip.

```ShellSession
$ sudo pip install iota
```

## running instance

1. First you have to import the package 
```Python
from iota import iota
```

2. Now you can run an instance 
```Python
node=iota("HIERCOMESMYSEED")
```

3. Access your iota 
```Python
node.searchNewTransaction()
print (node.error)
print (node.txCounter)
```

## package functions

### `sendMessage(address, message, value)`

Send a message to a specified Adress.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`seed` | string | Yes | 81-char encoded string which contains the accounts seed. The seed must be correctly encoded: only uppercase latin letters and 9’s. No other characters are allowed.
`input` |`address` | string | Yes | 81-char long address of the recipient of a transaction.
`input` |`message` | string | Yes | The message which added to the transation.
`input` |`value` | string | Yes | string the quantity of IOTA’s which should be transferred.

### `sendRequest(command)`

Send a request to the IOTA Node and return the answer.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`command` | string | Yes | The command which will made the request.
`return` |`jsonData` | string | Yes | The answer from the request in JSON.

### `searchNewTransaction(address)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`address` | string | Yes | 81-char long address of the recipient of a transaction.
`return` |`transaction` | string | Yes | Hash of the last transaction.

### `readSendersAddress(transaction)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`transaction` | string | Yes | Hash of the transaction from which you wanna read the sender address.
`return` |`address` | string | Yes | Sender address of the transaction.

### `getNewTransfer(seed)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`seed` | string | Yes | 81-char encoded string which contains the accounts seed. The seed must be correctly encoded: only uppercase latin letters and 9’s. No other characters are allowed.
`return` |`transaction` | string | Yes | Hash of the last transaction.

### `searchMessage(transaction)`


Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`transaction` | string | Yes | Hash of the transaction which include the message.
`return` |`message` | string | Yes | The message which is encoded in Trytes.

### `byteToTryte(char)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`char` | char | Yes | ASCII Character which will encoded to a Tryte.
`return` |`tryte` | char | Yes | The encoded character as tryte.

### `tryteToByte(char1,char2)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`char1` | char | Yes | First Tryte Character.
`input` |`char2` | char | Yes | Second Tryte Character.
`return` |`byte` | char | Yes | The decoded Byte as ASCII character.

### `messageEncode(message)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`message` | string | Yes | Message which will be encoded to tyrtes.
`return` |`trytes` | string | Yes | The encoded message in trytes

### `messageDecode(trytes)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`trytes` | string | Yes | Trytes which will be decoded to ASCII characters.
`return` |`message` | string | Yes | The decoded Message.
