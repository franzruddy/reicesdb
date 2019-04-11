import web

db_host = 'lmag6s0zwmcswp5w.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'usejmam2npbb581f'
db_user = 'y7llczkeg2yfbdup'
db_pw = 'qalq50cosono2ds6'


# import web

# db_host = 'localhost'
# db_name = 'raicesdb'
# db_user = 'raices'
# db_pw = 'raices.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )


    