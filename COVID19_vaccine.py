import pymssql

class COVID19Vaccine:
    '''Adds the Vaccine to the DB'''
    def __init__(self, manufacName, days_between_doses, cursor):
        # Determine number of doses needed for each vaccine
        if manufacName == 'Pfizer-BioNTech' or manufacName == 'Moderna':
        	self.dosesNeeded = 2
        else:
        	self.dosesNeeded = 1
        
        self.sqltext = "INSERT INTO Vaccines (ManufactererName, DosesNeeded, DosesInStock, DosesReserved, DaysBetweenDoses) VALUES ('" 
        self.sqltext += manufacName + "', "
        self.sqltext += str(self.dosesNeeded) + ", "
        self.sqltest += str(self.dosesInStock) + ", "
        self.sqltest += str(self.dosesReserved) + ", "
        self.sqltext += str(days_between_doses) + ")"
        
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

        
        # try:
        #     cursor.execute(sqltext2)
        # except pymssql.Error as db_err:
        #     print("Database Programming Error in SQL Query processing for COVID19_Vaccine! ")
        #     print("Exception code: " + str(db_err.args[0]))
        #     if len(db_err.args) > 1:
        #         print("Exception message: " + db_err.args[1])
        #     print("SQL text that resulted in an Error: " + self.sqltext)
            
    
    def addDoses(manufacName, numberOfDosesAdded):
        '''Add doses to the vaccine inventory for a particular vaccine'''


    def ReserveDoses(manufacName):
        '''reserve the vaccine doses associated with a specific patient who is being scheduled for vaccine administration'''
        #get doses in stock and doses reserved
            self.getdosesInStock = "SELECT DosesInStock FROM Vaccines WHERE ManufactererName = "
            self.getdosesInStock += manufacName
            self.getdosesReserved = "SELECT DosesReserved FROM Vaccines WHERE ManufactererName = "
            self.getdosesInStock += manufacName

        if manufacName == 'Pfizer-BioNTech' or 'Moderna':
            #check if there are enough in stock and reserve
            if self.getdosesInStock >= 2:
                self.getdosesReserved += 2
                self.getdosesInStock = getdosesInStock - 2
            else:
                print("Not enough vaccines in stock!")
        else:
            #check if there are enough in stock and reserve
            if self.getdosesInStock >= 1:
                self.getdosesReserved += 1
                self.getdosesInStock = getdosesInStock - 1
            else:
                print("Not enough vaccines in stock!")






        
