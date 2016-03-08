DELIMITER $$

DROP PROCEDURE  IF EXISTS uspAddUser;


CREATE PROCEDURE uspAddUser (
   IN email NVARCHAR(100),
   IN loginName NVARCHAR(40),
   IN password NVARCHAR(40),
   IN firstName NVARCHAR(40), 
   IN lastName NVARCHAR(40),
   IN userType INT,
   OUT userId varchar(36))

BEGIN
	SET @userId = UUID();
    INSERT INTO User (UserId, Email, LoginName, PasswordHash, FirstName, LastName, UserType) 
    VALUES (userId, email, loginName, SHA1(pPassword), firstName, lastName, userType);
END $$

DELIMITER ;



