CREATE DATABASE raicesdb;

USE raicesdb;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ------------------------------------------------
-- Estructura de tabla para la tabla `institucion`

CREATE TABLE institucion (
  codinstitucion int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  nombreinstitucion varchar(45) NOT NULL,
  usuario_web varchar(20) NOT NULL,
  FOREIGN KEY (usuario_web) REFERENCES users(username)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ------------------------------------------------------
-- Extructura de tabla para la tabla `grupos`

CREATE TABLE grupo (
  Idgrupo int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  Nombre varchar(50) NOT NULL,
  id_codinstitucion int(10) NOT NULL,
  FOREIGN KEY (id_codinstitucion) REFERENCES institucion(codinstitucion)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ------------------------------------------------
-- Extructura de tabla para la tabla `maestro`

CREATE TABLE maestro (
  Idmaestro int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  Nombre varchar(50) NOT NULL,
  Ap_paterno varchar(45) NOT NULL,
  Ap_materno varchar(45) NOT NULL,
  Usuario varchar(50) NOT NULL,
  idgrupo_grupo int(11) NOT NULL,
  FOREIGN KEY (idgrupo_grupo) REFERENCES grupo(Idgrupo)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ------------------------------------------------
-- Estructura de tabla para la tabla `jugador`

CREATE TABLE jugador (
  Idjugador int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  Nombre varchar(50) NOT NULL,
  Ap_paterno varchar(45) NOT NULL,
  Ap_materno varchar(45) NOT NULL,
  Usuario varchar(50) NOT NULL,
  idmaestro_ju int(11) NOT NULL,
  FOREIGN KEY (idmaestro_ju) REFERENCES maestro(Idmaestro)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Estructura de tabla para la tabla `juego`
-- -----------------------------------------------

CREATE TABLE juego (
  idjuego int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  codjuego varchar(10) NOT NULL,
  nombrejuego varchar(100) NOT NULL,
  niveljuego varchar(25) NOT NULL,
  tiempojuego timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  puntuajejuego int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ------------------------------------------------------
-- Estructura de tabla para la tabla `logros`

CREATE TABLE logros (
  Id_logros int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  nombre_logro varchar(11) NOT NULL,
  imagenes varchar (11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ------------------------------------------------------
-- Estructura de tabla para la tabla `registro_juego`

CREATE TABLE registro_juego (
  Idregistrojuego int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  fecha_registro datetime NOT NULL,
  jugador_idjugador int(11) NOT NULL,  
  juego_idjuego int(10) NOT NULL,
  logros_idlogros int(11) NOT NULL,
  FOREIGN KEY (jugador_idjugador) REFERENCES jugador(Idjugador),
  FOREIGN KEY (juego_idjuego) REFERENCES juego(idjuego),
  FOREIGN KEY (logros_idlogros) REFERENCES logros(Id_logros)
  
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------------------------------------------------

INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);


INSERT INTO institucion (nombreinstitucion,usuario_web) VALUES ('Rabasco','admin');
INSERT INTO institucion (nombreinstitucion,usuario_web) VALUES ('fe y alegria','franz');


INSERT INTO grupo (Nombre,id_codinstitucion) VALUES ('perlita',1);
INSERT INTO grupo (Nombre,id_codinstitucion) VALUES ('moradito',1);

INSERT INTO maestro (Nombre,Ap_paterno,Ap_materno,Usuario,idgrupo_grupo) VALUES ('Alejandro','Marañon','Mendosa','p01',1)

INSERT INTO jugador (Nombre,Ap_paterno,Ap_materno,Usuario,idmaestro_ju) VALUES ('Ariel','Villaroel','Merida','ariel1',1)






SELECT * FROM users;
SELECT * FROM sessions;

CREATE USER 'raices'@'localhost' IDENTIFIED BY 'raices.2019';
GRANT ALL PRIVILEGES ON raicesdb.* TO 'raices'@'localhost';
FLUSH PRIVILEGES;
