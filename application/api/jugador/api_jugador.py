import web
import config
import json


class Api_jugador:
    def get(self, Idjugador):
        try:
            # http://0.0.0.0:8080/api_jugador?user_hash=12345&action=get
            if Idjugador is None:
                result = config.model.get_all_jugador()
                jugador_json = []
                for row in result:
                    tmp = dict(row)
                    jugador_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(jugador_json)
            else:
                # http://0.0.0.0:8080/api_jugador?user_hash=12345&action=get&Idjugador=1
                result = config.model.get_jugador(int(Idjugador))
                jugador_json = []
                jugador_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(jugador_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            jugador_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(jugador_json)

# http://0.0.0.0:8080/api_jugador?user_hash=12345&action=put&Idjugador=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, Nombre,Ap_paterno,Ap_materno,Usuario,idmaestro_ju):
        try:
            config.model.insert_jugador(Nombre,Ap_paterno,Ap_materno,Usuario,idmaestro_ju)
            jugador_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(jugador_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_jugador?user_hash=12345&action=delete&Idjugador=1
    def delete(self, Idjugador):
        try:
            config.model.delete_jugador(Idjugador)
            jugador_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(jugador_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_jugador?user_hash=12345&action=update&Idjugador=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, Idjugador, Nombre,Ap_paterno,Ap_materno,Usuario,idmaestro_ju):
        try:
            config.model.edit_jugador(Idjugador,Nombre,Ap_paterno,Ap_materno,Usuario,idmaestro_ju)
            jugador_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(jugador_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            jugador_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(jugador_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            Idjugador=None,
            Nombre=None,
            Ap_paterno=None,
            Ap_materno=None,
            Usuario=None,
            idmaestro_ju=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            Idjugador=user_data.Idjugador
            Nombre=user_data.Nombre
            Ap_paterno=user_data.Ap_paterno
            Ap_materno=user_data.Ap_materno
            Usuario=user_data.Usuario
            idmaestro_ju=user_data.idmaestro_ju
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(Idjugador)
                elif action == 'put':
                    return self.put(Nombre,Ap_paterno,Ap_materno,Usuario,idmaestro_ju)
                elif action == 'delete':
                    return self.delete(Idjugador)
                elif action == 'update':
                    return self.update(Idjugador, Nombre,Ap_paterno,Ap_materno,Usuario,idmaestro_ju)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
