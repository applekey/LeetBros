DELIMITER $$

DROP PROCEDURE  IF EXISTS uspGETUserId $$


CREATE PROCEDURE uspGETUserId (
   IN isid varchar(36),
   OUT ouserId varchar(36))

BEGIN
  set ouserId := (select UserId from  ClientSID where  SID = isid);
END $$

DELIMITER ;


