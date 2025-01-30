import math, random, datetime as dt

class Database:
    # class variable
    population = 0
    myDict = {}

    def __init__(self):
        pass

    def organize(self):
        dash = "-"
        for key, value in Database.myDict.items():
            dict_keys = ""
            for k, v in value.items():
                dict_keys += f"{k.title():<20}"
            print(f"{dict_keys}\n{dash*66}") 
            break
        for key, value in Database.myDict.items():
            dict_values = ""
            for k, v in value.items():
                dict_values += f"{v:<20}"
            print(f"{dict_values}\n{dash*66}")  

    def admitted(self, firstname):
        verify = False
        for key, value in Database.myDict.items():
            if (firstname.lower() == value["firstname"]):
                return value
        if verify != True:
            return False

    def details(self, firstname, data=False):
        info = self.admitted(firstname)
        if info:
            if (data=='age'):
                return info[data]
            elif (data=='gender'):
                return info[data]
            else: return info
        else:
            return 'Invalid student!'

    
                
 


class Students(Database):

    def __init__(self, fname, lname, age, gender):
        super().__init__()
        Database.population+=1
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.gender = gender
        self.info = {
            'firstname': fname,
            'lastname': lname,
            'age': age,
            'gender': gender
        }
        Database.myDict[Database.population] = self.info 
    
database = Database()
student1 = Students('jerry', 'aribidara', 19, 'm')
student2 = Students('wonder', 'aribidara', 18, 'm')
student3 = Students('comfort', 'aribidara', 16, 'f')
student4 = Students('joshua', 'jacob', 20, 'm')
student5 = Students('queen', 'elizabeth', 20, 'f')

print(database.details('queen'))