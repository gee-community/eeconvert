from setuptools import setup

setup(name='eeconvert',
      version='0.1.3',
      description='earth engine conversion for jupyter notebook use',
      url='http://github.com/rutgerhofste/eeconvert',
      author='Rutger Hofste',
      author_email='rutgerhofste@gmail.com',
      license='MIT',
      packages=['eeconvert'],
      install_requires=[boto3,botocore],
      zip_safe=False)