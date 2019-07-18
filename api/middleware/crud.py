import api.datamodel as dm
from sqlalchemy import desc


def insert_status(status):
    model_name = dm.DataModels.get_model('ticket_status')
    data = model_name(status=status)
    dm.db.session.add(data)
    dm.db.session.commit()
    return True