from elasticsearch import Elasticsearch

class ElasticSearch:
    es = Elasticsearch(hosts="localhost", port=9200)

    @classmethod
    def find_by_keyword(cls, keyword):
        #  curl -XGET 'localhost:9200/til/_search?&pretty=true&q=PEP8&_source=name,path'
        res = cls.es.search(
            index = "til", doc_type = "_doc",
            body = {
                "query":{"multi_match": {
                    "query": keyword,
                    "fields": ["name", "context"]
                }},
                "_source": ["name", "path"]
            }
        )
        return res