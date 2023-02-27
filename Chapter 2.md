# Application Layer
## Overview
- principle of network applications
- Web and HTTP
- Email SMTP IMAP
- domain name system (DNS)
- p2p applications
- video streaming and content
- socket programming with UDP TCP

## Some network apps
	- social networking
	- email
	- streaming stored video

## Creating a network app
- Weite programs that:
	- run on different end systems
	- communicate over network
	- web server software, communicates with browser software
	
## Client-server paradigm
- server:
	- always on host
	- permanent ip address
	- often in data centers for scaling
- clients:
	- contact, communicate with server
	- may be intermittently connected
	- may have dynamic ip addresses
	- do not communicate directly with each other
	- examples: HTTP, IMAP, FTP
	
## Peer - peer architecture
- no always on server
- arbitrary end systems directly communicate
- peers request service from other peers, provide service in return to other peers
	- self scalability - new peers bring new service capacity as well as new service demands
- peers are intermittently connected and change ip addresses
	- complex management
- example: P2P file sharing

## Processes communicating
	- process: program running within a host
	- within same host, two processes communicate using inter-process communication
	- processes in different hosts communicate by exchanging
	- client process: process that initiates communication
	- server process: process that waits to be contacted

## Sockets
- process sends/receives messages to/from its socket
- combination of host ip and port
	- port - application identifier (25 - email, 443 - https, 80 - http)
- two sockets involved: one on each side

## Addressing processes
- to receive messages, process must have ==identifier==
- host device has unique 32-bit ip address
- ==identifier== includes both IP address and port numbers associated with process on host
- IP address: ------, Port number: 80 (HTTP)

## Application layer protocol defines:
- types of messages exchanged
- message syntax
- message semantics
	- meaning of info in fields
- rules
	- when and how processes send and respond to messages
- open protocols
	- defined in RFCs (request for comments), everyone has access to protocol definition
	- allows for interoperability
	- HTTP, SMTP
- proprietary protocols
	- ex: skype