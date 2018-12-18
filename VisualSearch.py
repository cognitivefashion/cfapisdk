#
# Licensed Materials - Property of IBM
#
# AI For Fashion 
#
# (C) Copyright IBM Corp. 2018 All Rights Reserved
#
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with
# IBM Corp.
#

""" Visual Search APIs.
https://cognitivefashion.github.io/slate/#visual-search
"""

__author__      = "Vikas Raykar"
__email__       = "viraykar@in.ibm.com"
__copyright__   = "IBM India Pvt. Ltd."

__all__ = ["VisualSearch"]

import os
import json
import requests
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

class VisualSearch():
    """ Visual Search APIs.
    """
    def __init__(self,
                 api_gateway_url,
                 api_key,
                 version='v1',
                 data_collection_opt_out=False):
        """ Initialization.

        :params:
            - api_gateway_url : str
            - api_key : str    
            - data_collection_opt_out : boolean, optional (default: False)
        """

        self.api_gateway_url = api_gateway_url
        self.version = version

        self.headers = {}
        self.headers['X-Api-Key'] = api_key
        self.headers['X-Data-Collection-Opt-Out'] = str(data_collection_opt_out).lower()

    #--------------------------------------------------------------------------
    # Get a random fashion quote.  
    # GET /v1/fashion_quote
    #--------------------------------------------------------------------------
    def fashion_quote(self):
        """ Get a random fashion quote. 
        """
        params = {}

        api_endpoint = '%s/fashion_quote'%(self.version)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                headers=self.headers,
                                params=params)        

        return response.status_code,response.json()

    #--------------------------------------------------------------------------
    # Build the visual search index.
    # POST /v1/catalog/{catalog_name}/visual_search_index
    # params - per_category_index
    #          full_index
    #          group_by
    #          group_by_k
    #--------------------------------------------------------------------------
    def index_build(self,catalog_name,
                    per_category_index=False,
                    full_index=True,
                    group_by=False,
                    group_by_k=5):
        """ Build the visual search index.
        
        :params:
            - catalog_name : str
                the catalog name
            - per_category_index : str, optional(default False)
                If this is set to True builds a separate visual search index 
                for each category specified in the prduct json field 
                data['visual_search_category'].
            - full_index : str, optional(default True)    
                If this is set to True builds the the full visual search index 
                along with the separate visual search index for 
                each visual search category.
            - group_by : boolean, optional(default:False)
                If this is set to True the group_by option is enabled. This
                groups the results from visual search into distinct groups 
                according to various criteria. Currently the group_by option 
                works only when full_index is set to True. If full_index is 
                False the group_by is disabled.
            - group_by_k : int, optional(default:5).
                The number of nearest neighbors to use for group_by.                
        """    
        
        params={}
        params['per_category_index'] = str(per_category_index).lower()
        params['full_index'] = str(full_index).lower()
        params['group_by'] = str(group_by).lower()
        params['group_by_k'] = group_by_k

        api_endpoint = '%s/catalog/%s/visual_search_index'%(self.version,
                                                             catalog_name)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.post(url,
                                 headers=self.headers,
                                 params=params)

        return response.status_code,response.json()

    #--------------------------------------------------------------------------
    # Get the status of the visual search index. 
    # GET  /v1/catalog/{catalog_name}/visual_search_index
    #--------------------------------------------------------------------------
    def index_status(self,catalog_name):
        """ Get the status of the visual search index.

        :params:
            - catalog_name : str
                the catalog name   
        """
        params={}

        api_endpoint = '%s/catalog/%s/visual_search_index'%(self.version,
                                                             catalog_name)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                headers=self.headers,
                                params=params)

        return response.status_code,response.json()

    #--------------------------------------------------------------------------
    # Delete the visual search index. 
    # DELETE  /v1/catalog/{catalog_name}/visual_search_index
    #--------------------------------------------------------------------------
    def index_delete(self,catalog_name):
        """ Delete the visual search categories prediction process

        :params:
            - catalog_name : str
                the catalog name           
        """
        params={}

        api_endpoint = '%s/catalog/%s/visual_search_index'%(self.version,
                                                             catalog_name)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.delete(url,
                                   headers=self.headers,
                                   params=params)

        return response.status_code,response.json()

    #--------------------------------------------------------------------------
    # Visual Browse
    #
    # Get other visually similar products in the catalog.
    # GET /v1/catalog/{catalog_name}/visual_search/{id}/{image_id}
    # params - max_number_of_results
    #          per_category_index
    #          categort
    #          use_cache
    #          sort_option
    #          unique_products
    #--------------------------------------------------------------------------
    def browse(self,catalog_name,id,image_id,
               max_number_of_results=12,
               per_category_index=False,
               category=None,
               use_cache=True,
               sort_option='visual_similarity',
               unique_products=False):
        """Get other visually similar products in the catalog.

        :params:
            - catalog_name : str
                the catalog name
            - id : str
                the item id  
            - image_id : str
                the image id  
            - max_number_of_results : int, optional (default: 12)
                The maximum number of results to return.   
            - per_category_index : boolean, optional (default: False)
                If this is set to True does visual browse only in the 
                categories specifed in the data['visual_search_category'] field. 
            - category : list of str, optional (default: None)  
                Optionally you can also spaecify a list of categories to search.
                category=['tops','blouses']. The categories have to be valid 
                categories specified in the data['visual_search_category'] field.                    
            - use_cache : boolean, optional (default: True)
                The first time visual browse is called it caches the results in 
                elasticsearch. On subsequent calls the API directly retrieves 
                the results from the cache unless use_cache=False.  
            - sort_option : str, optional (default: 'visual_similarity')
                visual_similarity  : Results are sorted by visual similarity.
                apparel_similarity : Re-sorts the results from visual browse 
                                     using apparel similarity.
            - unique_products : boolean, optional (default: False)
                By default visual browse uses all images available for a product.
                Hence, sometimes in the search results the same product id can 
                appear multiple times (with a different image_id). If this 
                parameter is set to True then the results are post-filtered 
                to contain only unique products (the best matching image_id is
                retained).                                       
        """ 

        params = {}
        params['max_number_of_results'] = max_number_of_results
        params['per_category_index'] = str(per_category_index).lower()
        params['use_cache'] = str(use_cache).lower()
        params['unique_products'] = str(unique_products).lower()
        params['sort_option'] = sort_option
        if category is not None:
            params['category'] = ','.join(category)

        api_endpoint = '%s/catalog/%s/visual_browse/%s/%s'%(self.version,
                                                             catalog_name,
                                                             id,
                                                             image_id)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                headers=self.headers,
                                params=params)

        return response.status_code,response.json()

    #--------------------------------------------------------------------------
    # Visual Search
    #
    # Get visually similar products in the catalog for an uploaded image.
    # POST /v1/catalog/{catalog_name}/visual_search
    # params - max_number_of_results
    #          per_category_index
    #          category
    #          sort_option
    #          visual_search_categories_threshold    
    #          group_by
    #          unique_products    
    #--------------------------------------------------------------------------
    def search(self,catalog_name,image_filename,
               max_number_of_results=12,
               per_category_index=False,
               category=None,
               visual_search_categories_threshold=0.0,
               sort_option='visual_similarity',
               reweight_similarity_scores=True,
               group_by=None,
               unique_products=False,
               return_original_predictions=False):
        """ Get visually similar products in the catalog for an uploaded image.

        :params:
            - catalog_name : str
                the catalog name
            - image_filename : str
                The full path to the image.    
            - max_number_of_results : int, optional (default: 12)
                The maximum number of results to return.   
            - per_category_index : boolean, optional (default: False)
                If this is set to 'true' does visual browse only in the 
                categories specifed in the data['visual_search_category'] field. 
            - category : list of str, optional (default: None)  
                Optionally you can also specify a list of categories to search.
                For example, category=['tops','blouses']. The categories have 
                to be valid categories specified in the 
                data['visual_search_category'] field.  
            - sort_option : str, optional (default: 'visual_similarity')
                visual_similarity  : Results are sorted by visual similarity.
                apparel_similarity : Re-sorts the results from visual browse 
                                     using apparel similarity.    
            - visual_search_categories_threshold : float, optional (default: 0.0)
                Use the prdictions from the visual search categories calssifier
                only if the confidence score is greate than this value.        
            - reweight_similarity_scores : str, optional (default: 'false')
                If true multiplies the visual similarity scores by the 
                (normalized) category classifier prediction scores.      
            - group_by : list of str, optional (default: None)  
                This field can be used to group the results from visual search 
                into distinct groups according to various criteria. For example, 
                group_by=['color','pattern]. There is also a special field 
                called 'visual' which uses the total visual appearance to group
                the reuslts rather than one specific attribute, for example, 
                group_by=['visual','color'].    
            - unique_products : boolean, optional (default: False)
                By default visual browse uses all images available for a product.
                Hence, sometimes in the search results the same product id can 
                appear multiple times (with a different image_id). If this 
                parameter is set to True then the results are post-filtered 
                to contain only unique products (the best matching image_id is
                retained).     
            - return_original_predictions : boolean, optional (default: False)
                If you set this to True returns the top-5 predictions from
                the classifier before the category mapping. This is useful
                to debug the classifier and the category mappings.                                                   
        """
        
        params = {}
        params['max_number_of_results'] = max_number_of_results
        params['per_category_index'] = str(per_category_index).lower()
        params['sort_option'] = sort_option
        params['visual_search_categories_threshold'] = visual_search_categories_threshold
        params['reweight_similarity_scores'] = str(reweight_similarity_scores).lower()
        params['unique_products'] = str(unique_products).lower()
        params['return_original_predictions'] = str(return_original_predictions).lower()
        if category is not None:
            params['category'] = ','.join(category)
        if group_by is not None:
            params['group_by'] = ','.join(group_by)

        api_endpoint = '%s/catalog/%s/visual_search'%(self.version,
                                                       catalog_name)

        url = urljoin(self.api_gateway_url,api_endpoint)

        headers = dict(self.headers)
        headers['Content-Type'] = 'image/jpeg'

        response = requests.post(url,
                                 headers=headers,
                                 params=params,
                                 data=open(image_filename,'rb'))

        return response.status_code,response.json()

    #--------------------------------------------------------------------------
    # Get all visual search categories 
    # GET /v1/catalog/{catalog_name}/visual_search_categories
    #--------------------------------------------------------------------------
    def visual_search_categories(self,catalog_name):
        """ Get all visual search categories 

        :params:
            - catalog_name : str
                the catalog name
        """

        params={}

        api_endpoint = '%s/catalog/%s/visual_search_categories'%(self.version,
                                                                  catalog_name)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                headers=self.headers,
                                params=params)

        return response.status_code,response.json()

    #--------------------------------------------------------------------------
    # Get all visual browse categories 
    # GET /v1/catalog/{catalog_name}/visual_browse_categories
    #--------------------------------------------------------------------------
    def visual_browse_categories(self,catalog_name):
        """ Get all visual browse categories 

        :params:
            - catalog_name : str
                the catalog name
        """

        params={}

        api_endpoint = '%s/catalog/%s/visual_browse_categories'%(self.version,
                                                                  catalog_name)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                headers=self.headers,
                                params=params)

        return response.status_code,response.json()

    #--------------------------------------------------------------------------
    # Predict the visual search categories based on product images
    # POST /v1/catalog/{catalog_name}/predict/visual_search_categories
    # params - clear_cache
    #          ignore_non_primary_images
    #          visual_search_categories_threshold
    #--------------------------------------------------------------------------
    def categories_predict(self,catalog_name,
                           clear_cache=False,
                           ignore_non_primary_images=False,
                           visual_search_categories_threshold=0.0):
        """
        Predict the visual search categories based on product images

        :params:
            - catalog_name : str
                the catalog name
            - clear_cache : boolean, optional (default: False)
                If 'visual_search_category' is already present in the product then
                we do not change it unless clear_cache=True.
            - ignore_non_primary_images : boolean, optional (default: False)
                If true uses only the primary images (specified in the field 
                data['images'][image_id]['image_type'] = 'primary') and 
                ignores all other images.
                If False uses all the available images for the product.
                All images with data['images'][image_id]['ignore'] = 'yes' 
                are ignored.
            - visual_search_categories_threshold : float, optional (default: 0.0)
                Use the predictions from the visual search categories classifier
                only if the confidence score is greater than this value.            
        """
        params = {}
        params['ignore_non_primary_images'] = str(ignore_non_primary_images).lower()
        params['clear_cache'] = str(clear_cache).lower()
        params['visual_search_categories_threshold'] = visual_search_categories_threshold

        api_endpoint = '%s/catalog/%s/predict/visual_search_categories'%(self.version,
                                                                          catalog_name)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.post(url,
                                 headers=self.headers,
                                 params=params)

        return response.status_code,response.json()

    #----------------------------------------------------------------------
    # Get the status of the visual search categories prediction
    # GET /v1/catalog/{catalog_name}/predict/visual_search_categories
    #----------------------------------------------------------------------
    def categories_status(self,catalog_name):
        """ Get the status of the visual search categories prediction

        :params:
            - catalog_name : str
                the catalog name   
        """
        params={}

        api_endpoint = '/%s/catalog/%s/predict/visual_search_categories'%(self.version,
                                                                          catalog_name)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                headers=self.headers,
                                params=params)

        return response.status_code,response.json()

    #----------------------------------------------------------------------
    # Delete the visual search categories prediction process
    # DELETE /v1/catalog/{catalog_name}/predict/visual_search_categories
    #----------------------------------------------------------------------     
    def categories_delete(self,catalog_name):
        """ Delete the visual search categories prediction process

        :params:
            - catalog_name : str
                the catalog name   
        """
        params={}

        api_endpoint = '%s/catalog/%s/predict/visual_search_categories'%(self.version,
                                                                          catalog_name)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.delete(url,
                                headers=self.headers,
                                params=params)

        return response.status_code,response.json()       