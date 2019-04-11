import web
import config
import json


class Api_institucion:
    def get(self, codinstitucion):
        try:
            # http://0.0.0.0:8080/api_institucion?user_hash=12345&action=get
            if codinstitucion is None:
                result = config.model.get_all_institucion()
                institucion_json = []
                for row in result:
                    tmp = dict(row)
                    institucion_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(institucion_json)
            else:
                # http://0.0.0.0:8080/api_institucion?user_hash=12345&action=get&codinstitucion=1
                result = config.model.get_institucion(int(codinstitucion))
                institucion_json = []
                institucion_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(institucion_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            institucion_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(institucion_json)

# http://0.0.0.0:8080/api_institucion?user_hash=12345&action=put&codinstitucion=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombreinstitucion,usuario_web):
        try:
            config.model.insert_institucion(nombreinstitucion,usuario_web)
            institucion_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(institucion_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_institucion?user_hash=12345&action=delete&codinstitucion=1
    def delete(self, codinstitucion):
        try:
            config.model.delete_institucion(codinstitucion)
            institucion_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(institucion_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_institucion?user_hash=12345&action=update&codinstitucion=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, codinstitucion, nombreinstitucion,usuario_web):
        try:
            config.model.edit_institucion(codinstitucion,nombreinstitucion,usuario_web)
            institucion_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(institucion_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            institucion_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(institucion_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            codinstitucion=None,
            nombreinstitucion=None,
            usuario_web=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            codinstitucion=user_data.codinstitucion
            nombreinstitucion=user_data.nombreinstitucion
            usuario_web=user_data.usuario_web
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(codinstitucion)
                elif action == 'put':
                    return self.put(nombreinstitucion,usuario_web)
                elif action == 'delete':
                    return self.delete(codinstitucion)
                elif action == 'update':
                    return self.update(codinstitucion, nombreinstitucion,usuario_web)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
