# eeConvert

Easy to use functions to convert google earth engine data types such as featureCollections into other GIS formats such as geopandas GeoDataframes or Folium map layers. These functions are client side so don't use them on large featureCollections or images. This package is mainly tailored to test subsets of your results and visualize them in a dataframe or folium map.

Supported formats:

1. pandas
1. geopandas
1. folium 
1. postGreSQL
1. postGIS (enabled postGreSQL)

use at your own risk.  

Documentation is currently limited to the comments of the different functions in the eeconvert/eeconvert/__init__.py file. 

[Link to read the Docs](http://eeconvert.readthedocs.io/en/latest/index.html)


## Installation:  

### Step 1:  

One of the packages' dependencies is pyproj which requires a compiler to be installed. 

#### Linux 

`apt-get install gcc`

#### MacOS

Using brew:  
`brew install llvm`


#### Windows

Install MicroSoft Visual


### Step 2:  

`pip install eeconvert`


## Todo: 
1. allow to install using `conda install eeconvert` 
1. Develop testing scripts
1. create a read the docs
1. improve functionality


[![Build Status](https://travis-ci.org/rutgerhofste/eeconvert.svg?branch=master)](https://travis-ci.org/rutgerhofste/eeconvert)
