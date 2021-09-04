# Sila SDK for Python

## Using the SDK
### Installation and use
A guide to the installation and configuration of this SDK can be found here: [https://docs.silamoney.com/docs/python-sdk](https://docs.silamoney.com/docs/python-sdk)

### Endpoint Methods
Example code for each SDK endpoint method is found in the associated endpoint's section in our docs, which can be found here: [https://docs.silamoney.com/docs/get-started](https://docs.silamoney.com/docs/get-started)

### Debug Logging

If you'd like to set additional debug logging, then make sure to set the logging level when you run your code:

```python
import logging

logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)
```