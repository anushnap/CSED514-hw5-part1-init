import pymssql

class COVID19Vaccine:
    '''Adds the Vaccine to the DB'''
    def __init__(self, manufacName, days_between_doses, dosesInStock, dosesReserved, cursor):
        # Determine number of doses needed for each vaccine
        if manufacName == 'Pfizer-BioNTech' or manufacName == 'Moderna':
        	self.dosesNeeded = 2
        else:
        	self.dosesNeeded = 1
        
        self.sqltext = "INSERT INTO Vaccines (ManufactererName, DosesNeeded, DosesInStock, DosesReserved, DaysBetweenDoses) VALUES ('" 
        self.sqltext += manufacName + "', "
        self.sqltext += str(self.dosesNeeded) + ", "
        self.sqltext += str(dosesInStock) + ", "
        self.sqltext += str(dosesReserved) + ", "
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
            
    
    def addDoses(manufacName, numberofDosesAdded, cursor):
        '''Add doses to the vaccine inventory for a particular vaccine'''
        sqltext = "UPDATE Vaccines SET DosesInStock = DosesInStock + "
        sqltext += str(numberofDosesAdded)
        sqltext += " WHERE ManufactererName = '"
        sqltext += str(manufacName) + "'"
        
        try: 
            cursor.execute(sqltext)
            cursor.connection.commit()
            print("Query executed successfully.")
        except pymssql.Error as db_err:
            print("Database Programming Error in SQL Query processing for Vaccines! ")
            print("Exception code: " + str(db_err.args[0]))
            if len(db_err.args) > 1:
                print("Exception message: " + db_err.args[1])
            print("SQL text that resulted in an Error: " + sqltext)


    def ReserveDoses(manufacName):
        '''reserve the vaccine doses associated with a specific patient who is being scheduled for vaccine administration'''
        sqltext1 = "SELECT DosesInStock, DosesReserved FROM Vaccines WHERE ManufactererName = '"
        sqltext1 += str(manufacName) + "'"
        
        #get doses in stock and doses reserved
        try: 
            cursor.execute(sqltext1)
            rows = cursor.fetchall()
            doses_in_stock = 0
            doses_reserved = 0
            
            for row in rows:
                doses_in_stock += row['DosesInStock']
                doses_reserved += row['DosesReserved']
            
            print("Query executed successfully.")
        except pymssql.Error as db_err:
            print("Database Programming Error in SQL Query processing for ReserveDoses")
            print("Exception code: " + str(db_err.args[0]))
            if len(db_err.args) > 1:
                print("Exception message: " + db_err.args[1])
            print("SQL text that resulted in an Error: " + sqltext)

        if manufacName == 'Pfizer-BioNTech' or 'Moderna':
            #check if there are enough in stock and reserve
            if doses_in_stock >= 2:
                doses_reserved += 2
                doses_in_stock -= 2
            elif doses_in_stock == 1:
                doses_reserved += 1
                doses_in_stock -= 1
                print("WARNING: STOCK LOW. ONLY ONE DOSE RESERVED")
            else:
                print("WARNING: Not enough vaccines in stock!")
        else:
            #check if there are enough in stock and reserve
            if doses_in_stock >= 1:
                doses_reserved += 1
                doses_in_stock -= 1
            else:
                print("WARNING: Not enough vaccines in stock!")
        
        sqltext2 = "UPDATE VACCINES SET DosesInStock = "
        sqltext2 += str(doses_in_stock) + ", DosesReserved = "
        sqltext2 += str(doses_reserved) + " WHERE ManufactererName = '"
        sqltext2 += manufacName + "'"

        try: 
            cursor.execute(sqltext2)
            cursor.connection.commit()
            print("Query executed successfully.")
        except pymssql.Error as db_err:
            print("Database Programming Error in SQL Query processing for ReserveDoses! ")
            print("Exception code: " + str(db_err.args[0]))
            if len(db_err.args) > 1:
                print("Exception message: " + db_err.args[1])
            print("SQL text that resulted in an Error: " + sqltext)