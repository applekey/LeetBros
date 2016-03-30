drop table if exists  Template;

CREATE TABLE Template(
   TemplateId varchar(36) NOT NULL UNIQUE, -- this is a guid
   Name NVARCHAR(100) NOT NULL,
   Description NVARCHAR(500),
   TemplateText NVARCHAR(10000),
   CreateDate DATETIME,
   Creator varchar(36) NOT NULL,
   PRIMARY KEY ( TemplateId )
);
