from api import create_app, register_stored_procedures
# import api.datamodels as dm

app = create_app('config/config.yml')

# with app.app_context():
#     dm.db.creat_all()
#
# register_stored_procedures(app)


if __name__ == '__main__':
    app.run(threaded=True)
