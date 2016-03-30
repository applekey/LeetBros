DELIMITER $$

DROP PROCEDURE  IF EXISTS uspAddTemplate;

CREATE PROCEDURE uspAddTemplate (
   In name NVARCHAR(100),
   In description NVARCHAR(500),
   In templateText NVARCHAR(10000),
   In createDate DATETIME,
   In creator varchar(36))

BEGIN
    INSERT INTO Template (TemplateId, Name, Description, TemplateText, CreateDate,Creator) 
    VALUES (UUID(), name, description, templateText, createDate, creator);
END $$

DELIMITER ;

  