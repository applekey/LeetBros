#people
# the default client id is 204de18f-ed4f-11e5-8824-8c89a5c59145

INSERT INTO User (UserId, Email, LoginName, PasswordHash, FirstName, LastName, GroupId, UserType)
  VALUES
  ('204de18f-ed4f-11e5-8824-8c89a5c59145', 'demoUser@gmail.com', 'demoUser', SHA1('demoPassword'), 'john', 'doe', '204de18f-ed4f-11e5-8824-8c89a5c59145', 1),
  ('2ea07995-ed52-11e5-8824-8c89a5c59145', 'client1@gmail.com', 'defaultLoginName', SHA1('defaultPassword'), 'client1', 'c1LastName', '204de18f-ed4f-11e5-8824-8c89a5c59145', 2),
  ('2ea07994-ed52-11e5-8824-8c89a5c59145', 'client2@gmail.com', 'defaultLoginName', SHA1('defaultPassword'), 'client2', 'c2LastName', '204de18f-ed4f-11e5-8824-8c89a5c59145', 2),
  ('2ea07993-ed52-11e5-8824-8c89a5c59145', 'client3@gmail.com', 'defaultLoginName', SHA1('defaultPassword'), 'client3', 'c3LastName', '204de18f-ed4f-11e5-8824-8c89a5c59145', 2),
  ('2ea07992-ed52-11e5-8824-8c89a5c59145', 'client4@gmail.com', 'defaultLoginName', SHA1('defaultPassword'), 'client4', 'c4LastName', '204de18f-ed4f-11e5-8824-8c89a5c59145', 2);

#bills
INSERT INTO Bill (BillId, Name, Description, Amount, DueDate,BillIssuerId, BillPayeeId)
    VALUES
    ('6ea07992-ed52-11e5-8824-8c89a5c59145', 'bill1', 'billDesc1', 10, DATE_ADD(NOW(),INTERVAL 1 DAY), '204de18f-ed4f-11e5-8824-8c89a5c59145', '2ea07995-ed52-11e5-8824-8c89a5c59145'),
    ('3ea07992-ed52-11e5-8824-8c89a5c59145', 'bill2', 'billDesc2', 11, DATE_ADD(NOW(),INTERVAL 2 DAY), '204de18f-ed4f-11e5-8824-8c89a5c59145', '2ea07994-ed52-11e5-8824-8c89a5c59145'),
    ('4ea07992-ed52-11e5-8824-8c89a5c59145', 'bill3', 'billDesc3', 12, DATE_ADD(NOW(),INTERVAL 3 DAY), '204de18f-ed4f-11e5-8824-8c89a5c59145', '2ea07993-ed52-11e5-8824-8c89a5c59145'),
    ('5ea07992-ed52-11e5-8824-8c89a5c59145', 'bill4', 'billDesc4', 13, DATE_ADD(NOW(),INTERVAL 4 DAY), '204de18f-ed4f-11e5-8824-8c89a5c59145', '2ea07992-ed52-11e5-8824-8c89a5c59145');
