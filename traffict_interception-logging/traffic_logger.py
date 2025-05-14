import sqlite3
import datetime
from enum import Enum

class ResponseStatus(Enum):
    OK = "OK"
    NOT_FOUND = "NOT_FOUND"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    BAD_REQUEST = "BAD_REQUEST"
    UNAUTHORIZED = "UNAUTHORIZED"

    