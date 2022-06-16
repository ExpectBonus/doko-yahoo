from flask import Flask

from db import init_db

from controllers.user_controller import user_blueprint
from controllers.comment_controller import comment_blueprint
from controllers.heatmap_controller import heatmap_blueprint

import models

app = Flask(__name__)
app.config.from_object('config.Config')
init_db(app)

app.register_blueprint(user_blueprint)
app.register_blueprint(comment_blueprint)
app.register_blueprint(heatmap_blueprint)

if __name__ == '__main__':
	app.run(host='0.0.0.0')