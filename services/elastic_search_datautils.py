'''
Created on 13-Sep-2019

@author: prabhu88
'''
from services.apibase import APIBase
import os


class elasticDTO(object):
    def __init__(self, **kwargs):
        self.index = kwargs['index']
        self.type = kwargs['type']
        self.id = kwargs['id']
        self.user = kwargs['user']
        self.post_date = kwargs['post_date']
        self.message = kwargs['message']      
        
class elasticDataUtils(object):
    
    def getDefault(self,dict_or_object):
        if type(dict_or_object) == type(dict()):
            kwargs = dict_or_object
        else:
            kwargs = dict_or_object.__dict__
        default_dict = {}
        default_dict['index'] = kwargs.get('index', 'datalogue')
        default_dict['type'] = kwargs.get('type', '_doc')
        default_dict['id'] = kwargs.get('id')
        default_dict['user'] = kwargs.get('user', 'prabhu')
        default_dict['post_date'] = kwargs.get('post_date')
        default_dict['message'] = kwargs.get('message')     
                
        return elasticDTO(**default_dict)
    
def getElasticPayload(params_dict):
    current_dir=os.path.dirname(os.path.abspath(__file__))
    template_dir = current_dir
    template_file='elastic.j2'
    return APIBase().getPayload(template_dir, template_file, params_dict)



if __name__ == '__main__':
    params_dict = {'user': 'kimchy', 'post_date': '2009-11-15T13:12:00', 'message': 'Trying out Elasticsearch, so far so good?'}
    payload=getElasticPayload(params_dict)
    print(payload)