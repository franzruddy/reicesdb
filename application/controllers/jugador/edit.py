import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    def GET(self, Idjugador, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(Idjugador) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, Idjugador, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(Idjugador) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html



    @staticmethod
    def GET_EDIT(Idjugador, **k):
        message = None # Error message
        Idjugador = config.check_secure_val(str(Idjugador)) # HMAC Idjugador validate
        result = config.model.get_jugador(int(Idjugador)) # search for the Idjugador
        result.Idjugador = config.make_secure_val(str(result.Idjugador)) # apply HMAC for Idjugador
        return config.render.edit(result, message) # render jugador edit.html

    @staticmethod
    def POST_EDIT(Idjugador, **k):
        form = config.web.input()  # get form data
        form['Idjugador'] = config.check_secure_val(str(form['Idjugador'])) # HMAC Idjugador validate
        # edit user with new data
        result = config.model.edit_jugador(
            form['Idjugador'],form['Nombre'],form['Ap_paterno'],form['Ap_materno'],form['Usuario'],form['idmaestro_ju'],
        )
        if result == None: # Error on udpate data
            Idjugador = config.check_secure_val(str(Idjugador)) # validate HMAC Idjugador
            result = config.model.get_jugador(int(Idjugador)) # search for Idjugador data
            result.Idjugador = config.make_secure_val(str(result.Idjugador)) # apply HMAC to Idjugador
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/jugador') # render jugador index.html
