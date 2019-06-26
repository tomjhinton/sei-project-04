import os

db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/interstitialapp')
secret = os.getenv('SECRET', 'a suitable secret')
