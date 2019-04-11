import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    def GET(self, Idmaestro, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(Idmaestro) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, Idmaestro, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(Idmaestro) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(Idmaestro, **k):
        message = None # Error message
        Idmaestro = config.check_secure_val(str(Idmaestro)) # HMAC Idmaestro validate
        result = config.model.get_maestro(int(Idmaestro)) # search  Idmaestro
        result.Idmaestro = config.make_secure_val(str(result.Idmaestro)) # apply HMAC for Idmaestro
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(Idmaestro, **k):
        form = config.web.input() # get form data
        form['Idmaestro'] = config.check_secure_val(str(form['Idmaestro'])) # HMAC Idmaestro validate
        result = config.model.delete_maestro(form['Idmaestro']) # get maestro data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            Idmaestro = config.check_secure_val(str(Idmaestro))  # HMAC user validate
            Idmaestro = config.check_secure_val(str(Idmaestro))  # HMAC user validate
            result = config.model.get_maestro(int(Idmaestro)) # get Idmaestro data
            result.Idmaestro = config.make_secure_val(str(result.Idmaestro)) # apply HMAC to Idmaestro
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/maestro') # render maestro delete.html 
