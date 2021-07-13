import os
import shutil
import tempfile

import pytest
from petshop import create_app
from petshop.db import get_db, init_db

@pytest.fixture
def app():
    db_dir = tempfile.mkdtemp()
    orig_db_file = os.path.join(os.path.dirname(__file__), 'test_db.sqlite')
    shutil.copy(orig_db_file, db_dir)
    used_db_file = os.path.join(db_dir, "test_db.sqlite")
    
    app = create_app({
        'TESTING': True,
        'DATABASE': used_db_file,
    })

    yield app
    
    shutil.rmtree(db_dir)
    
@pytest.fixture
def client(app):
    return app.test_client()
    
