from flask_restplus import Resource, Api, fields, Namespace, abort
from flask import request, session, make_response, redirect, Response, jsonify
from api.middleware.exception_handler import exceptionhander
from api.middleware.crud import insert_status, insert_type


api = Namespace('Ticket', description='Ticket Operations')


@api.route('/')
class TicketList(Resource):
    """ Ticket Related Operations  """

    def __init__(self, Resource):
        self.api = api

    @api.doc(description='Get Ticket Details')
    def get(self):
        return jsonify({'status': 'okay'})



@api.route('/<string:id>')
class Ticket(Resource):
    """ Process Tickets on the basis of Ticket numbers
    """

    def __init__(self, Resource):
        self.api = api

    @api.doc(description='Get Ticket information on the basis of Ticket Id')
    def get(self, id):
        """
        Get Ticket details on the basis of Ticket Id
        :param id:
        :return:
        """
        return jsonify({'ticket_id': id})


@api.route('/status/<string:status>')
class Status(Resource):
    """
    To upsert the status
    """

    def __init__(self, Resource):
        self.api = api

    @api.doc(description='To Add the Status')
    def post(self, status):
        insert_status(status=status)
        return jsonify({'status': status})

@api.route('/type/<string:type>')
class Type(Resource):
    """
    To update the ticket type
    """

    def __init__(self,Resource):
        self.api = api

    @api.doc(description='To add the type of the ticket')
    def post(self, type):
        insert_type(type=type)
        return jsonify({'status': 'success',
                        'ticket_type': type})