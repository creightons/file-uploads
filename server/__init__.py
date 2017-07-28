from database import db
from main import app
import routes

db.init_app(app)

import models

routes.apply_routes(app)
