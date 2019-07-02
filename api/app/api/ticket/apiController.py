from flask_restplus import Resource, Api, fields, Namespace, abort
from flask import request, session, make_response, redirect, Response, jsonify


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