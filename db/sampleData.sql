#people
insert into 
	people_tbl(people_name, people_email)
	values
	('shayak', 'shayak007@gmail.com'),
	('vincent', 'applekey@gmail.com');

#bill
insert into bill_tbl(bill_name, bill_description, bill_amount, bill_date)
	values
	('Luxurious bill', 'shayak\'s bill', 100.05, curdate()),
	('Hobo bill', 'vincent\'s bill', 10.05, curdate());

#owed
insert into owed_tbl(owed_people_id, owed_bill_id) 
	values
	(1, 1),
	(2, 2);
