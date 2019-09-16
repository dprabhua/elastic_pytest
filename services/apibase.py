'''
Created on 13-Sep-2019

@author: prabhu88
'''
import requests, jinja2
from requests.auth import HTTPBasicAuth
import traceback
import json


class APIBase():
    
    def __init__(self):
        self.headers = "Content-Type: application/json"
    
#     base_url = "https://localhost:9200/"
#     endpoints= { 'post': "post", 'patch' : "patch",
#                  'get': "get", 'put': "put",
#                  'delete': "delete",
#                  'base_auth': "basic-auth/{0}/{1}"  
#     }
#     
    def get_url(self, name, idim=None):
        if name in self.endpoints.keys():
            if idim is None: 
                return self.base_url+self.endpoints[name]
            else:
                return self.base_url+self.endpoints[name]+"/"+str(idim) 

    def http_post(self, payload):
        try:
            res = requests.post(self.url, headers=self.headers, data=payload, verify=False)
            print(json.dumps(res.json(), indent=4, sort_keys=True))
            res.raise_for_status()
            print("# Post Method Passed")
            return res
        except requests.HTTPError as er:
            print(traceback.format_exc())

    def http_patch(self, payload):
        try:
            res = requests.patch(self.url, headers=self.headers, data=payload, verify=False)
            print(json.dumps(res.json(), indent=4, sort_keys=True))
            res.raise_for_status()
            print("# Patch Method Passed")
            return res
        except requests.HTTPError as er:
            print(traceback.format_exc())

    def http_put(self, payload):
        try:
            res = requests.put(self.url, headers=self.headers, data=payload, verify=False)
            print(json.dumps(res.json(), indent=4, sort_keys=True))
            res.raise_for_status()
            print("# Put Method Passed")
            return res
        except requests.HTTPError as er:
            print(traceback.format_exc())

    def http_get(self, payload):
        try:
            res = requests.get(self.url, headers=self.headers, data=payload, verify=False)
            print(json.dumps(res.json(), indent=4, sort_keys=True))
            res.raise_for_status()
            print("# Get Method Passed")
            return res
        except Exception as er:
            print(traceback.format_exc())
            return res

    def http_delete(self, payload):
        try:
            res = requests.delete(self.url, headers=self.headers, data=payload, verify=False)
            print(json.dumps(res.json(), indent=4, sort_keys=True))
            res.raise_for_status()
            print("# Delete Method Passed")
            return res
        except requests.HTTPError as er:
            print(traceback.format_exc())
            return res

    def getPayload(self, template_dir, template_file, params_dict, keys_to_remove=None):

        print("Creating Jinja2 environment with template %s" % template_file)
        print(template_dir)
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=template_dir),
                                 trim_blocks=True,
                                 lstrip_blocks=True)
        template = env.get_template(template_file)
        
        result = template.render(params_dict)
        if keys_to_remove is not None:
            # Convert to dict
            result = json.loads(result)
            # remove keys from result
            [result.pop(key, None) for key in keys_to_remove]
            # convert dict to json string
            result = json.dumps(result)

        return result
    

if __name__ == '__main__':
    pass