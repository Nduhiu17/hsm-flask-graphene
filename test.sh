source virtual/bin/activate
export SECRET_KEY='set-your-secret-key-here'
export DATABASE_URL='postgres://antony:password@localhost:5432/hsm'

pytest --cov-report term-missing --cov=app