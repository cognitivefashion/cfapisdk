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

""" Catalog APIs.
https://cognitivefashion.github.io/slate/#catalog
"""

__author__      = "Vikas Raykar"
__email__       = "viraykar@in.ibm.com"
__copyright__   = "IBM India Pvt. Ltd."

__all__ = ["Catalog"]

import os
import json
import requests
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

class Catalog():
    """ Catalog APIs.
    """
    def __init__(self,
                 api_gateway_url,
                 api_key,
                 version='v1',
                 data_collection_opt_out=False):
        """ Initialization.

        :params:
            - api_gateway_url : str
                The api gateway url.
            - api_key : str    
                The api key.    
            - version : str, optional (default: 'v1')
                The api version.    
            - data_collection_opt_out : boolean, optional (default: False)
                https://cognitivefashion.github.io/slate/#data-collection
        """

        self.api_gateway_url = api_gateway_url
        self.version = version
        self.api_key = api_key

        self.headers = {}
        self.headers['X-Api-Key'] = self.api_key
        self.headers['X-Data-Collection-Opt-Out'] = str(data_collection_opt_out).lower()

    #--------------------------------------------------------------------------
    # Get a random fashion quote.  
    # GET /v1/fashion_quote
    #--------------------------------------------------------------------------
    def fashion_quote(self):
        """ Get a random fashion quote. 
        https://cognitivefashion.github.io/slate/#fashion-quote

        :returns:
            - status_code : int
                the status code of the response
            - response : json
                the response     
        """
        params = {}

        api_endpoint = '%s/fashion_quote'%(self.version)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                headers=self.headers,
                                params=params)        

        return response.status_code,response.json()

    #--------------------------------------------------------------------------
    # Add metadata to a catalog.    
    # POST /v1/catalog/{catalog_name}
    #--------------------------------------------------------------------------
    def add_metadata(self,catalog_name,data):
        """ Add product to a catalog. 
        
        :params:
            - catalog_name : str
                the catalog name 
            - metadata : dict
                Any metadata you want to track for the catalog. Suggested fields
                data={}
                data['friendly_name'] - A friendly name for display purposes.
                data['hero_image_url'] - The url of the hero image.
                data['description'] - A brief description.
                etc.
        """    
        
        params={}

        api_endpoint = '%s/catalog/%s'%(self.version,
                                        catalog_name)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.post(url,
                                 headers=self.headers,
                                 params=params,
                                 json=data)

        return response.status_code,response.json()

    #--------------------------------------------------------------------------
    # Get all catalog names. 
    # GET /v1/catalog_names
    #--------------------------------------------------------------------------
    def names(self):
        """ Get all catalog names. 
        """
        params = {}

        api_endpoint = '%s/catalog_names'%(self.version)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                headers=self.headers,
                                params=params)        

        return response.status_code,response.json()            

    #--------------------------------------------------------------------------
    # Get info about a product catalog.  
    # GET /v1/catalog/{catalog_name}
    #--------------------------------------------------------------------------
    def info(self,catalog_name):
        """ Get info about a product catalog.  

        :params:
            - catalog_name : str
                the catalog name       
        """
        
        params={}
 
        api_endpoint = '%s/catalog/%s'%(self.version,
                                         catalog_name)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                 headers=self.headers,
                                 params=params)

        return response.status_code,response.json()
    
    #--------------------------------------------------------------------------
    # Delete a product catalog.
    # DELETE /v1/catalog/{catalog_name}
    # params - delete_images
    #--------------------------------------------------------------------------
    def delete(self,catalog_name,
               delete_images=True):
        """ Delete a product catalog.

        :params:
            - catalog_name : str
                the catalog name       
            - delete_images : str, optional(default: 'true')
                By default deletes all the catalog images unless this is set to
                false.                    
        """
        
        params={}
        params['delete_images'] = str(delete_images).lower()
 
        api_endpoint = '%s/catalog/%s'%(self.version,
                                         catalog_name)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.delete(url,
                                 headers=self.headers,
                                 params=params)

        return response.status_code,response.json()

    #--------------------------------------------------------------------------
    # Basic text search
    # GET /v1/catalog/{catalog_name}/text_search
    # params : query_text, max_number_of_results
    #--------------------------------------------------------------------------
    def text_search(self,catalog_name,query_text,
                    max_number_of_results=12):
        """ Basic text search.
        
        :params:
            - catalog_name : str
                the catalog name
            - query_text : string
                the search query
            - max_number_of_results : int
                maximum number of results to return
                (defaults to 12)                    
        """    
        
        params={}
        params['query_text'] = query_text
        params['max_number_of_results'] = max_number_of_results

        api_endpoint = '%s/catalog/%s/text_search'%(self.version,
                                                    catalog_name)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                headers=self.headers,
                                params=params)

        return response.status_code,response.json()  

    #--------------------------------------------------------------------------
    # Add product to a catalog.    
    # POST /v1/catalog/{catalog_name}/products/{id}
    # params - download_images
    #--------------------------------------------------------------------------
    def add_product(self,catalog_name,id,data,
                    download_images=True):
        """ Add product to a catalog. 
        
        :params:
            - catalog_name : str
                the catalog name
            - id : str
                the product id    
            - data : dict
                the product data
            - download_images : boolean, optional(default: True)
                By default all the images specified in the json will be 
                downloaded. Set this to false if you do not want to 
                download the images.
        """    
        
        params={}
        params['download_images'] = str(download_images).lower()
 
        api_endpoint = '%s/catalog/%s/products/%s'%(self.version,
                                                     catalog_name,
                                                     id)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.post(url,
                                 headers=self.headers,
                                 json=data,
                                 params=params)

        return response.status_code,response.json()

    #--------------------------------------------------------------------------
    # Update product in a catalog.  
    # PUT  /v1/catalog/{catalog_name}/products/{id}
    # params - download_images
    #--------------------------------------------------------------------------
    def update_product(self,catalog_name,id,data,
                       download_images=True):
        """ Update product in a catalog.  
        
        :params:
            - catalog_name : str
                the catalog name
            - id : str
                the product id    
            - data : dict
                the product data
            - download_images : boolean, optional(default: True)
                By default all the images specified in the json will be 
                downloaded. Set this to false if you do not want to 
                download the images.                
        """    
        
        params={}
        params['download_images'] = str(download_images).lower()
 
        api_endpoint = '%s/catalog/%s/products/%s'%(self.version,
                                                    catalog_name,
                                                    id)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.put(url,
                                headers=self.headers,
                                json=data,
                                params=params)

        return response.status_code,response.json()    

    #--------------------------------------------------------------------------
    # Get product from a catalog.  
    # GET /v1/catalog/{catalog_name}/products/{id}
    #--------------------------------------------------------------------------
    def get_product(self,catalog_name,id):
        """ Get product from a catalog. 
        
        :params:
            - catalog_name : str
                the catalog name
            - id : str
                the product id    
        """    
        
        params={}

 
        api_endpoint = '%s/catalog/%s/products/%s'%(self.version,
                                                     catalog_name,
                                                     id)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                headers=self.headers,
                                params=params)

        return response.status_code,response.json()   

    #--------------------------------------------------------------------------
    # Delete product from a catalog.
    # DELETE /v1/catalog/{catalog_name}/products/{id}
    # params - delete_images
    #--------------------------------------------------------------------------
    def delete_product(self,catalog_name,id,
                       delete_images=False):
        """ Get product from a catalog. 
        
        :params:
            - catalog_name : str
                the catalog name
            - id : str
                the product id    
            - delete_images : str, optional (default: False) 
                Set this to True if you want to delete the images. 
        """    
        
        params={}
        params['delete_images'] = str(delete_images).lower()
 
        api_endpoint = '%s/catalog/%s/products/%s'%(self.version,
                                                     catalog_name,
                                                     id)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.delete(url,
                                   headers=self.headers,
                                   params=params)

        return response.status_code,response.json()   

    #--------------------------------------------------------------------------
    # Get an image in the catalog.
    # GET /v1/catalog/{catalog_name}/images/{image_name}
    # params : top_left_x,top_left_y,width,height
    #--------------------------------------------------------------------------
    def image_url(self,catalog_name,id,
                  image_id=None,
                  return_product_info=False,
                  top_left_x=None,
                  top_left_y=None,
                  width=None,
                  height=None):
        """ Get an image in the catalog.

        :params:
            - catalog_name : str
                the catalog name
            - id : str
                the product id  
            - image_id : str, optional (default: None)
                the image id    
                (If not specified returns the url of the first image)
            - return_product_info : boolean, optional (default: False) 
                If True also returns inte product info in the response.   
            [Optionally, you can pass these parameters to get a crop]
            - top_left_x : int 
                The x co-ordinate of the top left corner of the bounding box.
            - top_left_y : int 
                The y co-ordinate of the top left corner of the bounding box.
            - width : int
                The width of the bounding box.
            - height: int 
                The height of the bounding box.                            
        """

        status,response_product = self.get_product(catalog_name=catalog_name,
                                                   id=id)

        if status == 202: 
            if image_id is None:
                image_ids = list(response_product['data']['images'].keys())
                image_id  = image_ids[0]

            image_url = response_product['data']['images'][image_id]['image_url']
            image_filename = response_product['data']['images'][image_id]['image_filename']
            
            image_location = '%s/catalog/%s/images/%s'%(self.version,
                                                        catalog_name,
                                                        image_filename)

            if top_left_x is None: 
                image_url_local = '%s?api_key=%s'%(urljoin(self.api_gateway_url,image_location),
                                                   self.api_key)
            else:
                image_url_local = '%s?api_key=%s&top_left_x=%d&top_left_y=%d&width=%d&height=%d'%(
                                                urljoin(self.api_gateway_url,image_location),
                                                self.api_key,
                                                top_left_x,
                                                top_left_y,
                                                width,
                                                height)

            response = {}
            response['id'] = id
            response['image_id'] = image_id
            response['image_url'] = image_url
            response['image_filename'] = image_filename
            response['image_url_local'] = image_url_local
            if return_product_info:
                response['product_info'] = response_product['data'] 

            return status,response
        else:
            return status,response_product