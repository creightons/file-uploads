from server import db, app
import os

def main():
    if os.path.isfile('mydb.sqlite'):
        os.remove('mydb.sqlite')

    with app.test_request_context():
        db.init_app(app)
        import server.models
        db.create_all()

if __name__ == '__main__':
    main()
