CREATE TABLE owed_tbl(
   owed_id INT NOT NULL AUTO_INCREMENT,
   owed_people_id INT NOT NULL,
   owed_bill_id INT NOT NULL,
   paid INT not null default 0,
   PRIMARY KEY ( owed_id )
);
