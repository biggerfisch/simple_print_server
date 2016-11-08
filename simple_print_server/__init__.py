from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# Get thr routes
from simple_print_server import views
