import subprocess
import sys

# upgrade pip
print("---------- Upgrading pip package ---------- \n")
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

print("----------  Installing dependencies from requirements.txt ---------- \n")
# install requirements
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

print("----------  Creating .env file from requirements.txt ----------\n")
# create .env file with variables
with open(".env", "a") as f:
    f.write("DJANGO_SETTINGS_MODULE='core.settings.development'\n")
    f.write("DEBUG=True\n")
    f.write("DATABASE_NAME='hillside-db'\n")
    f.write("DATABASE_USERNAME='dev-user'\n")
    password = input("Enter the database password: ")
    f.write("DATABASE_PASSWORD='{}'\n".format(password))
    f.close()
