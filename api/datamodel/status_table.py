from api.datamodel.data_model import db,  DataModels, PrimitiveAttributes


@DataModels.register_model
class Status(db.Model):
    __tablename__ = 'ticket_status'
    __friendname__ = 'status'

    # id_seq = db.Sequence('id_seq', start=1000, increment=1)
    id = db.Column(db.Integer, db.Sequence('id_seq', start=1000, increment=1), primary_key=True, info={'human_name': 'Ticket Status Id',
                                                               'machine_name': 'ticket_status_id',
                                                               'display': False,
                                                               'type': 'INT'})
    status = db.Column(db.String(30), info={'human_name': 'Ticket Status Name',
                                            'machine_name': 'ticket_status_name',
                                            'display': False,'type': 'STRING'})