import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass
    def GET(self, Idgrupo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(Idgrupo) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, Idgrupo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(Idgrupo) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html


    @staticmethod
    def GET_DELETE(Idgrupo, **k):
        message = None # Error message
        Idgrupo = config.check_secure_val(str(Idgrupo)) # HMAC Idgrupo validate
        result = config.model.get_grupo(int(Idgrupo)) # search  Idgrupo
        result.Idgrupo = config.make_secure_val(str(result.Idgrupo)) # apply HMAC for Idgrupo
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(Idgrupo, **k):
        form = config.web.input() # get form data
        form['Idgrupo'] = config.check_secure_val(str(form['Idgrupo'])) # HMAC Idgrupo validate
        result = config.model.delete_grupo(form['Idgrupo']) # get grupo data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            Idgrupo = config.check_secure_val(str(Idgrupo))  # HMAC user validate
            Idgrupo = config.check_secure_val(str(Idgrupo))  # HMAC user validate
            result = config.model.get_grupo(int(Idgrupo)) # get Idgrupo data
            result.Idgrupo = config.make_secure_val(str(result.Idgrupo)) # apply HMAC to Idgrupo
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/grupo') # render grupo delete.html 
