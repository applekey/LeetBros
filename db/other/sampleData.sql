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


