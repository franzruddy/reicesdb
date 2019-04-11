import web
import config

db = config.db


def get_all_registro_juego():
    try:
        return db.select('registro_juego')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_registro_juego(Idregistrojuego):
    try:
        return db.select('registro_juego', where='Idregistrojuego=$Idregistrojuego', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_registro_juego(Idregistrojuego):
    try:
        return db.delete('registro_juego', where='Idregistrojuego=$Idregistrojuego', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_registro_juego(fecha_registro,jugador_idjugador,juego_idjuego,logros_idlogros):
    try:
        return db.insert('registro_juego',fecha_registro=fecha_registro,
jugador_idjugador=jugador_idjugador,
juego_idjuego=juego_idjuego,
logros_idlogros=logros_idlogros)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_registro_juego(Idregistrojuego,fecha_registro,jugador_idjugador,juego_idjuego,logros_idlogros):
    try:
        return db.update('registro_juego',Idregistrojuego=Idregistrojuego,
fecha_registro=fecha_registro,
jugador_idjugador=jugador_idjugador,
juego_idjuego=juego_idjuego,
logros_idlogros=logros_idlogros,
                  where='Idregistrojuego=$Idregistrojuego',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
