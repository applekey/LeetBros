CREATE TABLE owed_tbl(
   owed_id INT NOT NULL AUTO_INCREMENT,
   owed_people_id INT NOT NULL,
   owed_bill_id INT NOT NULL,
   PRIMARY KEY ( owed_people_id )
);
