DELIMITER $$
DROP PROCEDURE  IF EXISTS uspIfUserExists;

CREATE PROCEDURE uspIfUserExists (
    IN pLogin NVARCHAR(50), 
    IN pPassword NVARCHAR(50),
    OUT userExist BOOL)

BEGIN
	IF EXISTS(select FirstName,LastName from user_tbl where LoginName = pLogin and PasswordHash = SHA1(pPassword) LIMIT 1) THEN
		SET userExist = 1;
	ELSE
		SET userExist = 0;
	END IF;
END$$

DELIMITER ;

