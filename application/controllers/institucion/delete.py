import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass
    def GET(self, codinstitucion, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(codinstitucion) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, codinstitucion, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(codinstitucion) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

   
    @staticmethod
    def GET_DELETE(codinstitucion, **k):
        message = None # Error message
        codinstitucion = config.check_secure_val(str(codinstitucion)) # HMAC codinstitucion validate
        result = config.model.get_institucion(int(codinstitucion)) # search  codinstitucion
        result.codinstitucion = config.make_secure_val(str(result.codinstitucion)) # apply HMAC for codinstitucion
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(codinstitucion, **k):
        form = config.web.input() # get form data
        form['codinstitucion'] = config.check_secure_val(str(form['codinstitucion'])) # HMAC codinstitucion validate
        result = config.model.delete_institucion(form['codinstitucion']) # get institucion data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            codinstitucion = config.check_secure_val(str(codinstitucion))  # HMAC user validate
            codinstitucion = config.check_secure_val(str(codinstitucion))  # HMAC user validate
            result = config.model.get_institucion(int(codinstitucion)) # get codinstitucion data
            result.codinstitucion = config.make_secure_val(str(result.codinstitucion)) # apply HMAC to codinstitucion
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/institucion') # render institucion delete.html 
