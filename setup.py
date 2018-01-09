from setuptools import setup

setup(name='eeconvert',
      version='0.1.16',
      description='',
      url='http://github.com/rutgerhofste/eeconvert',
      author='Rutger Hofste',
      author_email='rutgerhofste@gmail.com',
      license='MIT',
      packages=['eeconvert'],
      install_requires=['boto3','botocore','sqlalchemy','earthengine-api','shapely','folium','geojson','branca','pandas'],
      zip_safe=False)
