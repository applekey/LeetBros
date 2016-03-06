CREATE TABLE Bill(
   BillId varchar(36) NOT NULL UNIQUE, -- this is a guid
   Name NVARCHAR(100) NOT NULL,
   Description NVARCHAR(500),
   Amount FLOAT NOT NULL,
   DueDate DATE NOT NULL,
   BillIssuerId varchar(36) NOT NULL,
   BillPayeeId varchar(36) NOT NULL,
   PRIMARY KEY ( BillId )
);
