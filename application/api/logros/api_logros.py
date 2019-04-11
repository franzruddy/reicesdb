import web
import config
import json


class Api_logros:
    def get(self, Id_logros):
        try:
            # http://0.0.0.0:8080/api_logros?user_hash=12345&action=get
            if Id_logros is None:
                result = config.model.get_all_logros()
                logros_json = []
                for row in result:
                    tmp = dict(row)
                    logros_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(logros_json)
            else:
                # http://0.0.0.0:8080/api_logros?user_hash=12345&action=get&Id_logros=1
                result = config.model.get_logros(int(Id_logros))
                logros_json = []
                logros_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(logros_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            logros_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(logros_json)

# http://0.0.0.0:8080/api_logros?user_hash=12345&action=put&Id_logros=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre_logro,imagenes):
        try:
            config.model.insert_logros(nombre_logro,imagenes)
            logros_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(logros_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_logros?user_hash=12345&action=delete&Id_logros=1
    def delete(self, Id_logros):
        try:
            config.model.delete_logros(Id_logros)
            logros_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(logros_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_logros?user_hash=12345&action=update&Id_logros=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, Id_logros, nombre_logro,imagenes):
        try:
            config.model.edit_logros(Id_logros,nombre_logro,imagenes)
            logros_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(logros_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            logros_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(logros_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            Id_logros=None,
            nombre_logro=None,
            imagenes=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            Id_logros=user_data.Id_logros
            nombre_logro=user_data.nombre_logro
            imagenes=user_data.imagenes
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(Id_logros)
                elif action == 'put':
                    return self.put(nombre_logro,imagenes)
                elif action == 'delete':
                    return self.delete(Id_logros)
                elif action == 'update':
                    return self.update(Id_logros, nombre_logro,imagenes)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
