import os
import random

from flask import Flask, render_template

from . import db

def create_app(test_config=None):
    app = Flask("petshop")
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'petshop.sqlite')
    )

    if test_config is not None:
        app.config.update(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import pets
    app.register_blueprint(pets.bp)

    from . import db 
    db.init_app(app) 


    return app
    
