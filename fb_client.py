from typing import List, Tuple
from SPARQLWrapper import SPARQLWrapper, JSON
import json
import urllib
from pathlib import Path
from tqdm import tqdm


sparql = SPARQLWrapper("http://a800-2:3001/sparql")
sparql.setReturnFormat(JSON)

def get_friendly_name(entity: str) -> str:
    query = ("""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX : <http://rdf.freebase.com/ns/> 
    SELECT (?x0 AS ?value) WHERE {
    SELECT DISTINCT ?x0  WHERE {
    """
             ':' + entity + ' :type.object.name ?x0 . '
                            """
    }
    }
    """)
    # # print(query)
    sparql.setQuery(query)
    try:
        results = sparql.query().convert()
    except urllib.error.URLError:
        print(query)
        exit(0)
    rtn = []
    for result in results['results']['bindings']:
        if result['value']['xml:lang'] == 'en':
            rtn.append(result['value']['value'])

    if len(rtn) == 0:
        query = ("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX : <http://rdf.freebase.com/ns/> 
        SELECT (?x0 AS ?value) WHERE {
        SELECT DISTINCT ?x0  WHERE {
        """
                 ':' + entity + ' :common.topic.alias ?x0 . '
                                """
        }
        }
        """)
        # # print(query)
        sparql.setQuery(query)
        try:
            results = sparql.query().convert()
        except urllib.error.URLError:
            print(query)
            exit(0)
        for result in results['results']['bindings']:
            if result['value']['xml:lang'] == 'en':
                rtn.append(result['value']['value'])

    if len(rtn) == 0:
        return 'null'

    return rtn[0]
if __name__ == '__main__':
    print(get_friendly_name('m.07ylj'))