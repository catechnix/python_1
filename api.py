"""
API are ...
* a way for two pieces of software to talk to each other
* the interface for software systems
* sets of requirements that govern how one application can talk to each other

Represental State Transfer (REST)
* API framework intended to build simpler web services than SOAP
* Another use for the HTTP protocol
* Popular due to performance, scale, simplicity and reliability
* Technically an API framework
* framework -- allows for the person to have some decision to change, protocol has the same activity, no change

XML-RPC and JSON-RPC:
* simple framework for communicating over HTTP
* RPC = Remote procedure call: When one system requests another system to execute code
* Offer XML and JSON data formats respectivly

What is REST:
* Representational state transfer
* API framework built on HTTP
* APIs often referred to as web services
* popular due to performance, scale, simplicity and reliability
Get, Post, Put, Delete -- get info from the server, post new info, put: update info in the server

A look under the hood of REST:
* THE URL: What are you requesting?
http://maps.googleapis.com/maps/api/geocode/json?address=sanjose

http://maps.googleapis.com ->server or host, resolve to the IP or the host to connect to 
/maps/api/geocode/json -> resource, the location of the data or object of interest on the server
?address=sanjose ->parameters, details to scope, filter, or clarify a request, often optional

HTTP verb: POST: create, GET: Read, PUT: update, PATCH: update, DELETE: delete

REST APIs are built on the HTTP protocol
Requests and Responses
How are URLs constructed
Methods, Status codes and headers used with REST APIs
Authentication options for HTTP









"""
