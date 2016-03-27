DELIMITER $$

DROP PROCEDURE  IF EXISTS uspAddUser $$


CREATE PROCEDURE uspAddUser (
   IN email NVARCHAR(100),
   IN loginName NVARCHAR(40),
   IN password NVARCHAR(40),
   IN firstName NVARCHAR(40), 
   IN lastName NVARCHAR(40),
   IN groupId varchar(36),
   IN userType INT)

BEGIN
  INSERT INTO User (UserId, Email, LoginName, PasswordHash, FirstName, LastName, GroupId, UserType) 
  VALUES (UUID(), email, loginName, SHA1(password), firstName, lastName, groupId, userType);
END $$

DELIMITER ;



