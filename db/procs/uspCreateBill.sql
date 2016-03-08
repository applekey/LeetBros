DELIMITER $$

DROP PROCEDURE  IF EXISTS uspCreateBill;

CREATE PROCEDURE uspCreateBill (
   IN name NVARCHAR(100),
   IN description NVARCHAR(500),
   IN amount FLOAT,
   IN dueDate DATE,
   IN billIssuerId varchar(36),
   IN billPayeeId varchar(36),
   OUT billId varchar(36), )


BEGIN
	SET @billId = UUID();

    INSERT INTO Bill (BillId, Name, Description, Amount, DueDate,BillIssuerId, BillPayeeId) 
    VALUES(@billId, name, description, amount, dueDate, billIssuerId, billPayeeId) ;
END $$

DELIMITER ;

