import web
import config

db = config.db


def get_all_maestro():
    try:
        return db.select('maestro')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_maestro(Idmaestro):
    try:
        return db.select('maestro', where='Idmaestro=$Idmaestro', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_maestro(Idmaestro):
    try:
        return db.delete('maestro', where='Idmaestro=$Idmaestro', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_maestro(Nombre,Ap_paterno,Ap_materno,Usuario,idgrupo_grupo):
    try:
        return db.insert('maestro',Nombre=Nombre,
Ap_paterno=Ap_paterno,
Ap_materno=Ap_materno,
Usuario=Usuario,
idgrupo_grupo=idgrupo_grupo)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_maestro(Idmaestro,Nombre,Ap_paterno,Ap_materno,Usuario,idgrupo_grupo):
    try:
        return db.update('maestro',Idmaestro=Idmaestro,
Nombre=Nombre,
Ap_paterno=Ap_paterno,
Ap_materno=Ap_materno,
Usuario=Usuario,
idgrupo_grupo=idgrupo_grupo,
                  where='Idmaestro=$Idmaestro',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
