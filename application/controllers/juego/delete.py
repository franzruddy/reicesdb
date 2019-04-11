import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    def GET(self, idjuego, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(idjuego) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idjuego, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(idjuego) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html



    @staticmethod
    def GET_DELETE(idjuego, **k):
        message = None # Error message
        idjuego = config.check_secure_val(str(idjuego)) # HMAC idjuego validate
        result = config.model.get_juego(int(idjuego)) # search  idjuego
        result.idjuego = config.make_secure_val(str(result.idjuego)) # apply HMAC for idjuego
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(idjuego, **k):
        form = config.web.input() # get form data
        form['idjuego'] = config.check_secure_val(str(form['idjuego'])) # HMAC idjuego validate
        result = config.model.delete_juego(form['idjuego']) # get juego data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            idjuego = config.check_secure_val(str(idjuego))  # HMAC user validate
            idjuego = config.check_secure_val(str(idjuego))  # HMAC user validate
            result = config.model.get_juego(int(idjuego)) # get idjuego data
            result.idjuego = config.make_secure_val(str(result.idjuego)) # apply HMAC to idjuego
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/juego') # render juego delete.html 
