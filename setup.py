import os
import re

from setuptools import setup, find_packages

# get version string from version.py
version_file = os.path.join(os.path.dirname(__file__), "silasdk/version.py")
version_regex = r"__version__ = ['\"]([^'\"]*)['\"]"
with open(version_file, encoding="utf-8") as f:
    version = re.search(version_regex, f.read(), re.M).group(1)

setup(
    name='silasdk',

    version=version,

    description='Sila Python library for message signing and api wrapper',

    url="https://github.com/Sila-Money/Sila-Python",

    author='Sila',
    author_email='support@silamoney.com',

    license='Apache',

    classifiers=[

        # How stable is your project?
        #   3 - Alpha, 4 - Beta,5 - Production/Stable

        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.12'

    ],

    keywords=f'Sila v{version} Rest API',

    packages=find_packages(exclude=["tests", "tests.*"]),

    install_requires=[
        "requests==2.32.4",
        "pyaml>=24.9.0",
        "eth-account==0.13.7",
        "setuptools>=75.6.0",
        "web3==7.13.0",
    ],

    zip_safe=False,

    include_package_data=True,

    extras_require={},

    package_data={},

    entry_points={}
)
