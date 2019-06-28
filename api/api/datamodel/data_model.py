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
            raise e

    @classmethod
    def get_tablename_from_friendname(cls, friend_name):
        try:
            for key, value in cls.models.items():
                if value.__friendname__ == friend_name:
                    return key
        except KeyError as e:
            print("Given friend name not matches with any of the existing models")
            raise e

    @staticmethod
    def register_model(model):
        """ Use this method as decorator to register the data models
        with the DataModels class and set them up with versioning """
        DataModels.add_model(model)
        return model


class PrimitiveAttributes(object):
    __versioned__ = {}

    is_active = db.Column(db.Boolean,
                          info={'human_name': 'Is Active',
                                            'machine_name': 'is_active',
                                            'display': False,
                                            'type': 'BOOL'})
    create_data = db.Column(db.DateTime,
                            server_default=func.now(),
                            info={'human_name': 'Creation Date',
                                  'machine_name': 'create_date',
                                  'display': True,
                                  'type': 'DATETIME'})
    update_date = db.Column(db.DateTime,
                            onupdate=func.now(),
                            info={'human_name': 'Updated Date',
                                  'machine_name': 'update_date',
                                  'display': True,
                                  'type': 'DATETIME'}
                            )
    created_by = db.Column(db.Text,
                           info={
                               'human_name': 'Created By',
                               'machine_name': 'created_by',
                               'display': True,
                               'type': 'TEXT'
                           })
    updated_by = db.Column(db.Text,
                           info={
                               'human_name': 'Updated By',
                               'machine_name': 'updated_by',
                               'display': True,
                               'type': 'TEXT'
                           })

def get_enum_values(col_info):
    clean_col_info = {}
    clean_col_info['human_name'] = col_info['human_name']
    clean_col_info['machine_name'] = col_info['machine_name']
    clean_col_info['display'] = col_info['display']
    clean_col_info['type'] = 'ENUM'
    model = DataModels.get_model(col_info['table_name'])
    clean_col_info['options'] = [{'value': inspect(model_inst).identity[0],
                                  'display_as': getattr(model_inst, col_info['value_col'])}
                                 for model_inst in model.query.all()]
    return clean_col_info


def get_col_info(model):
    """ Get all columns information for a model """
    col_info = [col.info for col in model.__table__.columns]
    cis = [ci for ci in col_info if ci]
    return [get_enum_values(ci) if ci['type'] == 'FK' else ci for ci in cis]


def get_col_name_list(model):
    """
    Get the list of columns for a table
    :param model:
    :return: list of columns
    """
    columns_info = get_col_info(model)
    column_list = []
    for item in columns_info:
        column_list.append(item['machine_name'])
    return column_list


if __name__ == '__main__':
    from api import create_app
    app = create_app('config/config.yml')
    with app.app_context():
        db.create_all(app=app)
