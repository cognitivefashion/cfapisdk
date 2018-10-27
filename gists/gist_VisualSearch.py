""" Example showing how to use visual search APIs via python SDK.
"""

from pprint import pprint
from props import *

from cfapivisualsearch.sdk import VisualSearch

#------------------------------------------------------------------------------
# Initialize. 
#------------------------------------------------------------------------------

vs = VisualSearch(api_gateway_url=props['api_gateway_url'],
                  api_key=props['api_key'],
                  version=props['api_version'],
                  data_collection_opt_out=props['data_collection_opt_out'])

# Check if the url and API key is valid.
status,response = vs.fashion_quote()
print(status)
pprint(response)

#------------------------------------------------------------------------------
# VISUAL SEARCH CATEGORIES PREDICTION
#------------------------------------------------------------------------------

"""
#Predict the visual search categories based on product images
status,response = vs.categories_predict(catalog_name=props['catalog_name'],
                                        clear_cache=True,
                                        ignore_non_primary_images=False,
                                        visual_search_categories_threshold=0.0)

# Get the status of the visual search categories prediction
status,response = vs.categories_status(catalog_name=props['catalog_name'])
pprint(response)

#Delete the visual search categories prediction process
status,response = vs.categories_delete(catalog_name=props['catalog_name'])
pprint(response)
"""

# Get all visual search categories 
status,response = vs.visual_search_categories(catalog_name=props['catalog_name'])
pprint(response)

# Get all visual browse categories 
status,response = vs.visual_browse_categories(catalog_name=props['catalog_name'])
pprint(response)

#------------------------------------------------------------------------------
# BUILD VISUAL SEARCH INDEX
#------------------------------------------------------------------------------

"""
# Build the visual search index.
status,response = vs.index_build(catalog_name=props['catalog_name'],
                                 per_category_index=False,
                                 full_index=True,
                                 group_by=False,
                                 group_by_k=5)
pprint(response)

# Get the status of the visual search index. 
status,response = vs.index_status(catalog_name=props['catalog_name'])
pprint(response)

# Delete the visual search index. 
status,response = vs.index_delete(catalog_name=props['catalog_name'])
pprint(response)
"""

#------------------------------------------------------------------------------
# VISUAL BROWSE
#------------------------------------------------------------------------------

# Get other visually similar products in the catalog.
status,response = vs.browse(catalog_name=props['catalog_name'],
                            id='ABOFA15AMCWJG10449',
                            image_id='1',
                            max_number_of_results=5,
                            per_category_index=True,
                            category=None,
                            use_cache=False,
                            sort_option='visual_similarity',
                            unique_products=True)
pprint(response)

#------------------------------------------------------------------------------
# VISUAL SEARCH
#------------------------------------------------------------------------------

# Get visually similar products in the catalog for an uploaded image.
status,response = vs.search(catalog_name=props['catalog_name'],
                            image_filename='test_image.jpeg',
                            max_number_of_results=5,
                            per_category_index=True,
                            category=None,
                            visual_search_categories_threshold=0.0,
                            sort_option='visual_similarity',
                            group_by=None,
                            unique_products=True)
pprint(response)

