import os

TRACE = os.environ.get('CIFSDK_CLIENT_HTTP_TRACE')
TIMEOUT = os.getenv('CIFSDK_CLIENT_HTTP_TIMEOUT', 120)
RETRIES = os.getenv('CIFSDK_CLIENT_HTTP_RETRIES', 5)
RETRIES_DELAY = os.getenv('CIFSDK_CLIENT_HTTP_RETRIES_DELAY', '30,60')