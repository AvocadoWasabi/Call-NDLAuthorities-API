# Call NDLAuthorities API via Python

## Purpose
This program is a sample for using NDL Authority API and access its database via Python.

## About NDL
NDL means the Natonal Diet Library in Japan.
It supplies searching service for authory data as Web API.
### Website
https://id.ndl.go.jp/auth/ndla
### Description of Functions
http://id.ndl.go.jp/information/function_en/

## SPARQL query
When API is called, SPARQL query is sent as parameter, which actually access database.
So, until getting result of API, at least 3 stage is needed.
API is called -> Run SPARQL query at server side -> Get results as JSON -> (Parse results)

## Requirement
Python 3

## Licence
CC0
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

## Auther
AvocadoWasabi
