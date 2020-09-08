source virtual/bin/activate
export SECRET_KEY='your-secret-key-comes-here'
export JWT_SECRET_KEY='your-secret-key-comes-here'
export DATABASE_URL="postgres://xxxxx:xxx@localhost:5432/xxx"

python manage.py server