# Devblops blog microservice

[![Build Status](http://52.91.9.136:8080/buildStatus/icon?job=BlogMicroservice)](http://52.91.9.136:8080/job/BlogMicroservice/)

## Issue Tracker
 - Token should be in header (API Gateway)
 - Comments should have date/time (Backend)

## Blog Frontend   
     
### Action: 
 * `C` for create blog
 * `R` for retrieve all blogs
 * `D` for delete a blog
 * `Q` for adding a comment in a blog

### Request methods and templates 
 - Request Body
```
{
    "Token": str <REQUIRED>,
    "Action": str <REQUIRED>,
    "BlogSubject": str / null if action = R ,
    "BlogBody": str / null if action = R, D, Q ,
    "Location": str / null if action = R, D, Q ,
    "Date": str / null if action = R, D, Q ,
    "Time": str / null if action = R, D, Q,
    "Comment": str / null if action = C, R, U, D
}
```
 - Response Body
 ```
{
    "statusCode": 200,
    "Status": boolean,
    "BlogSubject": str / null,
    "Error": str / null,
    "Description": str,
    "BlogDB": Array of dicts / null
}
```

### Route
POST to `https://0c77865x10.execute-api.us-east-1.amazonaws.com/v1/blog`
 
### Examples
 - Create blog
 ```
Request body:
{
  "Token": <Token>,
  "Action": "C",
  "BlogSubject": "First Blog",
  "BlogBody": "Hello world",
  "Location": <Location>,
  "Date": <Date>,
  "Time": <Time>,
  "Comment": null
}

Response body:
{
  "statusCode": 200,
  "Status": <boolean>,
  "BlogSubject": <Title of the blog you just created>,
  "Error": str / null,
  "Description": str
}
```

 - Delete blog:
```
Request body:
{
  "Token": <Token>,
  "Action": "D",
  "BlogSubject": "First Blog",
  "BlogBody": null,
  "Location": null,
  "Date": null,
  "Time": null,
  "Comment": null
}

Response body:
{
  "statusCode": 200,
  "Status": <boolean>,
  "BlogSubject": null,
  "Error": str / null,
  "Description": str,
  "BlogsDB": null
}
```

 - Add comment to a blog:
```
Request body:
{
  "Token": <Token>,
  "Action": "Q",
  "BlogSubject": "First Blog",
  "BlogBody": null,
  "Location": null,
  "Date": null,
  "Time": null,
  "Comment": "Hello this is my first comment"
}

Response body:
{
  "statusCode": 200,
  "Status": <boolean>,
  "BlogSubject": null,
  "Error": str / null,
  "Description": str,
  "BlogsDB": null
}
```

 - Get all blogs:
```
Request body:
{
  "Token": <Token>,
  "Action": "R",
  "BlogSubject": null,
  "BlogBody": null,
  "Location": null,
  "Date": null,
  "Time": null,
  "Comment": null
}

Response body:
{
  "statusCode": 200,
  "Status": <boolean>,
  "BlogSubject": null,
  "Error": str / null,
  "Description": "All blog from database",
  "BlogDB": [dicts]
}
```
 
