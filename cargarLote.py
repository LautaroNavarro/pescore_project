# import pymysql
# conn = pymysql.connect(host='localhost', user='root', passwd='', db='pescore')
# cur = conn.cursor()
# consultas = ["USE Pescore;",
# "TRUNCATE TABLE `competencia_categoria`;",
# "TRUNCATE TABLE `competencia_club`;",
# "TRUNCATE TABLE `competencia_participante`;",
# "TRUNCATE TABLE `competencia_especialidad`;",
# "TRUNCATE TABLE `competencia_campeonato`;",
# "TRUNCATE TABLE `competencia_campeonato_participantes`;",
# "TRUNCATE TABLE `competencia_torneo`;",
# "TRUNCATE TABLE `competencia_tarjeta`;",
# "INSERT INTO `competencia_categoria`(`nombre`) VALUES ('Seniors');",
# "INSERT INTO `competencia_categoria`(`nombre`) VALUES ('Damas');",
# "INSERT INTO `competencia_categoria`(`nombre`) VALUES ('Mayores Promocionales');",
# "INSERT INTO `competencia_categoria`(`nombre`) VALUES ('Mayores Federados');",
# "INSERT INTO `competencia_categoria`(`nombre`) VALUES ('Juveniles');",
# "INSERT INTO `competencia_club`(`nombre`, `abreviacion`) VALUES ('El Pelicano','PEL');",
# "INSERT INTO `competencia_club`(`nombre`, `abreviacion`) VALUES ('Rivadavia','RIV');",
# "INSERT INTO `competencia_club`(`nombre`, `abreviacion`) VALUES ('Medrano','MED');",

# "INSERT INTO `competencia_participante`(`nombre`,`apellido`, `fechaNacimiento`, `categoria_id`, `club_id`) VALUES ('Martin','Perez','1998/8/13',1,1);",
# "INSERT INTO `competencia_participante`(`nombre`, `apellido`, 	`fechaNacimiento`, `categoria_id`, `club_id`) VALUES ('Maximiliano','Sanchez','1998/2/2',2,2);",
# "INSERT INTO `competencia_participante`(`nombre`, `apellido`, 	`fechaNacimiento`, `categoria_id`, `club_id`) VALUES ('Lauatro','Navarro','1998/2/2',3,3);",

# "INSERT INTO `competencia_especialidad`( `nombre`, `descripcion`) VALUES ('Pulso','Modalidad sin boya');",
# "INSERT INTO `competencia_especialidad`( `nombre`, `descripcion`) VALUES ('Libre','Modalidad con o sin boya');",
# "INSERT INTO `competencia_especialidad`( `nombre`, `descripcion`) VALUES ('Balancin','Modalidad con boya obligatoria y en uso');",

# "INSERT INTO `competencia_campeonato`(`fecha`, `nombre`, `cantidadPescadores`, `cantidadClubes`) VALUES ('2018/2/2','Campeonato Mundial', 3 ,3);",
# "INSERT INTO `competencia_campeonato_participantes`(`campeonato_id`, `participante_id`) VALUES (1,1);",
# "INSERT INTO `competencia_campeonato_participantes`(`campeonato_id`, `participante_id`) VALUES (1,2);",
# "INSERT INTO `competencia_campeonato_participantes`(`campeonato_id`, `participante_id`) VALUES (1,3);",

# "INSERT INTO `competencia_campeonato`(`fecha`, `nombre`, `cantidadPescadores`, `cantidadClubes`) VALUES ('2017/3/1','Mega Camp', 3 ,3);",
# "INSERT INTO `competencia_campeonato_participantes`(`campeonato_id`, `participante_id`) VALUES (2,1);",
# "INSERT INTO `competencia_campeonato_participantes`(`campeonato_id`, `participante_id`) VALUES (2,2);",
# "INSERT INTO `competencia_campeonato_participantes`(`campeonato_id`, `participante_id`) VALUES (2,3);",

# "INSERT INTO `competencia_torneo`(`fecha`, `campeonato_id`, `club_id`, `especialidad_id`) VALUES ('2017/5/5',2,1,1);",
# "INSERT INTO `competencia_torneo`(`fecha`, `campeonato_id`, `club_id`, `especialidad_id`) VALUES ('2017/5/10',2,1,2);",
# "INSERT INTO `competencia_torneo`(`fecha`, `campeonato_id`, `club_id`, `especialidad_id`) VALUES ('2017/5/7',2,1,3);"
# ]
# try:
# 	for consulta in consultas:
# 		cur.execute(consulta)
# 		print (consulta)
# 	print ("Carga de lote de prueba exitosa")
# except Exception as e:
# 	print ("Carga de lote de prueba fallida")

