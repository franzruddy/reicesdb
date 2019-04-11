import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    def GET(self, Idregistrojuego):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(Idregistrojuego) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(Idregistrojuego):

        Idregistrojuego = config.check_secure_val(str(Idregistrojuego)) # HMAC Idregistrojuego validate
        result = config.model.get_registro_juego(Idregistrojuego) # search for the Idregistrojuego data
        return config.render.view(result) # render view.html with Idregistrojuego data
