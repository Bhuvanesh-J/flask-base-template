class ExecuteQuery():
    def __init__(self):
        from app import db
        self.db = db

    def _return_dict(self, cursor_object):
        result = []
        for data in cursor_object:
            result.append(dict(data.items()))
        cursor_object.close()
        return result

    def fetch_records(self, query):
        cursor_object = self.db.engine.execute(query)
        return self._return_dict(cursor_object)

    def execute_query_without_return_value(self, query):
        cursor_object = self.db.engine.execute(query)
        cursor_object.close()
        return None
