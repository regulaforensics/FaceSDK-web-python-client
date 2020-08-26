# regula.face.webclient.gen
Regula Face Recognition Web API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import regula.face.webclient.gen
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import regula.face.webclient.gen
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import regula.face.webclient.gen
from regula.face.webclient.gen.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = regula.face.webclient.gen.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with regula.face.webclient.gen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = regula.face.webclient.gen.GroupApi(api_client)
    group_to_create = regula.face.webclient.gen.GroupToCreate() # GroupToCreate | 

    try:
        # Create group
        api_instance.create_group(group_to_create)
    except ApiException as e:
        print("Exception when calling GroupApi->create_group: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GroupApi* | [**create_group**](docs/GroupApi.md#create_group) | **POST** /groups | Create group
*GroupApi* | [**get_all_groups**](docs/GroupApi.md#get_all_groups) | **GET** /groups | Get groups
*GroupApi* | [**update_group**](docs/GroupApi.md#update_group) | **PUT** /groups/{group_id} | Update group
*MatchingApi* | [**compare**](docs/MatchingApi.md#compare) | **POST** /compare | Compare given persons among themselves and return similarity score for each pair.


## Documentation For Models

 - [CompareRequest](docs/CompareRequest.md)
 - [CompareRequestFields](docs/CompareRequestFields.md)
 - [CompareResponse](docs/CompareResponse.md)
 - [CompareResponseFields](docs/CompareResponseFields.md)
 - [Group](docs/Group.md)
 - [GroupFields](docs/GroupFields.md)
 - [GroupFieldsAllOf](docs/GroupFieldsAllOf.md)
 - [GroupPage](docs/GroupPage.md)
 - [GroupPageAllOf](docs/GroupPageAllOf.md)
 - [GroupPatch](docs/GroupPatch.md)
 - [GroupToCreate](docs/GroupToCreate.md)
 - [GroupToCreateFields](docs/GroupToCreateFields.md)
 - [ImageSource](docs/ImageSource.md)
 - [OperationLog](docs/OperationLog.md)
 - [PageFields](docs/PageFields.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




