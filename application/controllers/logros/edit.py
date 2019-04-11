import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass


    def GET(self, Id_logros, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(Id_logros) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, Id_logros, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(Id_logros) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html



    @staticmethod
    def GET_EDIT(Id_logros, **k):
        message = None # Error message
        Id_logros = config.check_secure_val(str(Id_logros)) # HMAC Id_logros validate
        result = config.model.get_logros(int(Id_logros)) # search for the Id_logros
        result.Id_logros = config.make_secure_val(str(result.Id_logros)) # apply HMAC for Id_logros
        return config.render.edit(result, message) # render logros edit.html

    @staticmethod
    def POST_EDIT(Id_logros, **k):
        form = config.web.input()  # get form data
        form['Id_logros'] = config.check_secure_val(str(form['Id_logros'])) # HMAC Id_logros validate
        # edit user with new data
        result = config.model.edit_logros(
            form['Id_logros'],form['nombre_logro'],form['imagenes'],
        )
        if result == None: # Error on udpate data
            Id_logros = config.check_secure_val(str(Id_logros)) # validate HMAC Id_logros
            result = config.model.get_logros(int(Id_logros)) # search for Id_logros data
            result.Id_logros = config.make_secure_val(str(result.Id_logros)) # apply HMAC to Id_logros
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/logros') # render logros index.html
