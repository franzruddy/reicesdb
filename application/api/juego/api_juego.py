import web
import config
import json


class Api_juego:
    def get(self, idjuego):
        try:
            # http://0.0.0.0:8080/api_juego?user_hash=12345&action=get
            if idjuego is None:
                result = config.model.get_all_juego()
                juego_json = []
                for row in result:
                    tmp = dict(row)
                    juego_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(juego_json)
            else:
                # http://0.0.0.0:8080/api_juego?user_hash=12345&action=get&idjuego=1
                result = config.model.get_juego(int(idjuego))
                juego_json = []
                juego_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(juego_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            juego_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(juego_json)

# http://0.0.0.0:8080/api_juego?user_hash=12345&action=put&idjuego=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, codjuego,nombrejuego,niveljuego,tiempojuego,puntuajejuego):
        try:
            config.model.insert_juego(codjuego,nombrejuego,niveljuego,tiempojuego,puntuajejuego)
            juego_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(juego_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_juego?user_hash=12345&action=delete&idjuego=1
    def delete(self, idjuego):
        try:
            config.model.delete_juego(idjuego)
            juego_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(juego_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_juego?user_hash=12345&action=update&idjuego=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, idjuego, codjuego,nombrejuego,niveljuego,tiempojuego,puntuajejuego):
        try:
            config.model.edit_juego(idjuego,codjuego,nombrejuego,niveljuego,tiempojuego,puntuajejuego)
            juego_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(juego_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            juego_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(juego_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            idjuego=None,
            codjuego=None,
            nombrejuego=None,
            niveljuego=None,
            tiempojuego=None,
            puntuajejuego=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            idjuego=user_data.idjuego
            codjuego=user_data.codjuego
            nombrejuego=user_data.nombrejuego
            niveljuego=user_data.niveljuego
            tiempojuego=user_data.tiempojuego
            puntuajejuego=user_data.puntuajejuego
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(idjuego)
                elif action == 'put':
                    return self.put(codjuego,nombrejuego,niveljuego,tiempojuego,puntuajejuego)
                elif action == 'delete':
                    return self.delete(idjuego)
                elif action == 'update':
                    return self.update(idjuego, codjuego,nombrejuego,niveljuego,tiempojuego,puntuajejuego)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
