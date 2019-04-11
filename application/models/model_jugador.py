import web
import config

db = config.db


def get_all_jugador():
    try:
        return db.select('jugador')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_jugador(Idjugador):
    try:
        return db.select('jugador', where='Idjugador=$Idjugador', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_jugador(Idjugador):
    try:
        return db.delete('jugador', where='Idjugador=$Idjugador', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_jugador(Nombre,Ap_paterno,Ap_materno,Usuario,idmaestro_ju):
    try:
        return db.insert('jugador',Nombre=Nombre,
Ap_paterno=Ap_paterno,
Ap_materno=Ap_materno,
Usuario=Usuario,
idmaestro_ju=idmaestro_ju)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_jugador(Idjugador,Nombre,Ap_paterno,Ap_materno,Usuario,idmaestro_ju):
    try:
        return db.update('jugador',Idjugador=Idjugador,
Nombre=Nombre,
Ap_paterno=Ap_paterno,
Ap_materno=Ap_materno,
Usuario=Usuario,
idmaestro_ju=idmaestro_ju,
                  where='Idjugador=$Idjugador',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
