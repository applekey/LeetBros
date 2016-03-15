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
	