To init, migrate, upgrate db:
flask --app vapo.py db init
flask --app vapo.py db migrate
flask --app vapo.py db upgrade

The "**init**.py" let "models" be a Model. This allows us to import names from models.
