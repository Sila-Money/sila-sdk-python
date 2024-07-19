from setuptools import setup, find_packages

setup(
    name='silasdk',

    version='1.1.0',

    description='Sila Python library for message signing and api wrapper',

    url="https://github.com/Sila-Money/Sila-Python",

    author='Sila',
    author_email='support@silamoney.com',

    license='Apache',

    classifiers=[

        # How stable is your project?
        #   3 - Alpha, 4 - Beta,5 - Production/Stable

        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.9'

    ],

    keywords='Sila v1.1.0 Rest API',

    packages=find_packages(exclude=["tests", "tests.*"]),

    install_requires=[
        "requests==2.32.2",
        "pyaml>=15.8.2",
        "eth-account==0.8.0",
        "web3==6.5.0"
    ],

    zip_safe=False,

    include_package_data=True,

    extras_require={},

    package_data={},

    entry_points={}
)
