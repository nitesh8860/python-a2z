from contextlib import contextmanager
from urllib.request import urlopen

@contextmanager
def closing(db):
    try:
        yield db.conn()
    finally:
        db.close()


with closing(urlopen("http://www.google.com")) as webpage:
    for line in webpage:
        # process the line
        pass