DELIMITER $$

DROP PROCEDURE  IF EXISTS uspCreateBill;

CREATE PROCEDURE uspCreateBill (
   IN name NVARCHAR(100),
   IN description NVARCHAR(500),
   IN amount FLOAT,
   IN dueDate DATE,
   IN billIssuerId varchar(36),
   IN billPayeeId varchar(36),
   IN paid BOOLEAN,
   IN paidDate DATETIME)

BEGIN
    INSERT INTO Bill (BillId, Name, Description, Amount, DueDate,BillIssuerId, BillPayeeId, paid, PaidDate) 
    VALUES(UUID(), name, description, amount, dueDate, billIssuerId, billPayeeId, paid, paidDate) ;
END $$

DELIMITER ;

