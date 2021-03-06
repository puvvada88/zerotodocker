#     Copyright 2014 Netflix, Inc.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

# Database setup
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:sketchypassword@sketchy_postgres:5432/sketchy'

# Set hostname:port of your server or IP address if running in test setup (default is 127.0.0.1:8000)
# If you are using Nginx with SSL, only specify IP or Hostname
# Alternatively, you can export the 'host' variable on your system to set this as well
HOST = os.getenv('host', '0.0.0.0:8000')

# Set to true if you are serving Sketchy over SSL with Nginx (default is False)
# Alternatively, you can export the 'use_ssl' variable on your system as well
SSL = os.getenv('use_ssl', False)

# Broker configuration information, currently only supporting Redis
CELERY_BROKER_URL = 'redis://sketchy_redis:6379'
CELERY_RESULT_BACKEND = 'redis://sketchy_redis:6379'

# Local Screenshot storage
LOCAL_STORAGE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')

# Maximum number of Celery Job retries on failure
MAX_RETRIES = 1

# Seconds to sleep before retrying the task
COOLDOWN = 5

# Path to Phanotom JS
PHANTOMJS = '/usr/local/bin/phantomjs'

# S3 Specific configurations
# This will store your sketches, scrapes, and html in an S3 bucket
USE_S3 = False
S3_BUCKET_PREFIX = 'your_bucket.s3.here.test'
S3_LINK_EXPIRATION = 6000000

# Token Auth Setup
REQUIRE_AUTH = False
AUTH_TOKEN = os.getenv('auth_token', 'test')

# Log file configuration (currently only logs errors)
SKETCHY_LOG_FILE = "/usr/local/src/sketchy/sketchy-deploy.log"

# Perform SSL host validation (set to False if you want to scrape/screenshot sketchy websites)
SSL_HOST_VALIDATION = True
