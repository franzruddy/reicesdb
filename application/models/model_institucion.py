import web
import config

db = config.db


def get_all_institucion():
    try:
        return db.select('institucion')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_institucion(codinstitucion):
    try:
        return db.select('institucion', where='codinstitucion=$codinstitucion', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_institucion(codinstitucion):
    try:
        return db.delete('institucion', where='codinstitucion=$codinstitucion', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_institucion(nombreinstitucion,usuario_web):
    try:
        return db.insert('institucion',nombreinstitucion=nombreinstitucion,
usuario_web=usuario_web)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_institucion(codinstitucion,nombreinstitucion,usuario_web):
    try:
        return db.update('institucion',codinstitucion=codinstitucion,
nombreinstitucion=nombreinstitucion,
usuario_web=usuario_web,
                  where='codinstitucion=$codinstitucion',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
