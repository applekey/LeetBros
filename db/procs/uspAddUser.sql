DELIMITER $$

DROP PROCEDURE  IF EXISTS uspAddUser $$


CREATE PROCEDURE uspAddUser (
   IN email NVARCHAR(100),
   IN loginName NVARCHAR(40),
   IN password NVARCHAR(40),
   IN firstName NVARCHAR(40), 
   IN lastName NVARCHAR(40),
   IN userType INT)

BEGIN
  INSERT INTO User (UserId, Email, LoginName, PasswordHash, FirstName, LastName, UserType) 
  VALUES (UUID(), email, loginName, SHA1(password), firstName, lastName, userType);
END $$

DELIMITER ;



