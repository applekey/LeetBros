create View unpaidBills as
(
    select 
        pt.people_name as personName, 
        bt.bill_name as billName, 
        pt.people_email as email, 
        bt.bill_date as dueDate,
        bt.bill_description as billDesc,
        bt.bill_amount as amount
    from owed_tbl ot 
    join people_tbl pt on ot.owed_people_id = pt.people_id 
    join bill_tbl bt on ot.owed_bill_id = bt.bill_id 
    where ot.paid = false
);
