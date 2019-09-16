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
        es_dict={ 'index': 'datalogue', 'id': '5', 'user': 'prabhu', 'post_date': '2009-11-15T13:12:00', 'message': 'Trying out Elasticsearch, so far so good?'}
        es_dto=elasticDataUtils().getDefault(es_dict)
        self.es_svc.create_record(es_dto)
        es_dto.user = 'test_user'
        self.es_svc.update_record(es_dto)
        self.es_svc.get_record(es_dto)

if __name__ == '__main__':
     
    #high priority sanity cases
    crud_suite  = unittest.TestSuite()     
    crud_suite.addTest(ElasticSearchRecords('test001_CRUDSimpleRecord'))
    runner = unittest.TextTestRunner()
    runner.run(crud_suite)