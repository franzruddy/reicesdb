# Author : Salvador Hernandez Mendoza
# Email  : salvadorhm@gmail.com
# Twitter: @salvadorhm
import web
import config


#activate ssl certificate
ssl = False

urls = (
    '/', 'application.controllers.main.index.Index',
    '/login', 'application.controllers.main.login.Login',
    '/logout', 'application.controllers.main.logout.Logout',
    '/users', 'application.controllers.users.index.Index',
    '/users/printer', 'application.controllers.users.printer.Printer',
    '/users/view/(.+)', 'application.controllers.users.view.View',
    '/users/edit/(.+)', 'application.controllers.users.edit.Edit',
    '/users/delete/(.+)', 'application.controllers.users.delete.Delete',
    '/users/insert', 'application.controllers.users.insert.Insert',
    '/users/change_pwd', 'application.controllers.users.change_pwd.Change_pwd',
    '/logs', 'application.controllers.logs.index.Index',
    '/logs/printer', 'application.controllers.logs.printer.Printer',
    '/logs/view/(.+)', 'application.controllers.logs.view.View',
    '/institucion', 'application.controllers.institucion.index.Index',
    '/institucion/view/(.+)', 'application.controllers.institucion.view.View',
    '/institucion/edit/(.+)', 'application.controllers.institucion.edit.Edit',
    '/institucion/delete/(.+)', 'application.controllers.institucion.delete.Delete',
    '/institucion/insert', 'application.controllers.institucion.insert.Insert',
    '/api_institucion/?', 'application.api.institucion.api_institucion.Api_institucion',
    '/grupo', 'application.controllers.grupo.index.Index',
    '/grupo/view/(.+)', 'application.controllers.grupo.view.View',
    '/grupo/edit/(.+)', 'application.controllers.grupo.edit.Edit',
    '/grupo/delete/(.+)', 'application.controllers.grupo.delete.Delete',
    '/grupo/insert', 'application.controllers.grupo.insert.Insert',
    '/api_grupo/?', 'application.api.grupo.api_grupo.Api_grupo',
    '/maestro', 'application.controllers.maestro.index.Index',
    '/maestro/view/(.+)', 'application.controllers.maestro.view.View',
    '/maestro/edit/(.+)', 'application.controllers.maestro.edit.Edit',
    '/maestro/delete/(.+)', 'application.controllers.maestro.delete.Delete',
    '/maestro/insert', 'application.controllers.maestro.insert.Insert',
    '/api_maestro/?', 'application.api.maestro.api_maestro.Api_maestro',
    '/jugador', 'application.controllers.jugador.index.Index',
    '/jugador/view/(.+)', 'application.controllers.jugador.view.View',
    '/jugador/edit/(.+)', 'application.controllers.jugador.edit.Edit',
    '/jugador/delete/(.+)', 'application.controllers.jugador.delete.Delete',
    '/jugador/insert', 'application.controllers.jugador.insert.Insert',
    '/api_jugador/?', 'application.api.jugador.api_jugador.Api_jugador',
    '/juego', 'application.controllers.juego.index.Index',
    '/juego/view/(.+)', 'application.controllers.juego.view.View',
    '/juego/edit/(.+)', 'application.controllers.juego.edit.Edit',
    '/juego/delete/(.+)', 'application.controllers.juego.delete.Delete',
    '/juego/insert', 'application.controllers.juego.insert.Insert',
    '/api_juego/?', 'application.api.juego.api_juego.Api_juego',
    '/logros', 'application.controllers.logros.index.Index',
    '/logros/view/(.+)', 'application.controllers.logros.view.View',
    '/logros/edit/(.+)', 'application.controllers.logros.edit.Edit',
    '/logros/delete/(.+)', 'application.controllers.logros.delete.Delete',
    '/logros/insert', 'application.controllers.logros.insert.Insert',
    '/api_logros/?', 'application.api.logros.api_logros.Api_logros',
    '/registro_juego', 'application.controllers.registro_juego.index.Index',
    '/registro_juego/view/(.+)', 'application.controllers.registro_juego.view.View',
    '/registro_juego/edit/(.+)', 'application.controllers.registro_juego.edit.Edit',
    '/registro_juego/delete/(.+)', 'application.controllers.registro_juego.delete.Delete',
    '/registro_juego/insert', 'application.controllers.registro_juego.insert.Insert',
    '/api_registro_juego/?', 'application.api.registro_juego.api_registro_juego.Api_registro_juego',
    )

app = web.application(urls, globals())

if ssl is True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt"
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

if web.config.get('_session') is None:
    db = config.db
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(
        app,
        store,
        initializer={
        'login': 0,
        'privilege': -1,
        'user': 'anonymous',
        'loggedin': False,
        'count': 0
        }
        )
    web.config._session = session
    web.config.session_parameters['cookie_name'] = 'kuorra'
    web.config.session_parameters['timeout'] = 10
    web.config.session_parameters['expired_message'] = 'Session expired'
    web.config.session_parameters['ignore_expiry'] = False
    web.config.session_parameters['ignore_change_ip'] = False
    web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
else:
    session = web.config._session


class Count:
    def GET(self):
        session.count += 1
        return str(session.count)


def InternalError(): 
    raise config.web.seeother('/')


def NotFound():
    raise config.web.seeother('/')

if __name__ == "__main__":
    db.printing = False # hide db transactions
    web.config.debug = False # hide debug print
    web.config.db_printing = False # hide db transactions
    app.internalerror = InternalError
    app.notfound = NotFound
    app.run()
