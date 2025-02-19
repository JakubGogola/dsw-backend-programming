# openapi_client.DefaultApi

All URIs are relative to *https://api.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order**](DefaultApi.md#create_order) | **POST** /orders | Tworzy nowe zamówienie
[**create_user**](DefaultApi.md#create_user) | **POST** /users | Tworzy nowego użytkownika
[**delete_user**](DefaultApi.md#delete_user) | **DELETE** /users/{id} | Usuwa użytkownika
[**get_user**](DefaultApi.md#get_user) | **GET** /users/{id} | Pobiera szczegóły użytkownika
[**get_user_orders**](DefaultApi.md#get_user_orders) | **GET** /users/{id}/orders | Pobiera zamówienia użytkownika
[**get_users**](DefaultApi.md#get_users) | **GET** /users | Pobiera listę użytkowników


# **create_order**
> Order create_order(order_create)

Tworzy nowe zamówienie

### Example


```python
import openapi_client
from openapi_client.models.order import Order
from openapi_client.models.order_create import OrderCreate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.example.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    order_create = openapi_client.OrderCreate() # OrderCreate | 

    try:
        # Tworzy nowe zamówienie
        api_response = api_instance.create_order(order_create)
        print("The response of DefaultApi->create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_create** | [**OrderCreate**](OrderCreate.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Zamówienie zostało utworzone |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(user_create)

Tworzy nowego użytkownika

### Example


```python
import openapi_client
from openapi_client.models.user import User
from openapi_client.models.user_create import UserCreate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.example.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    user_create = openapi_client.UserCreate() # UserCreate | 

    try:
        # Tworzy nowego użytkownika
        api_response = api_instance.create_user(user_create)
        print("The response of DefaultApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Użytkownik został utworzony |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(id)

Usuwa użytkownika

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.example.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 56 # int | 

    try:
        # Usuwa użytkownika
        api_instance.delete_user(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Użytkownik został usunięty |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(id)

Pobiera szczegóły użytkownika

### Example


```python
import openapi_client
from openapi_client.models.user import User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.example.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 56 # int | 

    try:
        # Pobiera szczegóły użytkownika
        api_response = api_instance.get_user(id)
        print("The response of DefaultApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Szczegóły użytkownika |  -  |
**404** | Użytkownik nie znaleziony |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_orders**
> List[Order] get_user_orders(id)

Pobiera zamówienia użytkownika

### Example


```python
import openapi_client
from openapi_client.models.order import Order
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.example.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 56 # int | 

    try:
        # Pobiera zamówienia użytkownika
        api_response = api_instance.get_user_orders(id)
        print("The response of DefaultApi->get_user_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List[Order]**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lista zamówień użytkownika |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> List[User] get_users()

Pobiera listę użytkowników

### Example


```python
import openapi_client
from openapi_client.models.user import User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.example.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Pobiera listę użytkowników
        api_response = api_instance.get_users()
        print("The response of DefaultApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lista użytkowników |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

