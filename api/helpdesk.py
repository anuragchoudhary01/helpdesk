# from app import create_app, register_stored_procedures
# import api.datamodels as dm
from app import create_app

app = create_app('config/config.yml')

# with app.app_context():
#     dm.db.creat_all()
#
# register_stored_procedures(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0',threaded=True)
