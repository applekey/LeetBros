CREATE TABLE bill_tbl(
   bill_id INT NOT NULL AUTO_INCREMENT,
   bill_name NVARCHAR(100) NOT NULL,
   bill_description NVARCHAR(500),
   bill_amount FLOAT,
   bill_date DATE,
   PRIMARY KEY ( bill_id )
);
