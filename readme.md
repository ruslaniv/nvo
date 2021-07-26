# To Do

## Router
1. Build a more universal URL router with dynamic routing based on request body parameters
Eg.: request.body.transport == mail => route to mail endpoint
   
## Worker files
1. Use proper serializer (pydantic/marshmallow?) with schema validation and serialization
2. Subclass all error messages to custom error class 

## Celery
1. Make celery run as app in the background
2. Add proper email sending logic

## General
1. Add logging of all requests to a separate table in the database

## Views
1. Add request validation against schema (pydantic/marshmallow?)
