import file

# Count the registered dictionaries and increase the population to the number

# Anytime I save to a file, the dictionary should be emptied

class Database:
    # class variable
    database = {}
    population = len(database)


    def __init__(self, f):
        self.myfile = f
        self.my_dict = False
        # Read the file using the parameter in the class (Database) instance
        self.content = file.get(self.myfile)

    def sort_database_keys(self):
        obj2 = Database.database
        Database.database = {}
        num = 1
        for r, v in obj2.items():
            Database.database[num] = v
            num += 1
        return Database.database


    # If something is inside the file, let the database be equal to the file content which is a dictionary
    def update_database(self):
        import ast
        if self.content and Database.database=={}:
            self.sort_database_keys()
            # Convert file content to dictionaries
            content = ast.literal_eval(self.content)
            Database.database = content

            # Clear file after updating database with the file content so that when writing back to the file, it doesn't create duplicates
            file.clear_file(self.myfile)

            for c in content:
                Database.population += 1


    # Automatically adds new object to database dictionary in the class variable
    def save(self, data, f_name):
        self.my_dict = data
        Database.database[Database.population] = data

    # To verify if a user exists for authentication purposes
    def admitted(self, firstname):
        verify = False
        for key, value in Database.database.items():
            if (firstname.lower() == value["firstname"]):
                verify = True
                return value
        if verify != True:
            return False
        
    # Use code to register a new user through an object
    # To save registered names to file, use save_to_file() method
    # If what you want to save is less than or more than the parameters listed, just edit the register parameters and the 'info' dictionary
    # Every other thing will be taken care of by the code
    def register(self, fname, lname, mail, comment):
        self.update_database()
        verified = self.admitted(fname)
        if not verified:
            # Auto increment and saves if user firstname doesn't exist already
            Database.population+=1
            info = {
                'firstname': fname,
                'lastname': lname,
                'mail': mail,
                'comment': comment
            }
            self.save(info, self.myfile)
        else:
            print(fname.title() + ' already taken!')

    # Update user's data
    def update(self, firstname, data, value):
        verified = self.admitted(firstname)
        if verified:
            if data == 'mail' or data == 'comment':
                verified[data] = value
            else:
                return f"{data} doesn't exist in {firstname} data!"
        else:
            return 'Invalid user!'
        
    # To get the details of a particular user, if data is specified, it'll get that specific data rather than all the data
    def details(self, firstname, data=False):
        verified = self.admitted(firstname)
        if verified:
            if (data=='mail'):
                return verified[data]
            elif (data=='comment'):
                return verified[data]
            else: return verified
        else:
            return 'Invalid user!'
    
    # Delete data
    def delete(self, firstname):
        self.update_database()
        file.clear_file(self.myfile)
        verified = self.admitted(firstname)
        if verified:
            for key, value in Database.database.items():
                if (firstname.lower() == value['firstname']):
                    del Database.database[key]
                    break
            # self.sort_database_keys()
            self.population -= 1
            self.sort_database_keys() 
            file.write(self.myfile, str(Database.database))     
            return f"{firstname} successfully deleted!"
        else:
            return f"{firstname} is invalid!"
    
    # Save dictionary to file
    def save_to_file(self):
        verify = input('Are you sure you want to save? Yes(Y) or No(N): ')
        if Database.database and verify.upper()=='Y':
            file.write(self.myfile, str(Database.database))
        elif verify.upper()=='N':
            return 'Continue editing!'
        else:
            return 'No new data registered!'

    # All data are organized into a particular table with all their data listed
    def organize(self):
        self.update_database()
        
        dash = "-"
        for key, value in Database.database.items():
            dict_keys = ""
            for k, v in value.items():
                dict_keys += f"{k.title():<20}"
            print(f"{dict_keys}\n{dash*80}") 
            break
        for key, value in Database.database.items():
            dict_values = ""
            for k, v in value.items():
                if len(v) > 15:
                    v = v[:8] + '...'
                    dict_values += f"{v:<20}"
                else:
                    dict_values += f"{v:<20}"
            print(f"{dict_values}\n{dash*80}")
        
        # Save file again because the file is emptied after updating and dictionary automatically removes (no input)
        file.write(self.myfile, str(Database.database))
    

# Creating objects of the Database class
database = Database('database.txt')
database.register('jerry', 'aribidara', 'aribidarajerry@gmail.com', 'Nice job!')
database.register('clinton', 'wonder', 'clintonwonder689@gmail.com', 'You tried but you can work more on the UI. Thanks!')
database.register('alice', 'keys', 'alicekeys53@gmail.com', 'Well done! Keep up the good work!')
database.register('joshua', 'jacob', 'joshuajacob412@gmail.com', 'Wonderful!')
database.register('queen', 'elizabeth', 'queenelizabeth228@gmail.com', 'Hard work really pays!')
database.register('queeneth', 'elizabeth', 'queenethelizabeth228@gmail.com', 'Hard work pays!')

# database.delete('jerry')
print(database.organize())
print(database.save_to_file())


