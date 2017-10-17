---
​---
title: MOOC RESTful API Document
revision version: 1.0
edit history:
  [1.0]  initial version  SXKDZ  11/28/2016
​---
---

# MOOC RESTful API Document

## RESTful API Specifications

### Domain

Depoly APIs under a specific domain: `https://api.mooc.tongji.edu.cn/`.

### Versioning

The API version should be considered putting into URL: `https://api.mooc.tongji.edu.cn/v1/`.

### Endpoint

Every URL represents a **resource**, thus only **nouns** are acceptable and verbs are forbidden in URL. Besides, nouns are corresponding with databases. Generally speaking, forms in databases are *collections* of homogeneous records, so nouns are in plural form.

For example, a API providing the information of all of the classes: `https://api.mooc.tongji.edu.cn/v1/classes`.

### HTTP Verbs

For the specific operation of the resources, use HTTP verbs:

- `GET` (`SELECT`): retrieve one or more information
- `POST` (`CREATE`): create or modify a new resource
- `PUT` (`UPDATE`): update resources in the server and the client should provide full resources changed
- `PATCH` (`UPDATE`): update resources in the server and the client should provide properties changed
- `DELETE` (`DELETE`): delete resources in the server

For example:

```
GET /classes 				# gets all of the classes
POST /classes 				# creates a new class
GET /classes/ID				# gets the information of a specific class
POST /classes/ID			# updates information about a specific class (provide full information about the class)
GET /classes/ID/teachers	# gets the information of teachers teaching a specific class
```

### Filtering

API should provide parameters filtering results.

The design of filtering parameters is redundant, so it is allowed that URL parameters and API path are duplicated occasionally.

For example:

```
?limit=10					# specifies the number of records to return
?offset=10					# specifies the starting position of the returned record
?homework_type_id=1			# specifies the filter criteria
```

### Status Codes

The server returns status code and prompt information to the user.

```
200 OK - [GET]
    # The server successfully returns the data requested by the user, which is idempotent.
201 CREATED - [POST/PUT/PATCH]
    # The user created or modified the data successfully.
202 Accepted - [*]
    # Indicates that a request has been queued in the background (asynchronous task).
204 No Content - [DELETE]
    # The user deleted the data successfully.
400 Invalid Request - [POST/PUT/PATCH]
    # There was an error in the request from the user. The server was not doing the operation of creating or modifying the data, and the operation was idempotent.
401 Unauthorized - [*]
    # Indicates that the user does not have permission (token, user name, password error).
403 Forbidden - [*]
    # Indicates that the user is authorized (as opposed to 401 errors), but access is prohibited.
404 Not Found - [*]
    # The user's request is for a record that does not exist. The server does not operate, and the operation is idempotent.
406 Not Acceptable - [GET]
    # User request format is not available (such as the user request JSON format, but only XML format).
410 Gone - [GET]
    # The resource requested by the user is permanently deleted and can not be retrieved.
422 Unprocesable Entity - [POST/PUT/PATCH]
    # When an object is created, a validation error occurs.
500 Internal Server Error - [*]
    # A server error occurs and the user can not determine whether the request was successful.
```

### Error Handling

If the status code is 4xx, an error message should be returned to the user. In returned information, `error` is the key name and the key value is the error message.

For example:

```
{
    error: "Invalid API key"
}
```

### Returned Results

For different operations, the results returned from the server to the user which should meet the following specifications:

```
GET /collection				# Returns a list of resource objects (array)
GET /collection/resource	# Returns a single resource object
POST /collection			# Returns the newly generated resource object
PUT /collection/resource	# Returns the complete resource object
PATCH /collection/resource	# Returns the complete resource object
DELETE /collection/resource	# Returns an empty document
```

### Hypermedia API

The RESTful API is best done with Hypermedia, which provides links to other API methods in the returned results, so that users do not need to check the API document.

The Hypermedia API is designed to be called [HATEOAS](http://en.wikipedia.org/wiki/HATEOAS). Github API meets such design. A list of all available APIs can be get by visiting https://api.github.com.

### Miscellaneous

1. API authentication should use the OAuth 2.0 framework.
2. The server returns the data in JSON format rather than XML format.

## OAuth 2.0 Specifications

### Orientations

OAuth is an [open standard](https://en.wikipedia.org/wiki/Open_standard) for [authorization](https://en.wikipedia.org/wiki/Authorization), commonly used as a way for Internet users to authorize websites or applications to access their information on other websites but without giving them the passwords.

Generally, OAuth provides to clients a "secure delegated access" to server resources on behalf of a resource owner. It specifies a process for resource owners to authorize third-party access to their server resources without sharing their credentials. Designed specifically to work with [Hypertext Transfer Protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) (HTTP), OAuth essentially allows [access tokens](https://en.wikipedia.org/wiki/Access_token) to be issued to third-party clients by an authorization server, with the approval of the resource owner. The third party then uses the access token to access the protected resources hosted by the resource server.

### Definitions

1. Third-party application: a.k.a, client
2. HTTP service: the HTTP service provider
3. Resource owner: a.k.a, user
4. User agent: web browsers
5. Authorization server: a server of the service provider designed to handle authentication
6. Resource server: a server where a service provider stores user-generated resources

### Operation Flow

![](http://image.beekka.com/blog/2014/bg2014051203.png)

(A) After the user opens the client, the client requests authorization from the user.

(B) The user agrees to grant the client authority.

(C) The client uses the authorization obtained in the previous step to apply for a token to the authentication server.

(D) After the authentication server authenticates the client, it confirms the correctness and agrees to issue the token.

(E) The client requests a resource from the resource server using a token.

(F) The resource server confirms the token and agrees to open resources to the client.

It is not difficult to discover that among the above six steps, step (B), that how the user can agree to give the client authorization, is the key. With this authorization, the client can obtain tokens, and then obtain resources by token.

### Authorization Modes

After the authorization granted, the client are able to access token. OAuth 2.0 defines the following four kinds of authorization modes:

- authorization code
- implicit
- resource owner password credentials
- client credentials

#### Authorization Code Type

The authorization code is the authorization mode with complete features and most stringent process. It is characterized by interaction of the authorization server of the "services provider" with the back-end server via the client.

![](http://image.beekka.com/blog/2014/bg2014051204.png)

(A) The user accesses the client and the client redirects user to the authorization server.

(B) The user selects whether to authorize the client.

(C) Assuming that the user gives authorization, the authorization server redirects the user to the "redirection URI", specified by the client in advance, and attaches an authorization code.

(D) The client receives the authorization code and request a token from the authorization server with the attachment of the previous "redirection URI". This step is invisible to the user and is done in the background of the client server.

(E) The authorization server checks the authorization code and redirection URI, and sends an access token and a refresh token to the client, after confirming the correctness.

#### Implicit Grant Type

Implicit grant type requests the authentication server for a token directly in the browser, without going through the third-party application server. It skips the "authorization code" step, hence the name. All steps are done in the browser, the token is visible to the visitor, and the client does not need authentication.

![](http://image.beekka.com/blog/2014/bg2014051205.png)

(A) The client directs the user to the authentication server.

(B) The user decides whether to authorize the client.

(C) Assuming that the user gives permission, the authorization server redirects the user to the "redirection URI" with access token in Hash part.

(D) The browser sends requests to the resource server, excluding Hash value received in step (C).

(E) The resource server returns a web page, containing the code retrieving token in Hash value.

(F) The browser executes the script abtained in step (E).

(G) The browser sends token to the client.

### Updating Token

If the "access token" of the client has expired when the user accesses it, it needs to use the "update token" to request a new access token.

## MOOC API Document

