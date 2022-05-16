
from settings.build_app import create_app

app = create_app()
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

if __name__ == "__main__":
    # print(app.url_map)
    app.run(host='localhost', port=5000, debug=True)
