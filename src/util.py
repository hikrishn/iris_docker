import re
import json
import datetime
import const
from time import mktime
import pytz
import dateutil.parser

REGEX_IS_NUMBER = re.compile('^\d*$')

# Test if value is a number
def is_number(n):
    return True if REGEX_IS_NUMBER.match(n) else False

# Test if input is time with proper format
def is_time(t):
    try:
        datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
    except:
        return False
    return True
# Test if input time is ISO 8601 format
def is_iso_time(t):
    try:
        dateutil.parser.parse(t)
        print('In is ISO')
    except Exception as inst:
        print (type(inst))
        return False
    return True

# Test if input time is ISO 8601 format
def convert_iso_time_utc(t):
    try:
        d = dateutil.parser.parse(t)
        utc = pytz.UTC
        d = d.replace(tzinfo=utc) - d.utcoffset()
        print('In convert ISO')
        print(d)
        print('converting to UTC')
        return d.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as inst:
        print('In error iso')
        print (type(inst))     # the exception instance
        return t
    return t

# Test if input is time with proper format
def secs_between_dates(t1, t2):
    try:
        a = datetime.datetime.strptime(t1, '%Y-%m-%d %H:%M:%S')
        b = datetime.datetime.strptime(t2, '%Y-%m-%d %H:%M:%S')
        return (b-a).total_seconds()
    except:
        return 0
    return 0

# Verify 10 digit number
def verify_phone_number(n):
    return bool(re.search("\d{11}", str(n))) and (str(n)[0] == "1") and len(n) == 11

def is_date(t):
    try:
        datetime.datetime.strptime(t, '%Y-%m-%d')
    except:
        return False
    return True

def is_int(t):
    try:
        int(t)
    except:
        return False
    return True


# Test if input is text or unicode
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

# Class to build and return response
class ResponseUtil:
    status      = 200
    headers     = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }
    message     = {
        "success": True
    }
    logger      = None

    def __init__(self, status, message, logger):
        self.status = status
        self.message = message
        self.logger = logger

    # Handler to serialize datetime
    def datetime_handler(x):
        if isinstance(x, datetime.datetime):
            return x.isoformat()
        raise x
    def response(self, serialize=True):
        data    = {
            "statusCode": self.status,
            "headers": self.headers
        }
        if serialize:
            self.logger.debug('in serialize ')
            self.logger.debug(self.message)
            data["body"] = json.dumps(self.message, default=self.datetime_handler)
        else:
            data["body"] = self.message
        self.logger.debug(data)
        return data

class ErrorUtil:
    correlation_id  = 0
    status = 200
    domain = "accounts"
    endpoint = ""
    code = ""
    message = ""
    items = ""
    logger = None
    headers     = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }

    def __init__(self, correlation_id, status, domain, endpoint, code, message, items, logger):
        self.correlation_id = correlation_id
        self.status = status
        self.domain = domain
        self.endpoint = endpoint
        self.code = code
        self.message = message
        self.logger = logger
        self.items = items

    def response(self):

        data = {
            "statusCode": self.status,
            "headers": self.headers,
            "body": json.dumps({
                "errors": [
                    {
                        "correlation_id": self.correlation_id,
                        "status": self.status,
                        "domain": self.domain,
                        "endpoint": self.endpoint,
                        "code": self.code,
                        "message": self.message,
                        "reason": const.ERROR.get(self.code).get("value"),
                        "source": const.ERROR.get(self.code).get("category"),
                        "items": self.items
                    }
                ]
            })
        }

        self.logger.debug('Error response: \n %s', json.dumps(data, indent=2))

        return data

class AuthErrorUtil:
    status = 200
    data = ""
    size = 0
    error = ""
    error_string = ""
    logger = None
    headers     = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }

    def __init__(self, status, data, size, error, error_string, logger):
        self.status = status
        self.data = data
        self.size = size
        self.error = error
        self.error_string = message
        self.logger = logger

    def response(self):

        data = {
            "status": self.status,
            "headers": self.headers,
            "body": json.dumps({
                        "status": self.status,
                        "data": self.data,
                        "size": self.size,
                        "error": self.error,
                        "message": self.message,
                        "error_string": self.error_string,
                        "size": self.size
            })
        }

        self.logger.debug('Error response: \n %s', json.dumps(data, indent=2))

        return data

class ApiMgrErrorUtil:
    correlation_id  = 0
    status = 401
    code = ""
    message = ""
    description = ""
    logger = None
    headers     = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }

    def __init__(self, correlation_id, status, code, message, description, logger):
        self.correlation_id = correlation_id
        self.status = status
        self.code = code
        self.message = message
        self.description = description
        self.logger = logger

    def response(self):

        data = {
            "statusCode": self.status,
            "headers": self.headers,
            "body": json.dumps({
                "fault":
                    {
                        "code": self.code,
                        "status": self.status,
                        "message": self.message,
                        "description": self.description,
                    }
            })
        }

        self.logger.debug('Error response: \n %s', json.dumps(data, indent=2))

        return data