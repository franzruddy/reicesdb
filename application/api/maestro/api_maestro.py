import web
import config
import json


class Api_maestro:
    def get(self, Idmaestro):
        try:
            # http://0.0.0.0:8080/api_maestro?user_hash=12345&action=get
            if Idmaestro is None:
                result = config.model.get_all_maestro()
                maestro_json = []
                for row in result:
                    tmp = dict(row)
                    maestro_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(maestro_json)
            else:
                # http://0.0.0.0:8080/api_maestro?user_hash=12345&action=get&Idmaestro=1
                result = config.model.get_maestro(int(Idmaestro))
                maestro_json = []
                maestro_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(maestro_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            maestro_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(maestro_json)

# http://0.0.0.0:8080/api_maestro?user_hash=12345&action=put&Idmaestro=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, Nombre,Ap_paterno,Ap_materno,Usuario,idgrupo_grupo):
        try:
            config.model.insert_maestro(Nombre,Ap_paterno,Ap_materno,Usuario,idgrupo_grupo)
            maestro_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(maestro_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_maestro?user_hash=12345&action=delete&Idmaestro=1
    def delete(self, Idmaestro):
        try:
            config.model.delete_maestro(Idmaestro)
            maestro_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(maestro_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_maestro?user_hash=12345&action=update&Idmaestro=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, Idmaestro, Nombre,Ap_paterno,Ap_materno,Usuario,idgrupo_grupo):
        try:
            config.model.edit_maestro(Idmaestro,Nombre,Ap_paterno,Ap_materno,Usuario,idgrupo_grupo)
            maestro_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(maestro_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            maestro_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(maestro_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            Idmaestro=None,
            Nombre=None,
            Ap_paterno=None,
            Ap_materno=None,
            Usuario=None,
            idgrupo_grupo=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            Idmaestro=user_data.Idmaestro
            Nombre=user_data.Nombre
            Ap_paterno=user_data.Ap_paterno
            Ap_materno=user_data.Ap_materno
            Usuario=user_data.Usuario
            idgrupo_grupo=user_data.idgrupo_grupo
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(Idmaestro)
                elif action == 'put':
                    return self.put(Nombre,Ap_paterno,Ap_materno,Usuario,idgrupo_grupo)
                elif action == 'delete':
                    return self.delete(Idmaestro)
                elif action == 'update':
                    return self.update(Idmaestro, Nombre,Ap_paterno,Ap_materno,Usuario,idgrupo_grupo)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
