from models import db
from models import User


def setup():
    db.drop_all()
    db.create_all()
    db.session.add(User('admin', 'admin@example.ge'))
    db.session.commmit()


if __name__ == '__main__':
    setup()
