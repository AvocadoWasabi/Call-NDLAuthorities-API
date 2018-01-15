import requests
import json
import urllib.parse

def main():
    end_point = 'http://id.ndl.go.jp/auth/ndla'
    keyword = 'インターネット' #means Internet in Japanese.

    #make query
    #Make SPARQL Query, which searches authority data of the keyword
    query = ('PREFIX xl: <http://www.w3.org/2008/05/skos-xl#>'
            'PREFIX skos: <http://www.w3.org/2004/02/skos/core#>'
            'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>'
            'PREFIX rda: <http://RDVocab.info/ElementsGr2/>'
            'PREFIX ndl: <http://ndl.go.jp/dcndl/terms/>'
            'PREFIX foaf: <http://xmlns.com/foaf/0.1/>'
            'SELECT ?uri1 WHERE{'
            '   ?uri1 rdfs:label "' + keyword + '"'
            '}')

    #URL encode
    parameter = urllib.parse.urlencode({'query' : query, 'output' : 'json'})
    #make whole URL
    url = end_point + '?' + parameter

    result = requests.get(url)
    try:
        data = json.loads(result.text)
    except json.decoder.JSONDecodeError:
        #JSONDecodeError happens if query is incorrect
        #print API's Error message
        print(result.text)

    #print result
    print(data)

if __name__ == '__main__':
    main()