import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch database credentials
DB_HOST = str(os.getenv('AS_DB_HOST'))
DB_NAME = str(os.getenv('AS_DB_NAME'))
DB_USER = str(os.getenv('AS_DB_USER'))
DB_PASSWORD = str(os.getenv('AS_DB_PASSWORD'))

# Email settings
MAIL_USERNAME = str(os.getenv("AS_MAIL_USERNAME"))
MAIL_PASSWORD = str(os.getenv("AS_MAIL_PASSWORD"))
MAIL_FROM = str(os.getenv("AS_MAIL_FROM"))
MAIL_SERVER = str(os.getenv("AS_MAIL_SERVER"))
MAIL_PORT = int(str(os.getenv("AS_MAIL_PORT", "587")))
MAIL_STARTTLS = str(os.getenv("AS_MAIL_STARTTLS", "True")).lower() == "true"
MAIL_SSL_TLS = str(os.getenv("AS_MAIL_SSL_TLS", "False")).lower() == "true"