DELIMITER $$

DROP PROCEDURE  IF EXISTS uspAddUser;


CREATE PROCEDURE uspAddUser (
    IN pLogin NVARCHAR(50), 
    IN pPassword NVARCHAR(40), 
    IN pFirstName NVARCHAR(40), 
    IN pLastName NVARCHAR(40))

BEGIN
    INSERT INTO user_tbl (LoginName, PasswordHash, FirstName, LastName) VALUES(pLogin, SHA1(pPassword), pFirstName, pLastName);
END $$

DELIMITER ;


