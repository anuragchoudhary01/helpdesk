from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, func
import pandas as pd
from flask import jsonify
from sqlalchemy import Enum


db = SQLAlchemy()


ticket_type = ('Request', 'Incident')
ticket_type_enum = Enum(*ticket_type, name="ticket_type_enum")


def as_dict(self):
    res_dict = {}
    full_dict = self.__dict__
    for attr in full_dict:
        try:
            jsonify(full_dict[attr])
        except TypeError:
            continue
        res_dict[attr] = full_dict[attr]
    return res_dict


def tables_to_df(cls):
    """ Returns the whole table as a Pandas Dataframe """
    def make_row(x):
        return dict([(col.key, getattr(x, col.key)) for col in inspect(cls).attrs])

    df = pd.DataFrame([make_row(x) for x in cls.query.all()])
    return df.where((pd.notnull(df)), None)


class DataModels(object):
    models = {}

    @classmethod
    def add_model(cls, model):
        if model.__tablename__ not in cls.models.keys():
            cls.models[model.__tablename__] = model

    @classmethod
    def get_model(cls, model):
        try:
            return cls.models[model]
        except KeyError as e:
            print("Key {} not registered in DataModels".format(model))
            raise(e)

    @classmethod
    def get_tablename_from_friendname(cls, friend_name):
        try:
            for key, value in cls.models.items():
                if value.__friendname__ == friend_name:
                    return key
        except KeyError as e:
            print("Given friend name not matches with any of the existing models")
            raise(e)



