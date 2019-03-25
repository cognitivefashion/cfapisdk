""" Natural Language Search APIs.
https://cognitivefashion.github.io/slate/#natural-language-search
"""

__author__      = "Vikas Raykar"
__email__       = "viraykar@in.ibm.com"
__copyright__   = "IBM India Pvt. Ltd."

__all__ = ["NaturalLanguageSearch"]

import os
import json
import requests

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

class NaturalLanguageSearch():
    """ Natural Language Search APIs.
    """
    def __init__(self,
                 api_gateway_url,
                 api_key,
                 version='v1',
                 data_collection_opt_out=False):
        """ Initialization.

        Parameters
        ----------
        api_gateway_url : str
            The api gateway url.
        api_key : str    
            The api key.    
        version : str, optional (default: 'v1')
            The api version.    
        data_collection_opt_out : boolean, optional (default: False)
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

        Returns
        -------
        status_code : int
            the status code of the response
        response : json
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
    # Natural Language Semantic Search
    # GET /v1/catalog/{catalog_name}/natural_language_search
    # params : (required) query_text
    #          max_number_of_results
    #          max_number_of_backoffs
    #          return_elasticsearch_queries
    #--------------------------------------------------------------------------
    def natural_language_search(self,catalog_name,query_text,
                                max_number_of_results=12,
                                max_number_of_backoffs=5,
                                return_elasticsearch_queries=False):
        """ Natural Language Semantic Search
        https://cognitivefashion.github.io/slate/#natural-language-search28

        Parameters
        ----------
        catalog_name : str
            the catalog name
        query_text : string
            the natural language search query
            (e.g. show me some abof red graphic print tees under 1k.)
        max_number_of_results : int, optional(default:12)
            maximum number of results to return
        max_number_of_backoffs : int, optional(default:5)
            maximum number of backoffs
            Set to 0 if you want only one query.   
        return_elasticsearch_queries : str, optional(default:false)  
            If true returns the corresponding elasticsearch queries 
            (ordered from specific to general) in the query DSL format.

        Returns
        -------
        status_code : int
            the status code of the response
        response : json
            the response                 

        """    
        
        params={}
        params['query_text'] = query_text
        params['max_number_of_results'] = max_number_of_results
        params['max_number_of_backoffs'] = max_number_of_backoffs
        params['return_elasticsearch_queries'] = str(return_elasticsearch_queries).lower()

        api_endpoint = '%s/catalog/%s/natural_language_search'%(self.version,
                                                                catalog_name)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                headers=self.headers,
                                params=params)

        return response.status_code,response.json()  

    #--------------------------------------------------------------------------
    # Natural Language Semantic Search Elasticsearch Queries
    # GET /v1/natural_language_search/elasticsearch_queries
    # params : (required) query_text
    #          max_number_of_results
    #          max_number_of_backoffs
    #--------------------------------------------------------------------------
    def elasticsearch_queries(self,query_text,
                              max_number_of_results=12,
                              max_number_of_backoffs=5):
        """ Get elasticsearch queries.

        https://cognitivefashion.github.io/slate/#get-elasticsearch-queries

        Parameters
        ----------
        query_text : string
            the natural language search query
            (e.g. show me some abof red graphic print tees under 1k.)
        max_number_of_results : int, optional(default:12)
            maximum number of results to return
        max_number_of_backoffs : int, optional(default:5)
            maximum number of backoffs
            Set to 0 if you want only one query.   

        Returns
        -------
        status_code : int
            the status code of the response
        response : json
            the response                 

        """    
        
        params={}
        params['query_text'] = query_text
        params['max_number_of_results'] = max_number_of_results
        params['max_number_of_backoffs'] = max_number_of_backoffs

        api_endpoint = '%s/natural_language_search/elasticsearch_queries'%(self.version)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                headers=self.headers,
                                params=params)

        return response.status_code,response.json()  

    #--------------------------------------------------------------------------
    # Parse fashion text.
    # GET /v1/natural_language_search/parse
    # params : (required) query_text
    #          include_apparel_hyponyms 
    #          include_apparel_hypernyms
    #          return_search_terms  
    #--------------------------------------------------------------------------
    def parse(self,query_text,
              include_apparel_hyponyms=False,
              include_apparel_hypernyms=False,
              return_search_terms=False):
        """ Parse fashion text.

        https://cognitivefashion.github.io/slate/#parse-fashion-query-text

        Parameters
        ----------
        query_text : string
            the natural language search query
            (e.g. show me some abof red graphic print tees under 1k.)

        Returns
        -------
        status_code : int
            the status code of the response
        response : json
            the response                 

        """    
        
        params={}
        params['query_text'] = query_text
        params['include_apparel_hyponyms'] = str(include_apparel_hyponyms).lower()
        params['include_apparel_hypernyms'] = str(include_apparel_hypernyms).lower()
        params['return_search_terms'] = str(return_search_terms).lower()

        api_endpoint = '%s/natural_language_search/parse'%(self.version)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                headers=self.headers,
                                params=params)

        return response.status_code,response.json()         

    #--------------------------------------------------------------------------
    # Spelling Correction.
    # GET /v1/natural_language_search/spell_correct
    # params : (required) query_text
    #--------------------------------------------------------------------------
    def spell_correct(self,query_text):
        """ Parse fashion text.

        https://cognitivefashion.github.io/slate/#spelling-correction

        Parameters
        ----------
        query_text : string
            the natural language search query
            (e.g. show me some abof red graphic print tees under 1k.)

        Returns
        -------
        status_code : int
            the status code of the response
        response : json
            the response                 

        """    
        
        params={}
        params['query_text'] = query_text

        api_endpoint = '%s/natural_language_search/spell_correct'%(self.version)

        url = urljoin(self.api_gateway_url,api_endpoint)

        response = requests.get(url,
                                headers=self.headers,
                                params=params)

        return response.status_code,response.json()         
