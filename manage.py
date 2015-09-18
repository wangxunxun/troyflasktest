# -*- coding: utf-8 -*-
import os
from app import create_app

from flask_script import Manager






app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)



    

    
if __name__ == '__main__':

    app.run()
