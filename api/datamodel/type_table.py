from api.datamodel.data_model import db, DataModels

@DataModels.register_model
class Type(db.Model):
    __tablename__ = 'ticket_type'
    __friendname__ = 'type'

    id = db.Column(db.Integer, primary_key=True, info={'human_name': 'Ticket type Id',
                                                               'machine_name': 'ticket_type_id',
                                                               'display': False,
                                                               'type': 'INT'})
    type = db.Column(db.String(30), info={'human_name': 'Ticket Type Name',
                                                               'machine_name': 'ticket_type_name',
                                                               'display': False,
                                                               'type': 'STRING'})