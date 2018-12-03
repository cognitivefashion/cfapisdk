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

""" Complete The Look APIs.
https://cognitivefashion.github.io/slate/#complete-the-look
"""

__author__      = "Ayushi Dalmia"
__email__       = "adalmi08@in.ibm.com"
__copyright__   = "IBM India Pvt. Ltd."

__all__ = ["CompleteTheLook"]

import os
import json
import requests
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

class CompleteTheLook():
    """ CompleteTheLook APIs.
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

    #--------------------------------------------------------------------------
    # Get a style tip and set of recommended items for the text query.  
    # GET /v1/complete_the_look/text/
    # params: 
    #--------------------------------------------------------------------------
    def get_recommendation(self,
                           query_text,
			   gender,
                           query_text)
                           
        api_endpoint = 'v1/complete_the_look/text/'
        url = urljoin(self.api_gateway_url,api_endpoint)

        params = {}
        params['query_text'] = query_text
        params['gender'] = gender

        response = requests.get(url,headers=headers,params=params)
        return response.status_code, response.json()
