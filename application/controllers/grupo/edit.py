import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass
    def GET(self, Idgrupo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(Idgrupo) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, Idgrupo, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(Idgrupo) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html



    @staticmethod
    def GET_EDIT(Idgrupo, **k):
        message = None # Error message
        Idgrupo = config.check_secure_val(str(Idgrupo)) # HMAC Idgrupo validate
        result = config.model.get_grupo(int(Idgrupo)) # search for the Idgrupo
        result.Idgrupo = config.make_secure_val(str(result.Idgrupo)) # apply HMAC for Idgrupo
        return config.render.edit(result, message) # render grupo edit.html

    @staticmethod
    def POST_EDIT(Idgrupo, **k):
        form = config.web.input()  # get form data
        form['Idgrupo'] = config.check_secure_val(str(form['Idgrupo'])) # HMAC Idgrupo validate
        # edit user with new data
        result = config.model.edit_grupo(
            form['Idgrupo'],form['Nombre'],form['id_codinstitucion'],
        )
        if result == None: # Error on udpate data
            Idgrupo = config.check_secure_val(str(Idgrupo)) # validate HMAC Idgrupo
            result = config.model.get_grupo(int(Idgrupo)) # search for Idgrupo data
            result.Idgrupo = config.make_secure_val(str(result.Idgrupo)) # apply HMAC to Idgrupo
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/grupo') # render grupo index.html
