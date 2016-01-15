CREATE TABLE owed_tbl(
   owed_id INT NOT NULL AUTO_INCREMENT,
   owed_people_id INT NOT NULL,
   owed_bill_id INT NOT NULL,
   paid bool not null default false,
   PRIMARY KEY ( owed_id )
);
