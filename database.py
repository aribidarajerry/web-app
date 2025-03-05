import file

# Count the database list and increase the population to the number
# Anytime I save to a file, the dictionary should be emptied

class Database:

    # class variable
    database = []
    population = len(database)


    def __init__(self, f):
        self.myfile = f
        self.list = False

        # Read the file using the parameter in the class (Database) instance
        self.content = file.get(self.myfile)

    # If data is saved in the file, append its content to the database class variablel
    def update_database(self):

        # To convert the file content from string back to original list (or dictionary)
        import ast
        if self.content and Database.database==[]:
            
            # Convert file content from string to list
            Database.database = ast.literal_eval(self.content)

            # Clear file after updating database with the file content so that when writing back to the file, it doesn't create duplicates
            file.clear_file(self.myfile)
            for c in Database.database:
                Database.population += 1
            return Database.database

    # To verify if a key exists for authentication purposes
    def admitted(self, key):
        self.update_database()
        verify = False
        for data in Database.database:
            for d in data:
                if (key.lower() == data[d]):
                    verify = True
                    return data
        if verify != True:
            return False
        
    # Use code to register a new user through an object
    # To save registered names to file, use save_to_file() method
    # If what you want to save is less than or more than the parameters listed, just edit the register parameters and the 'info' dictionary
    # Every other thing will be taken care of by the code
    # The first parameter of this method represents the key for accessing it's data and cannot be duplicated
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
            self.save(info)
        else:
            print(fname.title() + ' already taken!')


    # Saves data registered above to database in class variable and can also be used to save any dictionary but for proper organization of keys, it's better to use the register() method
    def save(self, data):
        self.list = data
        Database.database.append(data)

    # Update saved data
    def update(self, key, data, value):
        verified = self.admitted(key)
        if verified:
            try:
                verified[data]
            except:
                return f"{data} doesn't exist in {key} data!"
            else:
                verified[data] = value
                return f'{key} {data} updated!'
            finally:
                self.save_to_file()
        else:
            self.save_to_file()
            return 'Invalid user!'
        
    # To get the details of a particular user, if data is specified, it'll get that specific data rather than all the data
    def details(self, key, data=False):
        verified = self.admitted(key)
        if verified:
            self.save_to_file()
            try:
                if data:
                    return verified[data]
            except Exception as e:
                return verified
            else:
                return verified
        else:
            self.save_to_file()
            return 'Invalid user!'
    
    # Delete data
    def delete(self, key):
        self.update_database()
        verified = self.admitted(key)
        if verified:
            for data in Database.database:
                for d in data:
                    if (key.lower() == data[d]):
                        del Database.database[Database.database.index(data)]
            self.population -= 1
            self.save_to_file()
            return f"{key} successfully deleted!"
        else:
            self.save_to_file()
            return f"{key} is invalid!"
    
    # Save dictionary to file
    def save_to_file(self):
        if Database.database:
            file.write(self.myfile, str(Database.database))
        else:
            file.write(self.myfile, str(Database.database))
            return 'No new data registered!'

    # To display saved data
    def organize(self):
        self.update_database()     
        dash = "-"
        for key in Database.database:
            dict_keys = ""
            for k, v in key.items():
                dict_keys += f"{k.title():<20}"
            print(f"{dict_keys}\n{dash*80}") 
            break
        for key in Database.database:
            dict_values = ""
            for k, v in key.items():
                if len(v) > 15:
                    v = v[:8] + '...'
                    dict_values += f"{v:<20}"
                else:
                    dict_values += f"{v:<20}"
            print(f"{dict_values}\n{dash*80}")
            # Save file again because the file is emptied after updating and dictionary automatically removes (no input)
            self.save_to_file()

    

# Creating objects of the Database class with the choiced filename
database = Database('database.txt')


# This is a sample usage of the register method for registering visitors for a website
# database.register('jerry', 'aribidara', 'aribidarajerry@gmail.com', 'Well done! Keep up the good work!')

# After registering, you must store user to file using the save_to_file()...Very important!
# database.save_to_file()

# print(database.delete('jerry'))

# You can view the file and verify if it's written to it using the 'file' module
print(database.organize())

"""
register ----
update ----
details ----
delete ----
save_to_file
organize
"""

# obj = {
#     'name': 'jerry'
# }
