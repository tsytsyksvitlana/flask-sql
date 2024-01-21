import typing as t
from flask import Flask

from web_app.db.session import set_session, pop_session, close_dbs
from web_app.groups.routers import groups_router
from web_app.students.routers import students_router


def create_app():
    app = Flask(__name__)
    app.register_blueprint(groups_router)
    app.register_blueprint(students_router)
    app.before_request(set_session)

    @app.teardown_request
    def handle_session(args) -> t.Any:
        pop_session()
        return args

    @app.teardown_appcontext
    def close_db(args) -> t.Any:
        close_dbs()
        return args

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
