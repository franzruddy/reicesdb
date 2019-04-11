import web
import config

db = config.db


def get_all_grupo():
    try:
        return db.select('grupo')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_grupo(Idgrupo):
    try:
        return db.select('grupo', where='Idgrupo=$Idgrupo', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_grupo(Idgrupo):
    try:
        return db.delete('grupo', where='Idgrupo=$Idgrupo', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_grupo(Nombre,id_codinstitucion):
    try:
        return db.insert('grupo',Nombre=Nombre,
id_codinstitucion=id_codinstitucion)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_grupo(Idgrupo,Nombre,id_codinstitucion):
    try:
        return db.update('grupo',Idgrupo=Idgrupo,
Nombre=Nombre,
id_codinstitucion=id_codinstitucion,
                  where='Idgrupo=$Idgrupo',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
