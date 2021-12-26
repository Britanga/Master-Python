CREATE DATABASE IF NOT EXISTS master_python;    -- Sino existe, crea BaseDatos
use master_python;                              -- Usar BD para crear tabla

CREATE TABLE usuarios(
id          int(25) auto_increment not null,    -- not null = atributo obligatorio
nombre      varchar(100),
apellidos   varchar(255),
email       varchar(255) not null,
password    varchar(255) not null,
fecha       date not null,                      -- Guarda fecha de Registro
CONSTRAINT pk_usuarios PRIMARY KEY(id),         -- Define PrimaryKey "id"
CONSTRAINT uq_email UNIQUE(email)               -- Define atributo único "email"
)ENGINE=InnoDb;                                 -- Permite relaciones entre tablas

CREATE TABLE notas(
id          int(25) auto_increment not null,
usuario_id  int(25) not null,       -- AtributRelacional para saber q nota es de c/usuario
titulo      varchar(255) not null,
descripcion MEDIUMTEXT,
fecha       date not null,
CONSTRAINT pk_notas PRIMARY KEY(id),
CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
-- usuario_id relaciona/guarda "id" de tabla "usuarios"
)ENGINE=InnoDb;