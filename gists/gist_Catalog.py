""" Example showing how to use catalog APIs via python SDK.
"""

import os
import json
from pprint import pprint
from props import *

from cfapicatalog.sdk import Catalog

#------------------------------------------------------------------------------
# Initialize. 
#------------------------------------------------------------------------------

catalog = Catalog(api_gateway_url=props['api_gateway_url'],
                  api_key=props['api_key'],
                  version=props['api_version'],
                  data_collection_opt_out=props['data_collection_opt_out'])


#------------------------------------------------------------------------------
# FASHION QUOTE
#------------------------------------------------------------------------------
# Check if the url and API key is valid.
status,response = catalog.fashion_quote()
print(status)
pprint(response)

#------------------------------------------------------------------------------
# ADD METADATA TO THE CATALOG
#------------------------------------------------------------------------------
# Post any metadata you want to track for the catalog. Suggested fields
data={}
#A friendly name for display purposes.
data['friendly_name'] = 'sample' 
# The url of the hero image.
data['hero_image_url'] = 'https://cognitivefashion.github.io/img/portfolio/logo_cf.svg' 
# A brief description.
data['description'] = 'A sample catalog to test IBM Research AI for Fashion APIs.' 

status,response = catalog.add_metadata(catalog_name=props['catalog_name'],
                                       data=data)
print(status)
pprint(response)

#------------------------------------------------------------------------------
# ADD PRODUCTS TO THE CATALOG
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
                                          download_images=True)

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

pprint(response)


#------------------------------------------------------------------------------
# GET PRODUCT
#------------------------------------------------------------------------------
status,response = catalog.get_product(catalog_name=props['catalog_name'],
                                      id='SKLTS16AMCWSH8SH20')
print(status)
pprint(response)


#------------------------------------------------------------------------------
# GET IMAGE
#------------------------------------------------------------------------------
status,response = catalog.image_url(catalog_name=props['catalog_name'],
                                    id='SKLTS16AMCWSH8SH20',
                                    image_id='1',
                                    return_product_info=True)
print(status)
pprint(response)

# If you need a image crop
status,response = catalog.image_url(catalog_name=props['catalog_name'],
                                    id='SKLTS16AMCWSH8SH20',
                                    image_id='1',
                                    top_left_x=50,
                                    top_left_y=50,
                                    width=100,
                                    height=100)
print(status)
pprint(response)

#------------------------------------------------------------------------------
# UPDATE PRODUCT
#------------------------------------------------------------------------------
data = {}
data['out_of_stock'] = 'yes'
status,response = catalog.update_product(catalog_name=props['catalog_name'],
                                         id='SKLTS16AMCWSH8SH20',
                                         data=data,
                                         download_images=True)
print(status)
pprint(response)


#------------------------------------------------------------------------------
# DELETE PRODUCT
#------------------------------------------------------------------------------
status,response = catalog.delete_product(catalog_name=props['catalog_name'],
                                      id='SKLTS16AMCWSH8SH20',
                                      delete_images=False)
print(status)
pprint(response)

#------------------------------------------------------------------------------
# BASIC TEXT SEARCH
#------------------------------------------------------------------------------
status,response = catalog.text_search(catalog_name=props['catalog_name'],
                                      query_text = 'male',
                                      max_number_of_results=12)
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

