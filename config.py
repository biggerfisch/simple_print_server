DEBUG = True

DATABASE_PATH = '/tmp/test.db'
DATABASE_URL = 'sqlite:///{}'.format(DATABASE_PATH)

PRINT_COMMAND = 'echo'

MAX_CONTENT_LENGTH = 128 * 1024 * 1024 # 128 MB
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])

SECRET_KEY = 'Sm9o3iBfY2hyb20ga2ljatMgYXNz'
