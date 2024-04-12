import pytest
from backend.app import crear_app, db

@pytest.fixture(scope='module')
def app():
    app = crear_app('pruebas-caja-arena')
    with app.app_context():
        yield app

@pytest.fixture(scope='function')
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='function')
def session(app):
    with app.app_context():
        db.create_all()  # Create all tables
        db.session.begin_nested()
        yield db.session
        db.session.rollback()
        db.drop_all()  # Drop all tables