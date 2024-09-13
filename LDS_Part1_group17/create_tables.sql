
---CONSTRAINT [FK_Answers_Subject] FOREIGN KEY ([subjectid]) REFERENCES [Group_17].[Subject]([subjectid])
USE [Group_17_DB]
GO

if object_id('answers') is null
	CREATE TABLE [Group_17].[answers](
		[answerid] [int] NOT NULL,
		[questionid] [int] NOT NULL,
		[userid] [int] NOT NULL,
		[organizationid] [int] NOT NULL,
		[dateid] [int] NOT NULL,
		[subjectid] [nvarchar] NOT NULL,
		[answer_value] [tinyint] NOT NULL,
		[correct_answer] [tinyint] NOT NULL,
		[iscorrect] [tinyint] NOT NULL,
		[confidence] [int] NOT NULL,
	CONSTRAINT [PK_answers] PRIMARY KEY CLUSTERED ([answerid] ASC),
	
	); 

if object_id('subject') is null
	CREATE TABLE [Group_17].[subject](
		[subjectid] [nvarchar] NOT NULL,
		[description] [nvarchar] NOT NULL,
	    CONSTRAINT [PK_subject] PRIMARY KEY CLUSTERED ([subjectid] ASC),
	);

if object_id('organization') is null
	CREATE TABLE [Group_17].[organization](
		[organizationid] [int] NOT NULL,
		[groupid] [int] NOT NULL,
		[quizid] [int] NOT NULL,
		[schemeofworkid] [int] NOT NULL,
	    CONSTRAINT [PK_organization] PRIMARY KEY CLUSTERED ([organizationid] ASC),
	    
		);
	
if object_id('date') is null
	CREATE TABLE [Group_17].[date](
		[dateid] [int] NOT NULL,
		[date] [nvarchar] NOT NULL,
		[day] [int] NOT NULL,
		[month] [int] NOT NULL,
		[year] [int] NOT NULL,
		[quarter] [nvarchar] NOT NULL,
	    CONSTRAINT [PK_date] PRIMARY KEY CLUSTERED ([dateid] ASC),
	    
		);
if object_id('users') is null
	CREATE TABLE [Group_17].[users](
		[userid] [int] NOT NULL,
		[dateofbirthid] [int] NOT NULL,
		[geoid] [int] NOT NULL,
		[gender] [tinyint] NOT NULL,
	    CONSTRAINT [PK_users] PRIMARY KEY CLUSTERED ([userid] ASC),
	   
		);

if object_id('geography') is null
	CREATE TABLE [Group_17].[geography](
		[geoid] [int] NOT NULL,
		[region] [nvarchar] NOT NULL,
		[country_name] [nvarchar] NOT NULL,
		[continent] [nvarchar] NOT NULL,
	    CONSTRAINT [PK_geography] PRIMARY KEY CLUSTERED ([geoid] ASC),
	    
		);