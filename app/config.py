import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(dotenv_path="app/.env")

# Fetch database credentials
DB_HOST = os.getenv('AS_DB_HOST')
DB_NAME = os.getenv('AS_DB_NAME')
DB_USER = os.getenv('AS_DB_USER')
DB_PASSWORD = os.getenv('AS_DB_PASSWORD')

# Email settings
MAIL_USERNAME = os.getenv("AS_MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("AS_MAIL_PASSWORD")
MAIL_FROM = os.getenv("AS_MAIL_FROM")
MAIL_SERVER = os.getenv("AS_MAIL_SERVER")
MAIL_PORT = int(os.getenv("AS_MAIL_PORT", 587))
MAIL_STARTTLS = os.getenv("AS_MAIL_STARTTLS", "True").lower() == "true"
MAIL_SSL_TLS = os.getenv("AS_MAIL_SSL_TLS", "False").lower() == "true"