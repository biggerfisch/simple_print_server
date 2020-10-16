import os

# DEBUG = True

DATABASE_PATH = os.path.join(os.getcwd(), 'sqlite.db')
DATABASE_URL = 'sqlite:///{}'.format(DATABASE_PATH)

PRINT_COMMAND = 'lp'

MAX_CONTENT_LENGTH = 128 * 1024 * 1024 # 128 MB
BASE_UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])

SECRET_KEY = 'Sm9o3iBfY2hyb20ga2ljatMgYXNz'
