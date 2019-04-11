import web

db_host = 'localhost'
db_name = 'raicesdb'
db_user = 'raices'
db_pw = 'raices.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )