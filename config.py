import os

# Flask WTForms
WTF_CSRF_ENABLED = False

# DB
SQLITE_URI = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db')
