'''
Created on 13-Sep-2019

@author: prabhu88
'''
import unittest, time, os
import pytest, logging

from services.elastic_search_datautils import elasticDataUtils
from services.elastic_service import ElasticService
 
 
class ElasticSearchRecords(unittest.TestCase):
    """
    class for all the test cases in clouds UI page
    """
    @classmethod            
    def setUpClass(self):
        print("Suite setup")
        self.es_svc = ElasticService()
        
    @classmethod            
    def tearDownClass(self):
        print("Suite teardown")
        
    @pytest.mark.sanity
    def test001_CRUDSimpleRecord(self):
        '''
        Basic Testcase to verify the Elastic Search Create, Update, Get and Delete API for simple json document
        
        '''
        es_dict={ 'index': 'datalogue', 'id': '1', 'user': 'prabhu', 'post_date': '2009-11-15T13:12:00', 'message': 'Trying out Elasticsearch, so far so good?'}
        es_dto=elasticDataUtils().getDefault(es_dict)
        self.es_svc.create_record(es_dto)
        es_dto.user = 'test_user'
        self.es_svc.update_record(es_dto)
        self.es_svc.get_record(es_dto)
        
    @pytest.mark.sanity
    def test002_CRUDSimpleRecord(self):
        '''
        Basic Testcase to verify the Elastic Search Create, Update, Get and Delete API for simple json document
        
        '''
        es_dict={ 'index': 'datalogue', 'user': 'prabhu', 'post_date': '2009-11-15T13:12:00', 'message': 'Trying out Elasticsearch, so far so good?'}
        es_dto=elasticDataUtils().getDefault(es_dict)
        self.es_svc.create_record(es_dto)
        es_dto.message = 'The message is updated in Testcases to verify the PUT method'
        self.es_svc.update_record(es_dto)
        self.es_svc.get_record(es_dto)
        self.es_svc.delete_record(es_dto)
        
    
        
    @pytest.mark.regression
    def test003_ValidateIndexApi(self):
        '''
        Basic Testcase to validate the Elastic Search Index API Error Message
        1. Invalid Index
        2. Invalid Id
        
        '''
        es_dict={ 'index': 'datalogue', 'id': '1', 'user': 'prabhu', 'post_date': '2009-11-15T13:12:00', 'message': 'Trying out Elasticsearch, so far so good?'}
        es_dto=elasticDataUtils().getDefault(es_dict)
        self.es_svc.create_record(es_dto)
        es_dto.index="Wrong_index"     
        msg={
                "error": {
                    "index": "Wrong_index",
                    "index_uuid": "_na_",
                    "reason": "no such index [Wrong_index]",
                    "resource.id": "Wrong_index",
                    "resource.type": "index_expression",
                    "root_cause": [
                        {
                            "index": "Wrong_index",
                            "index_uuid": "_na_",
                            "reason": "no such index [Wrong_index]",
                            "resource.id": "Wrong_index",
                            "resource.type": "index_expression",
                            "type": "index_not_found_exception"
                        }
                    ],
                    "type": "index_not_found_exception"
                },
                "status": 404
            }
        self.es_svc.get_record(es_dto, msg)
        self.es_svc.delete_record(es_dto, msg)
        es_dto.index="datalogue" 
        es_dto.id="Invalid_Id"
        msg={
            "_id": "Invalid_Id",
            "_index": "datalogue",
            "_type": "_doc",
            "found": False
        }
        self.es_svc.get_record(es_dto, msg)

if __name__ == '__main__':
     
    #high priority sanity cases
    crud_suite  = unittest.TestSuite()     
    crud_suite.addTest(ElasticSearchRecords('test003_ValidateIndexApi'))
    runner = unittest.TextTestRunner()
    runner.run(crud_suite)