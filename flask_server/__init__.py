from flask import Flask

app = Flask(__name__)




from flask_server.admin.route import todo
app.register_blueprint(todo)

