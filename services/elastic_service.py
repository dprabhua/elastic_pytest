'''
Created on 13-Sep-2019

@author: prabhu88
'''
from services.apibase import APIBase
from services.elastic_search_datautils import elasticDataUtils, getElasticPayload

class ElasticService(APIBase):
    
    def __init__(self):
        self.base_url = "http://localhost:9200/"
        self.headers = {'content-type': 'application/json'}
    
    def create_record(self, es_dto, msg=None):
        self.url=self.base_url + '{}/{}/{}'.format(es_dto.index, es_dto.type, es_dto.id)
        try:
            self.payload=getElasticPayload(es_dto.__dict__)
            response = self.http_post(self.payload)
            print(response.json())
            response.raise_for_status()
        except Exception as e:
            if msg:
                assert response.status_code == msg["status"], "Response status code not matching with expected Error code"
                assert response.json() == msg, "Response Error message not matching with expected message"
                print("The Error message is matching the api returned Error message")
                return
            raise RuntimeError("Unable to Create the Record due to : %s" %e)       
    
    def update_record(self, es_dto, msg=None):
        self.url=self.base_url + '{}/{}/{}'.format(es_dto.index, es_dto.type, es_dto.id)
        try:
            self.payload=getElasticPayload(es_dto.__dict__)
            response = self.http_post(self.payload)
            print(response.json())
            response.raise_for_status()
        except Exception as e:
            if msg:
                assert response.status_code == msg["status"], "Response status code not matching with expected Error code"
                assert response.json() == msg, "Response Error message not matching with expected message"
                print("The Error message is matching the api returned Error message")
                return
            raise RuntimeError("Unable to Update the Record due to : %s" %e)  
        
    def delete_record(self, es_dto, msg=None):
        self.url=self.base_url + '{}/{}/{}'.format(es_dto.index, es_dto.type, es_dto.id)
        try:
            self.payload=getElasticPayload(es_dto.__dict__)
            response = self.http_delete(self.payload)
            response.raise_for_status()
            print(response.json())
        except Exception as e:
            if msg:
                #assert response.status_code == msg["status"], "Response status code not matching with expected Error code"
                assert response.json() == msg, "Response Error message not matching with expected message"
                print("The Error message is matching the api returned Error message")
                return
            raise RuntimeError("Unable to Delete the Record due to : %s" %e)  
        
        
    def get_record(self, es_dto, msg=None):
        self.url=self.base_url + '{}/{}/{}'.format(es_dto.index, es_dto.type, es_dto.id)
        try:
            self.payload=getElasticPayload(es_dto.__dict__)
            response = self.http_get(self.payload)
            response.raise_for_status()
            print(response.json())
        except Exception as e:
            if msg:
                #assert response.status_code == msg["status"], "Response status code not matching with expected Error code"
                assert response.json() == msg, "Response Error message not matching with expected message"
                print("The Error message is matching the api returned Error message")
                return
            raise RuntimeError("Unable to Get the Record due to : %s" %e)  
        
if __name__ == '__main__':
    es_svc = ElasticService()
    es_dict={ 'index': 'datalogue', 'id': '5', 'user': 'kimchy', 'post_date': '2009-11-15T13:12:00', 'message': 'Trying out Elasticsearch, so far so good?'}
    es_dto=elasticDataUtils().getDefault(es_dict)
    es_svc.create_record(es_dto)
    es_svc.get_record(es_dto)
    pass
