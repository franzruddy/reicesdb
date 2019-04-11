import web
import config

db = config.db


def get_all_juego():
    try:
        return db.select('juego')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_juego(idjuego):
    try:
        return db.select('juego', where='idjuego=$idjuego', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_juego(idjuego):
    try:
        return db.delete('juego', where='idjuego=$idjuego', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_juego(codjuego,nombrejuego,niveljuego,tiempojuego,puntuajejuego):
    try:
        return db.insert('juego',codjuego=codjuego,
nombrejuego=nombrejuego,
niveljuego=niveljuego,
tiempojuego=tiempojuego,
puntuajejuego=puntuajejuego)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_juego(idjuego,codjuego,nombrejuego,niveljuego,tiempojuego,puntuajejuego):
    try:
        return db.update('juego',idjuego=idjuego,
codjuego=codjuego,
nombrejuego=nombrejuego,
niveljuego=niveljuego,
tiempojuego=tiempojuego,
puntuajejuego=puntuajejuego,
                  where='idjuego=$idjuego',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
