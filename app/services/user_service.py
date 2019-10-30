#!/usr/bin/env python
from models.user import User
from config import db
from werkzeug.exceptions import NotFound

def get():
    '''
    Get all entities
    :returns: all entity
    '''
    return User.objects()

def post(body):
    '''
    Create entity with body
    :param body: request body
    :returns: the created entity
    '''
    user = User(**body).save()
    return user

def put(body):
    '''
    Update entity by id
    :param body: request body
    :returns: the updated entity
    '''
    user = User.objects(pk=body['id']).first()
    if user:
        user.update(**body)
        return User(**body)
    raise NotFound('no such entity found with id=' + str(body['id']))

def delete(id):
    '''
    Delete entity by id
    :param id: the entity id
    :returns: the response
    '''
    user = User.objects(pk=id).first()
    if user:
        user.delete()
        return {'success': True}
    raise NotFound('no such entity found with id=' + str(id))


