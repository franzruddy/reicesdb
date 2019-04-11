import web
import config

db = config.db


def get_all_logros():
    try:
        return db.select('logros')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_logros(Id_logros):
    try:
        return db.select('logros', where='Id_logros=$Id_logros', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_logros(Id_logros):
    try:
        return db.delete('logros', where='Id_logros=$Id_logros', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_logros(nombre_logro,imagenes):
    try:
        return db.insert('logros',nombre_logro=nombre_logro,
imagenes=imagenes)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_logros(Id_logros,nombre_logro,imagenes):
    try:
        return db.update('logros',Id_logros=Id_logros,
nombre_logro=nombre_logro,
imagenes=imagenes,
                  where='Id_logros=$Id_logros',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
