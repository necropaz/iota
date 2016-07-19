# iota - Python package

This is a package for python which can be
used to handle with the IOTA API. It is very easy to install it with pip (for more go to installation). To run the  package it is required to run a IOTA instance (IRI.jar or the IOTA Wallet).
When you run an instance from the iota class you have special values which let you error handling or help other things.

## What I need to run an iota instance?

- [ ] Install the latest IOTA release from : [IOTA Node](https://github.com/IOTAledger/iota-gui-beta/releases)
- [ ] the python package sys, json, urllib2 are required

## Installation

If you already have installed pip then you can skip this point and can directly install the package with pip.
For other OS go to: [installing pip](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py)
In Ubuntu you can do this:
```ShellSession
$ sudo apt-get install python-pip python-dev build-essential 
$ sudo pip install --upgrade pip 
$ sudo pip install --upgrade virtualenv
```

Now you have pip and can install the package very easy.

```ShellSession
$ sudo pip install -i https://testpypi.python.org/pypi iota
```

## running instance
- First you have to import the package 
```Python
from iota import iota
```

- Now you can run an instance 
```Python
node=iota("HIERCOMESMYSEED")
```

- Access your iota 
```Python
node.searchNewTransaction()
print (node.error)
print (node.txCounter)
```

## Error Handling
There are two types of error handlings in the iota. If a error appears the node print the error to the stdout.
When the instance is running you can check the errors also if you read the string error from the node (iota.error). All error are also written to this error string.
All methods give a None back if there was en error.

## Transaction Counter

There is an txCounter implemented in the iota so you can check the actual tx high with iota.txCounter.


## Iota class

### `iota(seed, address=None)`

Make an instance from iota.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`seed` | string | Yes | 81-char encoded string which contains the accounts seed. The seed must be correctly encoded: only uppercase latin letters and 9’s. No other characters are allowed.
`input` |`address` | string | No | 81-char long address where transaction can be searched.

### `sendMessage(address, message, value)`

Send a message to a specified address.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`address` | string | Yes | 81-char long address of the recipient of a transaction.
`input` |`message` | string | Yes | The message which added to the transation.
`input` |`value` | string | Yes | string the quantity of IOTA’s which should be transferred.
`return` |`jsonData` | json | Yes | Return an error or the answer from the request in JSON.

### `sendRequest(command)`

Send a request to the IOTA Node and return the answer.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`command` | string | Yes | The command which will be send.
`return` |`jsonData` | json | Yes | The answer from the request in JSON.

### `searchNewTransaction(address=None)`
Search for new transaction. If a new is received the txCounter increments an the latest transaction is given back as Hash.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`address` | string | No | 81-char long address of the recipient of a transaction.
`return` |`transaction` | string | Yes | Hash of the last transaction.

### `searchTransaction(address=None)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`seed` | string | No | 81-char encoded string which contains the accounts seed. The seed must be correctly encoded: only uppercase latin letters and 9’s. No other characters are allowed.
`return` |`transaction` | string | Yes | Hash of the last transaction.

### `checkConfirmed()`
Checks if the latest arrived transaction is confirmed.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`return` |`persistence` | int | Yes | The persistence of the latest transaction.

### `searchMessage(transaction, i=0)`
Reade the message out of the transaction. `i` is optional and can say which message in the bundle should be readed.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`transaction` | string | Yes | Hash of the transaction which include the message.
`input` | `i` | int | No | Which message will be read in the bundle. Default to 0.
`return` |`message` | string | Yes | The message which is encoded in trytes.

### `byteToTryte(char)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`char` | char | Yes | ASCII Character which will encoded to a tryte.
`return` |`tryte` | char | Yes | The encoded character as tryte.

### `tryteToByte(tryte)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`tryte` | string | Yes | The tryte which should convertet. (2 chars long)
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
