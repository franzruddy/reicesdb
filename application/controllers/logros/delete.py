import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    def GET(self, Id_logros, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(Id_logros) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, Id_logros, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(Id_logros) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html



    @staticmethod
    def GET_DELETE(Id_logros, **k):
        message = None # Error message
        Id_logros = config.check_secure_val(str(Id_logros)) # HMAC Id_logros validate
        result = config.model.get_logros(int(Id_logros)) # search  Id_logros
        result.Id_logros = config.make_secure_val(str(result.Id_logros)) # apply HMAC for Id_logros
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(Id_logros, **k):
        form = config.web.input() # get form data
        form['Id_logros'] = config.check_secure_val(str(form['Id_logros'])) # HMAC Id_logros validate
        result = config.model.delete_logros(form['Id_logros']) # get logros data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            Id_logros = config.check_secure_val(str(Id_logros))  # HMAC user validate
            Id_logros = config.check_secure_val(str(Id_logros))  # HMAC user validate
            result = config.model.get_logros(int(Id_logros)) # get Id_logros data
            result.Id_logros = config.make_secure_val(str(result.Id_logros)) # apply HMAC to Id_logros
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/logros') # render logros delete.html 
