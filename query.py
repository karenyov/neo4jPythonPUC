from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

db = GraphDatabase ("http://localhost:7474", username="neo4j", password="nosql")

q = 'MATCH (u:Usuario)-[r:follows]->(m:Usuario) WHERE u.name="Alice" RETURN u, type(r), m'

results = db.query(q, returns=(client.Node, str, client.Node))

for r in results:
    print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))
