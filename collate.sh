# For ease of maintainence the python sdk for each api/microservice
# are kept in the correspoding repo for the microservice.
# Run this script to copy all the required files to this folder.

cp -a /cognitive_fashion/code/cfapicatalog/sdk/Catalog.py .
cp -a /cognitive_fashion/code/cfapicatalog/sdk/gist_Catalog.py gists

cp -a /cognitive_fashion/code/cfapivisualsearch/sdk/VisualSearch.py .
cp -a /cognitive_fashion/code/cfapivisualsearch/sdk/gist_VisualSearch.py gists