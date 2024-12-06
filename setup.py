from setuptools import setup, find_packages

setup(
    name='silasdk',

    version='1.1.2',

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

    keywords='Sila v1.1.2 Rest API',

    packages=find_packages(exclude=["tests", "tests.*"]),

    install_requires=[
        "requests==2.32.3",
        "pyaml>=24.9.0",
        "eth-account==0.13.4",
        "setuptools>=75.6.0",
        "web3==7.6.0"
    ],

    zip_safe=False,

    include_package_data=True,

    extras_require={},

    package_data={},

    entry_points={}
)
