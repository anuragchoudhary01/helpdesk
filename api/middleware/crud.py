import api.datamodel as dm
from sqlalchemy import desc


def insert_status(status):
    model_name = dm.DataModels.get_model('ticket_status')
    data = model_name(status=status)
    dm.db.session.add(data)
    dm.db.session.commit()
    return True

def insert_type(type):
    model_name = dm.DataModels.get_model('ticket_type')
    data = model_name(type=type)
    dm.db.session.add(data)
    dm.db.session.commit()
    return True
