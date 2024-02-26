import urllib

SECRET_KEY = 'top_secret'
# SQLALCHEMY_DATABASE_URI='postgresql://postgres:Flask123@localhost/Flaskapp'
params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=DESKTOP-CR1OVOB\SQLEXPRESS;DATABASE=Test;Trusted_Connection=yes;')
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
SQLALCHEMY_TRACK_NOTIFICATION = False
