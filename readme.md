# REST API
----
https://realpython.com/api-integration-in-python/
---
REST (Representational State Transfer) is an architectural style for designing networked applications. It's commonly used in the development of web services such as APIs (Application Programming Interfaces). RESTful APIs adhere to a set of principles that emphasize a stateless client-server relationship, a uniform interface, and resource-based interactions.

![Sample](https://github.com/RAJGUPTA28/Python-REST_APIs/blob/main/what_is_rest_api.png)
---- 
# The key principles of REST include:

- **Client-Server Architecture**: The client and server are separate and independent, allowing them to evolve independently.
- **Statelessness**: Each request from a client to the server must contain all the necessary information for the server to fulfill the request. The server doesn't store any client state between requests.
- **Uniform Interface**: This principle is further broken down into several constraints, including:
- **Resource identification**: Resources (such as data entities) are uniquely identified using URIs (Uniform Resource Identifiers).
- **Resource manipulation through representations**: Resources can have multiple representations (like JSON, XML, HTML), and clients interact with these representations rather than directly with the resources.
- **Self-descriptive messages**: Each message sent from the server to the client contains enough information for the client to understand how to process it.
Hypermedia as the engine of application state (HATEOAS): Resources contain hyperlinks to related resources, allowing the client to discover and navigate the API dynamically.
- **Cacheability**: Responses from the server can be labeled as cacheable or non-cacheable to improve performance.
- **Layered System**: A client may not be aware of whether it's directly connected to the server or to an intermediary, like a load balancer or proxy server. This separation improves scalability and security.

-----
# USAGE
RESTful APIs are widely used due to their simplicity, scalability, and compatibility with the HTTP protocol, making them suitable for a variety of applications and devices.
Developers interact with REST APIs by sending HTTP requests (such as GET, POST, PUT, DELETE) to specific endpoints (URLs) that represent resources, and the server responds with the requested data or performs the specified actions.


# METHODS

- **GET**: Requests data from a specified resource. It should only retrieve data and should not modify anything on the server.
- **POST**: Submits data to be processed to a specified resource. It's often used for creating new resources or sending data that will result in some kind of processing on the server.
- **PUT**: Updates a specified resource with the request payload. It replaces the entire resource if it exists or creates it if it doesn't.
- **PATCH**: Applies partial modifications to a resource. It's similar to PUT but is used to apply partial updates rather than replacing the entire resource.
- **DELETE**: Deletes the specified resource.
- **OPTIONS**: Requests information about the communication options available for the target resource. It's often used to inquire about the supported methods on a resource.
- **HEAD**: Requests the headers that would be returned if the HEAD request's URL were instead requested using a GET method. It's useful for checking resources' metadata without retrieving the entire content.

![IMG](https://github.com/RAJGUPTA28/Python-REST_APIs/blob/main/rest-api.png)
![IMG](https://github.com/RAJGUPTA28/Python-REST_APIs/blob/main/rest2.webp)
# STATUS CODES
Status code	Description
|200 | OK	Your request was successful! |
|201 | Created	Your request was accepted, and the resource was created. |
|400 | Bad Request	Your request is either wrong or missing some information. |
|401 | Unauthorized	Your request requires some additional permissions. |
|404  |Not Found	The requested resource doesn’t exist.|
|405| Method Not Allowed	The endpoint doesn’t allow for that specific HTTP method. |
|500 |Internal Server Error	Your request wasn’t expected and probably broke something on the server side.|

 # INSTALLATION
```bash
$ python -m pip install requests
```


# Rest API Response Codes
---

**1) 100 Series**
 (These are temporary Responses)

- 100 Continue
- 101 Switching Protocols
- 102 Processing
