import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    def GET(self, Idregistrojuego, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(Idregistrojuego) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, Idregistrojuego, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(Idregistrojuego) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html




    @staticmethod
    def GET_EDIT(Idregistrojuego, **k):
        message = None # Error message
        Idregistrojuego = config.check_secure_val(str(Idregistrojuego)) # HMAC Idregistrojuego validate
        result = config.model.get_registro_juego(int(Idregistrojuego)) # search for the Idregistrojuego
        result.Idregistrojuego = config.make_secure_val(str(result.Idregistrojuego)) # apply HMAC for Idregistrojuego
        return config.render.edit(result, message) # render registro_juego edit.html

    @staticmethod
    def POST_EDIT(Idregistrojuego, **k):
        form = config.web.input()  # get form data
        form['Idregistrojuego'] = config.check_secure_val(str(form['Idregistrojuego'])) # HMAC Idregistrojuego validate
        # edit user with new data
        result = config.model.edit_registro_juego(
            form['Idregistrojuego'],form['fecha_registro'],form['jugador_idjugador'],form['juego_idjuego'],form['logros_idlogros'],
        )
        if result == None: # Error on udpate data
            Idregistrojuego = config.check_secure_val(str(Idregistrojuego)) # validate HMAC Idregistrojuego
            result = config.model.get_registro_juego(int(Idregistrojuego)) # search for Idregistrojuego data
            result.Idregistrojuego = config.make_secure_val(str(result.Idregistrojuego)) # apply HMAC to Idregistrojuego
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/registro_juego') # render registro_juego index.html
