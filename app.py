from settings.build_app import create_app
from settings.register_blueprint import register_blueprint

app = create_app()
register_blueprint(app)

if __name__ == "__main__":
    # print(app.url_map)
    app.run(host='localhost', port=5000, debug=True)
