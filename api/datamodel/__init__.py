from api.datamodel.status_table import Status
from api.datamodel.data_model import db
from api.datamodel.data_model import DataModels
from sqlalchemy import orm


__all__ = [Status]

orm.configure_mappers()