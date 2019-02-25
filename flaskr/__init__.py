import os

from flask import Flask

def create_app(test_config=None:
    # Create and configure the application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, flaskr.sqlite),
    )

    
