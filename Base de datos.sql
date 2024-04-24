create database	farm_to_cell;
use farm_to_cell;

CREATE TABLE registro_personas (
 id_persona INT(11) NOT NULL  PRIMARY KEY  AUTO_INCREMENT,
  Nombre_persona VARCHAR(45) NOT NULL,
  Apellido_person VARCHAR(45) NOT NULL,
  Celular INT NOT NULL,
  Dirección VARCHAR(45) NOT NULL,
  Email varchar(45) not null,
  Contraseña VARCHAR(45) NOT NULL
 );
select * from registro_personas;
/*ALTER TABLE `farm_to_cell`.`registro personas` 
CHANGE COLUMN `id_persona` `id_persona` INT(11) NOT NULL AUTO_INCREMENT ;*/

CREATE TABLE registro_producto (
  id_producto INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  Nombre_producto VARCHAR(45) NOT NULL,
  Cantidad VARCHAR(45) NOT NULL,
  Precio VARCHAR(45) NOT NULL,
  Descripción VARCHAR(70) NOT NULL,
  Imagen_prodcuto BLOB NOT NULL
   );
   
   select * from registro_producto;
   
  /*ALTER TABLE `farm_to_cell`.`registro producto` 
CHANGE COLUMN `id_producto` `id_producto` INT(11) NOT NULL AUTO_INCREMENT ;*/

CREATE TABLE inventario (
  id_Inventario INT NOT NULL PRIMARY KEY ,
  Cantidad_disp INT NOT NULL,
  Fecha_exp DATE NOT NULL,
  Personita int not null,
  Productito int not null,
  foreign key (Personita) references registro_personas(id_persona),
  foreign key (Productito) references registro_producto(id_producto)
);

select * from inventario;

show tables;
