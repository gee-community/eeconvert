# eeconvert

the objective of eeconvert is to have easy to use functions to convert google earth engine data types such as featureCollections into other GIS formats such as geopandas GeoDataframes or Folium map layers. These functions are client side so mostly useful for testing of specific areas or geometries. 

This repo is mainly for personal use so use at your own risk.  

Documentation is currently limited to the comments of the different functions in the eeconvert/eeconvert/__init__.py file. 



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
