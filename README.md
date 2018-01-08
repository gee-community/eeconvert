# eeconvert

the objective of eeconvert is to have easy to use functions to convert google earth engine data types such as featureCollections into other GIS formats such as geopandas GeoDataframes or Folium map layers. These functions are client side so mostly useful for testing of specific areas or geometries. 

This repo is mainly for personal use so use at your own risk. +

Documentation is currently limited to the comments of the different functions in the eeconvert/eeconvert/__init__.py file. 



Installation:

`pip install eeconvert`


Todo: 
allow to install using `conda install eeconvert` 

Caveat with pip install:
- The functions with geopandas require pyproj which is a non pure pythonic package and needs to be compiled. To avoid this complexity you will have to install geopandas (incl. pyproj) separately. 


[![Build Status](https://travis-ci.org/rutgerhofste/eeconvert.svg?branch=master)](https://travis-ci.org/rutgerhofste/eeconvert)
