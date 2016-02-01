CREATE TABLE people_tbl(
   people_id INT NOT NULL AUTO_INCREMENT,
   people_name NVARCHAR(100) NOT NULL,
   people_email NVARCHAR(100) NOT NULL UNIQUE,
   PRIMARY KEY ( people_id )
);

--ALTER TABLE people_tbl
--	modify people_email nvarchar(100) not null unique
