""" Example showing how to use Natural Language Searc APIs via python SDK.
"""

__author__      = "Vikas Raykar"
__email__       = "viraykar@in.ibm.com"
__copyright__   = "IBM India Pvt. Ltd."

import os
import json
from pprint import pprint
from props import *

from cfapicatalog.sdk import Catalog
from cfapinls.sdk import NaturalLanguageSearch

#------------------------------------------------------------------------------
# Initialize. 
#------------------------------------------------------------------------------

catalog = Catalog(api_gateway_url=props['api_gateway_url'],
                  api_key=props['api_key'],
                  version=props['api_version'],
                  data_collection_opt_out=props['data_collection_opt_out'])

nls = NaturalLanguageSearch(api_gateway_url=props['api_gateway_url'],
                            api_key=props['api_key'],
                            version=props['api_version'],
                            data_collection_opt_out=props['data_collection_opt_out'])

#------------------------------------------------------------------------------
# FASHION QUOTE
#------------------------------------------------------------------------------
# Check if the url and API key is valid.
status,response = nls.fashion_quote()
print(status)
pprint(response)

#------------------------------------------------------------------------------
# ADD SOME SAMPLE PRODUCTS TO THE CATALOG
#------------------------------------------------------------------------------
# Some sample data where each product in the catalog is in a json format
# described earlier.
catalog_folder = os.path.join(props['catalog_folder'],'jsons')
json_filenames = [f for f in os.listdir(catalog_folder) if not f.startswith('.')]

for filename in json_filenames:
    # Load the json file.
    with open(os.path.join(catalog_folder,filename),'r') as f:
        data = json.loads(f.read())

    status,response = catalog.add_product(catalog_name=props['catalog_name'],
                                          id=data['id'],
                                          data=data,
                                          download_images=False)

    print(status)
    pprint(response)

#------------------------------------------------------------------------------
# CATALOG NAMES
#------------------------------------------------------------------------------
status,response = catalog.names()
print(status)
pprint(response)

#------------------------------------------------------------------------------
# CATALOG INFO
#------------------------------------------------------------------------------
status,response = catalog.info(catalog_name=props['catalog_name'])
print(status)
pprint(response)

query_text = 'blue joggers for men'
#query_text = 'blue kurta for my neice'

#------------------------------------------------------------------------------
# BASIC TEXT SEARCH
#------------------------------------------------------------------------------
status,response = catalog.text_search(catalog_name=props['catalog_name'],
                                      query_text = query_text,
                                      max_number_of_results=12)
print(status)
pprint(response)

for product in response['products']:
  status,response = catalog.get_product(catalog_name=props['catalog_name'],
                                        id=product['id'])
  print('[%s] %s'%(product['id'],response['data']['name']))

#------------------------------------------------------------------------------
# natural_language_search
#------------------------------------------------------------------------------
status,response = nls.natural_language_search(catalog_name=props['catalog_name'],
                                              query_text = query_text,
                                              max_number_of_results=12,
                                              max_number_of_backoffs=5,
                                              return_elasticsearch_queries=False)
print(status)
pprint(response)

for product in response['products']:
  status,response = catalog.get_product(catalog_name=props['catalog_name'],
                                        id=product['id'])
  print('[%s] %s'%(product['id'],response['data']['name']))

#------------------------------------------------------------------------------
# elasticsearch_queries
#------------------------------------------------------------------------------
status,response = nls.elasticsearch_queries(query_text = query_text,
                                            max_number_of_results=12,
                                            max_number_of_backoffs=5)
print(status)
pprint(response)

#------------------------------------------------------------------------------
# parse
#------------------------------------------------------------------------------
status,response = nls.parse(query_text=query_text,
                            include_apparel_hyponyms=True,
                            include_apparel_hypernyms=True,
                            return_search_terms=True)
print(status)
pprint(response)

#------------------------------------------------------------------------------
# spell_correct
#------------------------------------------------------------------------------
status,response = nls.spell_correct(query_text=query_text)
print(status)
pprint(response)

#------------------------------------------------------------------------------
# DELETE CATALOG
#------------------------------------------------------------------------------
"""
status,response = catalog.delete(catalog_name=props['catalog_name'],
                                 delete_images=False)
print(status)
pprint(response)
"""

