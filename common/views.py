from settings.build_app import db


def commit_object_to_db(obj):
    db.session.add(obj)
    db.session.commit()
    return
