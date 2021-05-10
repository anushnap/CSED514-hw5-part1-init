import pymssql

class COVID19Vaccine:
    '''Adds the Vaccine to the DB'''
    def __init__(self, manufacName, days_between_doses, cursor):
        self.sqltext = "INSERT INTO Vaccines (ManufactererName) VALUES ('" + str(manufacName) + "')"
        self.VaccineId = 0
        try: 
            cursor.execute(self.sqltext)
            cursor.connection.commit()
            cursor.execute("SELECT @@IDENTITY AS 'Identity'; ")
            _identityRow = cursor.fetchone()
            self.VaccineId = _identityRow['Identity']
            # cursor.connection.commit()
            print('Query executed successfully. Vaccine : ' + manufacName 
            +  ' added to the database using Vaccine ID = ' + str(self.VaccineId))
        except pymssql.Error as db_err:
            print("Database Programming Error in SQL Query processing for Vaccines! ")
            print("Exception code: " + str(db_err.args[0]))
            if len(db_err.args) > 1:
                print("Exception message: " + db_err.args[1])
            print("SQL text that resulted in an Error: " + self.sqltext)

        # Determine number of doses needed for each vaccine
        if manufacName == 'Pfizer-BioNTech' or manufacName == 'Moderna':
        	self.dosesNeeded = 2
        else:
        	self.dosesNeeded = 1

       	sqltext2 = ("INSERT INTO Vaccines (VaccineId, DosesNeeded, DaysBetweenDoses) VALUES (")
        sqltext2 += str(self.VaccineId) + ", " + str(self.dosesNeeded) + ", " + str(days_between_doses) + ")"
        # print(sqltext2)

        try:
            cursor.execute(sqltext2)
        except pymssql.Error as db_err:
            print("Database Programming Error in SQL Query processing for COVID19_Vaccine! ")
            print("Exception code: " + str(db_err.args[0]))
            if len(db_err.args) > 1:
                print("Exception message: " + db_err.args[1])
            print("SQL text that resulted in an Error: " + self.sqltext)
            
    
    def addDoses(VaccineId, numberOfDosesAdded):
        '''Add doses to the vaccine inventory for a particular vaccine'''
        pass

    def ReserveDoses(VaccineId, patientId):
        '''reserve the vaccine doses associated with a specific patient who is being scheduled for vaccine administration'''
        pass
