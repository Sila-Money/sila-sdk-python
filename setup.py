from setuptools import setup, find_packages

CURRENT_VERSION = '1.1.3'

def _setup():
    setup(
        name='silasdk',

        version=CURRENT_VERSION,

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

        keywords=f'Sila v{CURRENT_VERSION} Rest API',

        packages=find_packages(exclude=["tests", "tests.*"]),

        install_requires=[
            "requests==2.32.4",
            "pyaml>=24.9.0",
            "eth-account==0.13.7",
            "web3==7.13.0",
        ],

        zip_safe=False,

        include_package_data=True,

        extras_require={},

        package_data={},

        entry_points={}
    )

if __name__ == "__main__":
    _setup()
