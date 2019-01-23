
from setuptools import setup, find_packages

from codecs import open
from os import path



setup(
    name='sila_api_wrapper',


    version='1.0',

    description='Sila Python library for message signing and api wrapper',

    url='https://github.com/Sila-Money/Sila-Python',

    author='Sila',
    author_email='support@silamoney.com',

    license='MIT',

    classifiers=[
        
        # How stable is your project? 
        #   3 - Alpha, 4 - Beta,5 - Production/Stable

        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6'

    ],

    keywords='Sila v1.0 Rest API',

    packages=["sila_api"],

   
    install_requires=['requests'],

    zap_safe=False,
    
    include_package_data=True,

    extras_require={},

   
    package_data={},

  
    entry_points={}
)