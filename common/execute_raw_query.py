def _return_dict(cursor_object):
    result = []
    for data in cursor_object:
        result.append(dict(data.items()))
    cursor_object.close()
    return result


def fetch_records(query):
    from settings.build_app import db

    cursor_object = db.engine.execute(query)
    return _return_dict(cursor_object)


def execute_query_without_return_value(query):
    from settings.build_app import db
    cursor_object = db.engine.execute(query)
    print(cursor_object)
    cursor_object.close()
    return None
