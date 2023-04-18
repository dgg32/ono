import os
from neo4j import GraphDatabase

host = os.environ.get('NEO4J_URL')
#host = "bolt://localhost:7687"
user = os.environ.get('NEO4J_USER')
password = os.environ.get('NEO4J_PASS')

def run_query(query):
    driver = GraphDatabase.driver(host, auth=(user, password))
    response = []
    with driver.session() as session:
        result = session.run(query)
        response = [r.values()[0] for r in result]
    return response

if __name__ == '__main__':
    query = 'MATCH (w:Word {word: "きっちり"}) <-[r:SIMILAR_TO]-(o:Word) RETURN o.word AS result LIMIT 10'
    print (run_query(query))




