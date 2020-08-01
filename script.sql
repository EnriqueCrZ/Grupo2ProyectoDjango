create table Alumno_alumno
(
    id_alumno integer      not null
        primary key,
    nombre    varchar(45)  not null,
    apellido  varchar(45)  not null,
    dpi       varchar(13)  not null
        unique,
    telefono  varchar(10)  not null,
    correo    varchar(125) not null
);

create table Contrato_catedratico
(
    id_catedratico integer      not null
        primary key,
    nombre         varchar(45)  not null,
    apellido       varchar(45)  not null,
    dpi            varchar(13)  not null
        unique,
    telefono       varchar(10)  not null,
    correo         varchar(125) not null
);

create table Nivel_grado
(
    id_grado     integer     not null
        primary key,
    nombre_grado varchar(45) not null
);

create table Nivel_nivel
(
    id_nivel          integer     not null
        primary key ,
    nombre_nivel      varchar(45) not null,
    grado_id_grado_id integer     not null
        references Nivel_grado
            deferrable initially deferred
);

create table Contrato_contrato
(
    id_contrato                   integer not null
        primary key ,
    fecha                         date    not null,
    catedratico_id_catedratico_id integer not null
        references Contrato_catedratico
            deferrable initially deferred,
    nivel_id_nivel_id             integer not null
        references Nivel_nivel
            deferrable initially deferred
);

create index Contrato_contrato_catedratico_id_catedratico_id_45327634
    on Contrato_contrato (catedratico_id_catedratico_id);

create index Contrato_contrato_nivel_id_nivel_id_244cd223
    on Contrato_contrato (nivel_id_nivel_id);

create index Nivel_nivel_grado_id_grado_id_7aa32b78
    on Nivel_nivel (grado_id_grado_id);

create table Sucursal_sucursal
(
    id_sucursal  integer      not null
        primary key ,
    nombre       varchar(45)  not null,
    razon_social varchar(45)  not null,
    direccion    varchar(125) not null,
    telefono     varchar(10)  not null,
    correo       varchar(125) not null
);

create table Usuario_tipousuario
(
    idtipo_usuario integer     not null
        primary key ,
    tipo           varchar(45) not null
);

create table Usuario_user
(
    password                       varchar(128) not null,
    last_login                     datetime,
    id_user                        integer      not null
        primary key ,
    nombre                         varchar(45)  not null,
    correo                         varchar(125) not null
        unique,
    is_superadmin                  bool         not null,
    is_active                      bool         not null,
    is_staff                       bool         not null,
    sucursal_id_sucursal_id        integer      not null
        references Sucursal_sucursal
            deferrable initially deferred,
    tipo_usuario_idtipo_usuario_id integer      not null
        references Usuario_tipousuario
            deferrable initially deferred
);

create table Inscripcion_inscripcion
(
    id_inscripcion          integer not null
        primary key ,
    fecha                   date    not null,
    alumno_id_alumno_id     integer not null
        references Alumno_alumno
            deferrable initially deferred,
    nivel_id_nivel_id       integer not null
        references Nivel_nivel
            deferrable initially deferred,
    sucursal_id_sucursal_id integer not null
        references Sucursal_sucursal
            deferrable initially deferred,
    usuario_id_user_id      integer not null
        references Usuario_user
            deferrable initially deferred
);

create index Inscripcion_inscripcion_alumno_id_alumno_id_6f03c92d
    on Inscripcion_inscripcion (alumno_id_alumno_id);

create index Inscripcion_inscripcion_nivel_id_nivel_id_7a5af37d
    on Inscripcion_inscripcion (nivel_id_nivel_id);

create index Inscripcion_inscripcion_sucursal_id_sucursal_id_09839845
    on Inscripcion_inscripcion (sucursal_id_sucursal_id);

create index Inscripcion_inscripcion_usuario_id_user_id_ef7c8e83
    on Inscripcion_inscripcion (usuario_id_user_id);

create table Inscripcion_nota
(
    id_nota                       integer not null
        primary key ,
    fecha                         date    not null,
    inscripcion_id_inscripcion_id integer not null
        references Inscripcion_inscripcion
            deferrable initially deferred,
    nota                          integer not null
);

create index Inscripcion_nota_inscripcion_id_inscripcion_id_bfe4581e
    on Inscripcion_nota (inscripcion_id_inscripcion_id);

create index Usuario_user_sucursal_id_sucursal_id_624641e0
    on Usuario_user (sucursal_id_sucursal_id);

create index Usuario_user_tipo_usuario_idtipo_usuario_id_876bd872
    on Usuario_user (tipo_usuario_idtipo_usuario_id);

create table auth_group
(
    id   integer      not null
        primary key ,
    name varchar(150) not null
        unique
);

create table django_content_type
(
    id        integer      not null
        primary key ,
    app_label varchar(100) not null,
    model     varchar(100) not null
);

create table auth_permission
(
    id              integer      not null
        primary key ,
    content_type_id integer      not null
        references django_content_type
            deferrable initially deferred,
    codename        varchar(100) not null,
    name            varchar(255) not null
);

create table auth_group_permissions
(
    id            integer not null
        primary key ,
    group_id      integer not null
        references auth_group
            deferrable initially deferred,
    permission_id integer not null
        references auth_permission
            deferrable initially deferred
);

create index auth_group_permissions_group_id_b120cbf9
    on auth_group_permissions (group_id);

create unique index auth_group_permissions_group_id_permission_id_0cd325b0_uniq
    on auth_group_permissions (group_id, permission_id);

create index auth_group_permissions_permission_id_84c5c92e
    on auth_group_permissions (permission_id);

create index auth_permission_content_type_id_2f476e4b
    on auth_permission (content_type_id);

create unique index auth_permission_content_type_id_codename_01ab375a_uniq
    on auth_permission (content_type_id, codename);

create unique index django_content_type_app_label_model_76bd3d3b_uniq
    on django_content_type (app_label, model);

create table django_migrations
(
    id      integer      not null
        primary key ,
    app     varchar(255) not null,
    name    varchar(255) not null,
    applied datetime     not null
);


