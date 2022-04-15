--  Auto-generated SQL script #202204151918
INSERT INTO `movies-controll`.movies (id,tipo,nome,total_ep,atual_ep)
	VALUES (1,0,'Friends',10,1);
INSERT INTO `movies-controll`.movies (id,tipo,nome)
	VALUES (2,1,'Avengers');

select * from `movies-controll`.movies

#update `movies-controll`.movies set ultima_view = '2022-04-16' where `movies-controll`.movies.id = 1;

select * from `movies-controll`.movies

update `movies-controll`.movies set ultima_view = '2022-04-15'

--  Auto-generated SQL script #202204151932
INSERT INTO `movies-controll`.movies (id,tipo,nome)
	VALUES (2,1,'Avengers');
INSERT INTO `movies-controll`.movies (id,tipo,nome,total_ep,atual_ep)
	VALUES (3,0,'Todo Mundo Odeia o Chris',20,1);
INSERT INTO `movies-controll`.movies (id,tipo,nome)
	VALUES (4,1,'1917');
INSERT INTO `movies-controll`.movies (id,tipo,nome)
	VALUES (5,1,'300');
UPDATE `movies-controll`.movies
	SET id=1,tipo=1
	WHERE id=1;

delete from `movies-controll`.movies where id=4

INSERT INTO `movies-controll`.movies (id,tipo,nome)
	VALUES (4,1,'1917');

