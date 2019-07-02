from flask_restplus import Api
from app.api.ticket.apiController import api as ns1

api = Api(version='1.0',
          title='Helpdesl Rest API',
          doc='/swagger',
          description='Document for Helpdesk REST API',
          contact='helpdesk-developers@geminisolutions.in',
          default='tweet')

api.add_namespace(ns1, path='/api/v1/ticket')
