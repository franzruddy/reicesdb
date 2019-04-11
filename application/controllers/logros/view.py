import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    def GET(self, Id_logros):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(Id_logros) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(Id_logros):

        Id_logros = config.check_secure_val(str(Id_logros)) # HMAC Id_logros validate
        result = config.model.get_logros(Id_logros) # search for the Id_logros data
        return config.render.view(result) # render view.html with Id_logros data
