import pymysql

class MySQL:

    def __init__(self, IP_DNS, USER, PASSWORD, BD_NAME, PORT):
        self.IP_DNS = IP_DNS
        self.USER = USER
        self.PASSWORD = PASSWORD
        self.BD_NAME = BD_NAME
        self.PORT = PORT
        self.SQL_ALCHEMY = 'mysql+pymysql://' + self.USER + ':' + self.PASSWORD + '@' + self.IP_DNS + ':' + str(self.PORT) + '/' + self.BD_NAME
        # 'mysql+pymysql://user:password@91.76.54.33:20001/apr_july_2021_tb'
    def connect(self):
        # Open database connection
        self.db = pymysql.connect(host=self.IP_DNS,
                                  user=self.USER, 
                                  password=self.PASSWORD, 
                                  database=self.BD_NAME, 
                                  port=self.PORT)
        # prepare a cursor object using cursor() method
        self.cursor = self.db.cursor()
        print("Connected to MySQL server [" + self.BD_NAME + "]")
        return self.db

    def close(self):
        # disconnect from server
        self.db.close()
        print("Close connection with MySQL server [" + self.BD_NAME + "]")
    
    def execute_interactive_sql(self, sql, delete=False):
        """ NO SELECT """
        result = 0
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Commit your changes in the database
            self.db.commit()
            print("Executed \n\n" + str(sql) + "\n\n successfully")
            result = 1
        except Exception as error:
            print(error)
            # Rollback in case there is any error
            self.db.rollback()
        return result
        
    def execute_get_sql(self, sql):
        """SELECT"""
        results = None
        print("Executing:\n", sql)
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = self.cursor.fetchall()
        except Exception as error:
            print(error)
            print ("Error: unable to fetch data")
        
        return results

    def generate_insert_into_people_sql(self, to_insert):
        """
        This must be modified according to the table structure
        """

        autonomous_communities = to_insert[0]
        year = to_insert[1]
        GDP = to_insert[2]
        Population = to_insert[3]
        GDPpercapita = to_insert[4]
        Domestic_WasteWheelie =  to_insert[5]
        Bulk =  to_insert[6]
        metallics =  to_insert[7]
        glass =  to_insert[8]
        Paper  =  to_insert[9]
        Plastics =  to_insert[10]
        Wood =  to_insert[11]
        Textile =  to_insert[12]
        Electrical =  to_insert[13]
        Battery =  to_insert[14]
        Animal =  to_insert[15]
        Mixed_packaging =  to_insert[16]
        Sludge =  to_insert[17]
        Construction =  to_insert[18]
        Others =  to_insert[19]
        Totalmixed  =  to_insert[20]
        Totalseparately =  to_insert[21]
        TotalWaste =  to_insert[22]
        Recycling =  to_insert[23]
        Recovered =  to_insert[24]
        Composting_ford =  to_insert[25]
        Compostingdigestion =  to_insert[26]
        Incinerated =  to_insert[27]
        Landfillrejects =  to_insert[28]
        Withoutpretreatment =  to_insert[29]
        TotalWastedisposal =  to_insert[30]
        Totaltnday =  to_insert[31]
        PerCapita_coll = to_insert[32]
        Processed_waste =  to_insert[33]
        NotProcessed_waste =  to_insert[34]

        
        sql = """INSERT INTO MaryCruz_Meza
        (MOMENTO, AUTONOMOUS_COMMUNITIES, YEAR, GDP, POPULATION, GDPPERCAPITA, DOMESTIC_WASTEWHEELIE, BULK, METALLICS, GLASS, PAPER, PLASTICS, WOOD, TEXTILE, ELECTRICAL, BATTERY, ANIMAL, MIXED_PACKAGING, SLUDGE,
        CONSTRUCTION, OTHERS, TOTALMIXED, TOTALSEPARATELY, TOTALWASTE, RECYCLING, RECOVERED, COMPOSTING_FORD, COMPOSTINGDIGESTION, INCINERATED, LANDFILLREJECTS, WITHOUTPRETREATMENT, TOTALWASTEDISPOSAL,
        TOTALTNDAY, PERCAPITA_COLL, PROCESSED_WASTE, NOTPROCESSED_WASTE)
            VALUES
            (NOW(), '""" + autonomous_communities + """', '""" + year + """', '""" + GDP + """', '""" + Population + """', '""" + GDPpercapita + """', '""" + Domestic_WasteWheelie + """','""" + Bulk + """', '""" + metallics + """', '""" + glass + """', 
            '""" + Paper + """', '""" + Plastics + """', '""" + Wood + """', '""" + Textile + """', '""" + Electrical + """', '""" + Textile + """', '""" + Battery + """', '""" + Animal + """', '""" + Mixed_packaging + """', '""" + Sludge + """',  
            '""" + Construction + """', '""" + Others + """', '""" + Totalmixed + """', '""" + Totalseparately + """', '""" + TotalWaste + """', '""" + Recycling + """', '""" + Recovered + """', , '""" + Composting_ford + """', '""" + Compostingdigestion + """',
            '""" + Incinerated + """', '""" + Landfillrejects + """', '""" + Withoutpretreatment + """', '""" + TotalWastedisposal + """', '""" + Totaltnday + """', '""" + Processed_waste + """', '""" + PerCapita_coll + """', '""" + NotProcessed_waste + """')"""

        sql = sql.replace("\n", "").replace("            ", " ")
        return sql
                    
             
        
       