# Import dependencies
from flask import Flask

# Create a new Flask App Instance
app = Flask(__name__)

#Create Flask Routes
# Adding Root Route
@app.route('/')
def hello_world():
    return 'Hello world'
