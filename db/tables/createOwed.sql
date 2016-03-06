CREATE TABLE owed_tbl(
   owed_id INT NOT NULL AUTO_INCREMENT,
   owed_people_id INT NOT NULL,
   owed_bill_id INT NOT NULL,
   paid bool not null default false,
   userId CHAR(16) NOT NULL,
   PRIMARY KEY ( owed_id )
);
