import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass
    def GET(self, codinstitucion, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(codinstitucion) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, codinstitucion, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(codinstitucion) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html


       
    
    @staticmethod
    def GET_EDIT(codinstitucion, **k):
        message = None # Error message
        codinstitucion = config.check_secure_val(str(codinstitucion)) # HMAC codinstitucion validate
        result = config.model.get_institucion(int(codinstitucion)) # search for the codinstitucion
        result.codinstitucion = config.make_secure_val(str(result.codinstitucion)) # apply HMAC for codinstitucion
        return config.render.edit(result, message) # render institucion edit.html

    @staticmethod
    def POST_EDIT(codinstitucion, **k):
        form = config.web.input()  # get form data
        form['codinstitucion'] = config.check_secure_val(str(form['codinstitucion'])) # HMAC codinstitucion validate
        # edit user with new data
        result = config.model.edit_institucion(
            form['codinstitucion'],form['nombreinstitucion'],form['usuario_web'],
        )
        if result == None: # Error on udpate data
            codinstitucion = config.check_secure_val(str(codinstitucion)) # validate HMAC codinstitucion
            result = config.model.get_institucion(int(codinstitucion)) # search for codinstitucion data
            result.codinstitucion = config.make_secure_val(str(result.codinstitucion)) # apply HMAC to codinstitucion
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/institucion') # render institucion index.html
