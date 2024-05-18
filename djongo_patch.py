from pymongo.database import Database as _Database

def patched_bool(self):
    return self is not None

_Database.__bool__ = patched_bool