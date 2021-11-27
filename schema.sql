
CREATE DATABASE IF NOT EXISTS  Unites;

use Unites;

create table automate(
    id INT PRIMARY KEY AUTO_INCREMENT,
    unit_id INT NOT NULL ,
    num_automate tinyint not null,
    type_auto  VARCHAR(10)
);


create table fact_automate (
    id INT PRIMARY KEY AUTO_INCREMENT,
    automate_id VARCHAR(45),
    cuveTemp FLOAT,
    outsideTemp FLOAT,
    cuveMilkWeigth INT(11),
    finalProductWeight INT(11),
    ph FLOAT,
    kp tinyint(1),
    naCl Float,
    bactSalmo SMALLINT(3), 
    bactEcoli smallint(3),
    bactListeria smallint(3),
    date_bdd DATETIME,
    date_unit DATETIME
);

create table unit(
    id INT PRIMARY KEY AUTO_INCREMENT
);

Insert into unit (id) values (1) (2) (3) (4) (5);

DELIMITER //
FOR i IN 1..10
DO
    Insert into automate (unit_id,num_automate,type_auto)
    values(1,i,'default');
END FOR;
//
DELIMITER;