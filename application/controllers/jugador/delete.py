import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    def GET(self, Idjugador, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(Idjugador) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, Idjugador, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(Idjugador) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html



    @staticmethod
    def GET_DELETE(Idjugador, **k):
        message = None # Error message
        Idjugador = config.check_secure_val(str(Idjugador)) # HMAC Idjugador validate
        result = config.model.get_jugador(int(Idjugador)) # search  Idjugador
        result.Idjugador = config.make_secure_val(str(result.Idjugador)) # apply HMAC for Idjugador
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(Idjugador, **k):
        form = config.web.input() # get form data
        form['Idjugador'] = config.check_secure_val(str(form['Idjugador'])) # HMAC Idjugador validate
        result = config.model.delete_jugador(form['Idjugador']) # get jugador data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            Idjugador = config.check_secure_val(str(Idjugador))  # HMAC user validate
            Idjugador = config.check_secure_val(str(Idjugador))  # HMAC user validate
            result = config.model.get_jugador(int(Idjugador)) # get Idjugador data
            result.Idjugador = config.make_secure_val(str(result.Idjugador)) # apply HMAC to Idjugador
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/jugador') # render jugador delete.html 
