def init_app(app):
    # Configure the DB here or in app.py
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_BINDS'] = {
        'db': "sqlite:///SPCADFW.sqlite"
    }
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SPCADFW.sqlite'

    db.init_app(app)
    app.logger.info('Initialized models')

    with app.app_context():
        from .Users import Users
        from .Pets import Pets
        from .PetTypes import PetTypes
        from .Adoptions import Adoptions
        from .Reviews import Reviews

    db.create_all()
    db.session.commit()
