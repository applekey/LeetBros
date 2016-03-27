CREATE TABLE ClientSID(
   UserId varchar(36) NOT NULL , -- this is a guid
   SID varchar(36) NOT NULL,
   EntryTime datetime NOT NULL DEFAULT NOW()
);