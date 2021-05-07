-- Given CREATE TABLE statements to start your database

--==========================================================================

Create Table Caregivers(
	CaregiverId int IDENTITY PRIMARY KEY,
	CaregiverName varchar(50),
	PhoneNumber int NOT NULL,
	UserPassword varchar(20)
);

--==========================================================================

Create Table AppointmentStatusCodes(
	StatusCodeId int PRIMARY KEY,
	StatusCode   varchar(30)
);

--Insert values into Appointment Status Codes
INSERT INTO AppointmentStatusCodes (statusCodeId, StatusCode)
	VALUES (0, 'Open');
INSERT INTO AppointmentStatusCodes (statusCodeId, StatusCode)
	VALUES (1, 'OnHold');
INSERT INTO AppointmentStatusCodes (statusCodeId, StatusCode)
	VALUES (2, 'Scheduled');
INSERT INTO AppointmentStatusCodes (statusCodeId, StatusCode)
	VALUES (3, 'Completed');
INSERT INTO AppointmentStatusCodes (statusCodeId, StatusCode)
	VALUES (4, 'Missed');

--==========================================================================

--Create caregiver schedule table
Create Table CareGiverSchedule(
	 int Identity PRIMARY KEY, 
	CaregiverId int DEFAULT 0 NOT NULL
		CONSTRAINT FK_CareGiverScheduleCaregiverId FOREIGN KEY (caregiverId)
			REFERENCES Caregivers(CaregiverId),
	WorkDay date,
	SlotTime time,
	SlotHour int DEFAULT 0 NOT NULL,
	SlotMinute int DEFAULT 0 NOT NULL,
	SlotStatus int  DEFAULT 0 NOT NULL
		CONSTRAINT FK_CaregiverStatusCode FOREIGN KEY (SlotStatus) 
		     REFERENCES AppointmentStatusCodes(StatusCodeId),
	VaccineAppointmentId int DEFAULT 0 NOT NULL,
	FOREIGN KEY (VaccineAppointmentID) REFERENCES VaccineAppointments(VaccineAppointmentId)
);

--==========================================================================

-- Create patients table
Create Table Patients(
	PatientId int PRIMARY KEY,
	PatientName varchar(50),
	PhoneNumber int NOT NULL,
	UserPassword varchar(20),
	DosesGiven int DEFAULT 0 NOT NULL
);

--==========================================================================

-- Create Vaccine appointments table
Create Table VaccineAppointments(
	VaccineAppointmentId int PRIMARY KEY,
	PatientId int,
	VaccineId int,
	FOREIGN KEY (PatientId) REFERENCES Patients(PatientId),
	FOREIGN KEY (VaccineId) REFERENCES Vaccines(VaccineId)
);

--==========================================================================

-- Create Vaccines table
Create Table Vaccines(
	VaccineId int PRIMARY KEY,
	ManufactererName varchar(50),
	DosesNeeded int NOT NULL,
	DosesInStock int DEFAULT 0 NOT NULL,
	DosesReserved int DEFAULT 0 NOT NULL,
);

 
-- Additional helper code for your use if needed

-- --- Drop commands to restructure the DB
-- Drop Table CareGiverSchedule
-- Drop Table AppointmentStatusCodes
-- Drop Table Caregivers
-- Go

-- --- Commands to clear the active database Tables for unit testing
-- Truncate Table CareGiverSchedule
-- DBCC CHECKIDENT ('CareGiverSchedule', RESEED, 0)
-- Delete From Caregivers
-- DBCC CHECKIDENT ('Caregivers', RESEED, 0)
-- GO
