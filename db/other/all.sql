drop table if exists bill;

CREATE TABLE Bill(
   BillId varchar(36) NOT NULL UNIQUE, -- this is a guid
   Name NVARCHAR(100) NOT NULL,
   Description NVARCHAR(500),
   Amount FLOAT NOT NULL,
   DueDate DATE NOT NULL,
   BillIssuerId varchar(36) NOT NULL,
   BillPayeeId varchar(36) NOT NULL,
   Paid BOOLEAN NOT NULL,
   PaidDate DATETIME,
   PRIMARY KEY ( BillId )
);
drop table if exists ClientSID;

CREATE TABLE ClientSID(
   UserId varchar(36) NOT NULL , -- this is a guid
   SID varchar(36) NOT NULL,
   EntryTime datetime
);drop table if exists  Template;

CREATE TABLE Template(
   TemplateId varchar(36) NOT NULL UNIQUE, -- this is a guid
   Name NVARCHAR(100) NOT NULL,
   Description NVARCHAR(500),
   TemplateText NVARCHAR(10000),
   CreateDate DATETIME,
   Creator varchar(36) NOT NULL,
   PRIMARY KEY ( TemplateId )
);
drop table if exists User;

CREATE TABLE User(
   UserId varchar(36) NOT NULL UNIQUE, -- this is a guid
   Email NVARCHAR(100) NOT NULL UNIQUE,
   LoginName NVARCHAR(40),
   PasswordHash BINARY(40),
   FirstName NVARCHAR(40), 
   LastName NVARCHAR(40),
   GroupId varchar(36) NOT NULL,
   UserType INT,
   CONSTRAINT PK_User_UserID PRIMARY KEY (UserID )
);
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

DELIMITER $$

DROP PROCEDURE  IF EXISTS uspGETUserId $$


CREATE PROCEDURE uspGETUserId (
   IN isid varchar(36),
   OUT ouserId varchar(36))

BEGIN
  set ouserId := (select UserId from  ClientSID where  SID = isid);
END $$

DELIMITER ;


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

#people
# the default client id is 204de18f-ed4f-11e5-8824-8c89a5c59145

delete from User;
delete from Bill;

INSERT INTO User (UserId, Email, LoginName, PasswordHash, FirstName, LastName, GroupId, UserType)
  VALUES
  ('204de18f-ed4f-11e5-8824-8c89a5c59145', 'demoUser@gmail.com', 'demoUser', SHA1('demoPassword'), 'john', 'doe', '204de18f-ed4f-11e5-8824-8c89a5c59145', 1),
  ('2ea07995-ed52-11e5-8824-8c89a5c59145', 'client1@gmail.com', 'defaultLoginName', SHA1('defaultPassword'), 'client1', 'c1LastName', '204de18f-ed4f-11e5-8824-8c89a5c59145', 2),
  ('2ea07994-ed52-11e5-8824-8c89a5c59145', 'client2@gmail.com', 'defaultLoginName', SHA1('defaultPassword'), 'client2', 'c2LastName', '204de18f-ed4f-11e5-8824-8c89a5c59145', 2),
  ('2ea07993-ed52-11e5-8824-8c89a5c59145', 'client3@gmail.com', 'defaultLoginName', SHA1('defaultPassword'), 'client3', 'c3LastName', '204de18f-ed4f-11e5-8824-8c89a5c59145', 2),
  ('2ea07992-ed52-11e5-8824-8c89a5c59145', 'client4@gmail.com', 'defaultLoginName', SHA1('defaultPassword'), 'client4', 'c4LastName', '204de18f-ed4f-11e5-8824-8c89a5c59145', 2);

#bills bill 1 has already being paid
INSERT INTO Bill (BillId, Name, Description, Amount, DueDate,BillIssuerId, BillPayeeId, Paid, paidDate)
    VALUES
    ('6ea07992-ed52-11e5-8824-8c89a5c59145', 'bill1', 'billDesc1', 10, DATE_SUB(NOW(),INTERVAL 1 DAY), '204de18f-ed4f-11e5-8824-8c89a5c59145', '2ea07995-ed52-11e5-8824-8c89a5c59145',true,'1000-01-01 00:00:00'),
    ('3ea07992-ed52-11e5-8824-8c89a5c59145', 'bill2', 'billDesc2', 11, DATE_ADD(NOW(),INTERVAL 2 DAY), '204de18f-ed4f-11e5-8824-8c89a5c59145', '2ea07994-ed52-11e5-8824-8c89a5c59145',false,'1000-01-01 00:00:00'),
    ('4ea07992-ed52-11e5-8824-8c89a5c59145', 'bill3', 'billDesc3', 12, DATE_ADD(NOW(),INTERVAL 3 DAY), '204de18f-ed4f-11e5-8824-8c89a5c59145', '2ea07993-ed52-11e5-8824-8c89a5c59145',false,'1000-01-01 00:00:00'),
    ('5ea07992-ed52-11e5-8824-8c89a5c59145', 'bill4', 'billDesc4', 13, DATE_ADD(NOW(),INTERVAL 4 DAY), '204de18f-ed4f-11e5-8824-8c89a5c59145', '2ea07992-ed52-11e5-8824-8c89a5c59145',false,'1000-01-01 00:00:00');



set @modalText1 = '
<button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal">Open Modal</button>
<!-- Modal -->
<div id="myModal" class="modal fade" role="dialog">
  <div class="modal-dialog">
    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">Modal Header</h4>
      </div>
      <div class="modal-body">
        <p>Some text in the modal.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>';

set @modalText2 = '
<button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal">Open Modal</button>
<!-- Modal -->
<div id="myModal" class="modal fade" role="dialog">
  <div class="modal-dialog">
    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">Modal Header</h4>
      </div>
      <div class="modal-body">
        <p>Some text in the modal.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>';

## insert sample templates
INSERT INTO Template (TemplateId, Name, Description, TemplateText, CreateDate, Creator)
  VALUES
  ('1ea07992-ed52-11e5-8824-8c89a5c59145', 'SampleTemplate1', 'SampleTemplateDesc1', @modalText1, NOW(), '204de18f-ed4f-11e5-8824-8c89a5c59145'),
  ('2ea07992-ed52-11e5-8824-8c89a5c59145', 'SampleTemplate2', 'SampleTemplateDesc2', @modalText2, NOW(), '204de18f-ed4f-11e5-8824-8c89a5c59145')


