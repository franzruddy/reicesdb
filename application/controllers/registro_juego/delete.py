import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    def GET(self, Idregistrojuego, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(Idregistrojuego) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, Idregistrojuego, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(Idregistrojuego) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html


    @staticmethod
    def GET_DELETE(Idregistrojuego, **k):
        message = None # Error message
        Idregistrojuego = config.check_secure_val(str(Idregistrojuego)) # HMAC Idregistrojuego validate
        result = config.model.get_registro_juego(int(Idregistrojuego)) # search  Idregistrojuego
        result.Idregistrojuego = config.make_secure_val(str(result.Idregistrojuego)) # apply HMAC for Idregistrojuego
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(Idregistrojuego, **k):
        form = config.web.input() # get form data
        form['Idregistrojuego'] = config.check_secure_val(str(form['Idregistrojuego'])) # HMAC Idregistrojuego validate
        result = config.model.delete_registro_juego(form['Idregistrojuego']) # get registro_juego data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            Idregistrojuego = config.check_secure_val(str(Idregistrojuego))  # HMAC user validate
            Idregistrojuego = config.check_secure_val(str(Idregistrojuego))  # HMAC user validate
            result = config.model.get_registro_juego(int(Idregistrojuego)) # get Idregistrojuego data
            result.Idregistrojuego = config.make_secure_val(str(result.Idregistrojuego)) # apply HMAC to Idregistrojuego
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/registro_juego') # render registro_juego delete.html 
