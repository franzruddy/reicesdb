import web
import config
import json


class Api_registro_juego:
    def get(self, Idregistrojuego):
        try:
            # http://0.0.0.0:8080/api_registro_juego?user_hash=12345&action=get
            if Idregistrojuego is None:
                result = config.model.get_all_registro_juego()
                registro_juego_json = []
                for row in result:
                    tmp = dict(row)
                    registro_juego_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(registro_juego_json)
            else:
                # http://0.0.0.0:8080/api_registro_juego?user_hash=12345&action=get&Idregistrojuego=1
                result = config.model.get_registro_juego(int(Idregistrojuego))
                registro_juego_json = []
                registro_juego_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(registro_juego_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            registro_juego_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(registro_juego_json)

# http://0.0.0.0:8080/api_registro_juego?user_hash=12345&action=put&Idregistrojuego=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, fecha_registro,jugador_idjugador,juego_idjuego,logros_idlogros):
        try:
            config.model.insert_registro_juego(fecha_registro,jugador_idjugador,juego_idjuego,logros_idlogros)
            registro_juego_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(registro_juego_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_registro_juego?user_hash=12345&action=delete&Idregistrojuego=1
    def delete(self, Idregistrojuego):
        try:
            config.model.delete_registro_juego(Idregistrojuego)
            registro_juego_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(registro_juego_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_registro_juego?user_hash=12345&action=update&Idregistrojuego=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, Idregistrojuego, fecha_registro,jugador_idjugador,juego_idjuego,logros_idlogros):
        try:
            config.model.edit_registro_juego(Idregistrojuego,fecha_registro,jugador_idjugador,juego_idjuego,logros_idlogros)
            registro_juego_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(registro_juego_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            registro_juego_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(registro_juego_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            Idregistrojuego=None,
            fecha_registro=None,
            jugador_idjugador=None,
            juego_idjuego=None,
            logros_idlogros=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            Idregistrojuego=user_data.Idregistrojuego
            fecha_registro=user_data.fecha_registro
            jugador_idjugador=user_data.jugador_idjugador
            juego_idjuego=user_data.juego_idjuego
            logros_idlogros=user_data.logros_idlogros
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(Idregistrojuego)
                elif action == 'put':
                    return self.put(fecha_registro,jugador_idjugador,juego_idjuego,logros_idlogros)
                elif action == 'delete':
                    return self.delete(Idregistrojuego)
                elif action == 'update':
                    return self.update(Idregistrojuego, fecha_registro,jugador_idjugador,juego_idjuego,logros_idlogros)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
