To init, migrate, upgrate db:
flask --app vapo.py db init
flask --app vapo.py db migrate
flask --app vapo.py db upgrade

The "**init**.py" let "models" be a Model. This allows us to import names from models.

from flask_bcrypt import Bcrypt
bcrupt = Bcrypt()
bcrypt.generate_password_hash(pwd).decode('utf-8')
bcrypt.check_password_hash(hashed_pw, "password")
