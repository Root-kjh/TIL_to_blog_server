from elasticsearch import Elasticsearch
import json

class ElasticSearch:
    es = Elasticsearch(hosts="localhost", port=9200)

    @classmethod
    def find_by_keyword(cls, keyword):
        #  curl -XGET 'localhost:9200/til/_search?&pretty=true&q=PEP8&_source=name,path'
        res = cls.es.search(
            index = "til", doc_type = "_doc",
            body = {
                "query":{
                    "pretty":"true",
                    "q": keyword,
                    "fields": "name,path"
                }
            }
        )
        return (json.dumps(res, ensure_ascii=False, indent=4))