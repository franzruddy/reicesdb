import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    def GET(self, Idmaestro, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(Idmaestro) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, Idmaestro, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(Idmaestro) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html



    @staticmethod
    def GET_EDIT(Idmaestro, **k):
        message = None # Error message
        Idmaestro = config.check_secure_val(str(Idmaestro)) # HMAC Idmaestro validate
        result = config.model.get_maestro(int(Idmaestro)) # search for the Idmaestro
        result.Idmaestro = config.make_secure_val(str(result.Idmaestro)) # apply HMAC for Idmaestro
        return config.render.edit(result, message) # render maestro edit.html

    @staticmethod
    def POST_EDIT(Idmaestro, **k):
        form = config.web.input()  # get form data
        form['Idmaestro'] = config.check_secure_val(str(form['Idmaestro'])) # HMAC Idmaestro validate
        # edit user with new data
        result = config.model.edit_maestro(
            form['Idmaestro'],form['Nombre'],form['Ap_paterno'],form['Ap_materno'],form['Usuario'],form['idgrupo_grupo'],
        )
        if result == None: # Error on udpate data
            Idmaestro = config.check_secure_val(str(Idmaestro)) # validate HMAC Idmaestro
            result = config.model.get_maestro(int(Idmaestro)) # search for Idmaestro data
            result.Idmaestro = config.make_secure_val(str(result.Idmaestro)) # apply HMAC to Idmaestro
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/maestro') # render maestro index.html
