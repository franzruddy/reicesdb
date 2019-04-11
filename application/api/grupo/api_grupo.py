import web
import config
import json


class Api_grupo:
    def get(self, Idgrupo):
        try:
            # http://0.0.0.0:8080/api_grupo?user_hash=12345&action=get
            if Idgrupo is None:
                result = config.model.get_all_grupo()
                grupo_json = []
                for row in result:
                    tmp = dict(row)
                    grupo_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(grupo_json)
            else:
                # http://0.0.0.0:8080/api_grupo?user_hash=12345&action=get&Idgrupo=1
                result = config.model.get_grupo(int(Idgrupo))
                grupo_json = []
                grupo_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(grupo_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            grupo_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(grupo_json)

# http://0.0.0.0:8080/api_grupo?user_hash=12345&action=put&Idgrupo=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, Nombre,id_codinstitucion):
        try:
            config.model.insert_grupo(Nombre,id_codinstitucion)
            grupo_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(grupo_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_grupo?user_hash=12345&action=delete&Idgrupo=1
    def delete(self, Idgrupo):
        try:
            config.model.delete_grupo(Idgrupo)
            grupo_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(grupo_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_grupo?user_hash=12345&action=update&Idgrupo=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, Idgrupo, Nombre,id_codinstitucion):
        try:
            config.model.edit_grupo(Idgrupo,Nombre,id_codinstitucion)
            grupo_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(grupo_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            grupo_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(grupo_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            Idgrupo=None,
            Nombre=None,
            id_codinstitucion=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            Idgrupo=user_data.Idgrupo
            Nombre=user_data.Nombre
            id_codinstitucion=user_data.id_codinstitucion
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(Idgrupo)
                elif action == 'put':
                    return self.put(Nombre,id_codinstitucion)
                elif action == 'delete':
                    return self.delete(Idgrupo)
                elif action == 'update':
                    return self.update(Idgrupo, Nombre,id_codinstitucion)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
