USE Pescore;
TRUNCATE TABLE `competencia_categoria`;
TRUNCATE TABLE `competencia_club`;
TRUNCATE TABLE `competencia_participante`;
TRUNCATE TABLE `competencia_especialidad`;

#CATEGORIAS
INSERT INTO `competencia_categoria`(`nombre`) VALUES ("Seniors");
INSERT INTO `competencia_categoria`(`nombre`) VALUES ("Damas");
INSERT INTO `competencia_categoria`(`nombre`) VALUES ("Mayores Promocionales");
INSERT INTO `competencia_categoria`(`nombre`) VALUES ("Mayores Federados");
INSERT INTO `competencia_categoria`(`nombre`) VALUES ("Juveniles");

#CLUBES
INSERT INTO `competencia_club`(`nombre`, `abreviacion`) 
VALUES ("El Pelicano","PEL");
INSERT INTO `competencia_club`(`nombre`, `abreviacion`) 
VALUES ("Rivadavia","RIV");
INSERT INTO `competencia_club`(`nombre`, `abreviacion`) 
VALUES ("Medrano","MED");

#PARTICIPANTES
INSERT INTO 
`competencia_participante`(`nombre`, `apellido`, 
	`fechaNacimiento`, `categoria_id`, `club_id`) 
VALUES ("Martin","Perez","1998/2/2",1,1);
INSERT INTO 
`competencia_participante`(`nombre`, `apellido`, 
	`fechaNacimiento`, `categoria_id`, `club_id`) 
VALUES ("Maximiliano","Sanchez","1998/2/2",2,2);
INSERT INTO 
`competencia_participante`(`nombre`, `apellido`, 
	`fechaNacimiento`, `categoria_id`, `club_id`) 
VALUES ("Lauatro","Navarro","1998/2/2",3,3);

#ESPECIALIDADES
INSERT INTO `competencia_especialidad`( `nombre`, `descripcion`) 
VALUES ("Pulso","Modalidad sin boya");
INSERT INTO `competencia_especialidad`( `nombre`, `descripcion`) 
VALUES ("Libre","Modalidad con o sin boya");
INSERT INTO `competencia_especialidad`( `nombre`, `descripcion`) 
VALUES ("Balancin","Modalidad con boya obligatoria y en uso");