import file

# Count the registered dictionaries and increase the population to the number

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

    # If something is inside the file, let the database be equal to the file content which is a dictionary
    def update_database(self):
        # To convert string back to original list or dictionary
        import ast
        if self.content and Database.database==[]:
            # Convert file content from string to list
            Database.database = ast.literal_eval(self.content)
            # Clear file after updating database with the file content so that when writing back to the file, it doesn't create duplicates
            file.clear_file(self.myfile)
            for c in Database.database:
                Database.population += 1
            return Database.database


    # Automatically adds new object to database list in the class variable
    def save(self, data):
        self.list = data
        Database.database.append(data)

    # To verify if a user exists for authentication purposes
    def admitted(self, firstname):
        self.update_database()
        verify = False
        for data in Database.database:
            for d in data:
                if (firstname.lower() == data[d]):
                    verify = True
                    return data
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
            self.save(info)
        else:
            print(fname.title() + ' already taken!')

    # Update user's data
    def update(self, firstname, data, value):
        verified = self.admitted(firstname)
        if verified:
            try:
                verified[data] = value
            except:
                return f"{data} doesn't exist in {firstname} data!"
        else:
            return 'Invalid user!'
        
    # To get the details of a particular user, if data is specified, it'll get that specific data rather than all the data
    def details(self, firstname, data=False):
        verified = self.admitted(firstname)
        if verified:
            try:
                if data:
                    return verified[data]
            except Exception as e:
                return verified
            else:
                return verified
        else:
            return 'Invalid user!'
    
    # Delete data
    def delete(self, firstname):
        self.update_database()
        file.clear_file(self.myfile)
        verified = self.admitted(firstname)
        if verified:
            for data in Database.database:
                for d in data:
                    if (firstname.lower() == data[d]):
                        del Database.database[data]
            self.population -= 1
            file.write(self.myfile, str(Database.database))     
            return f"{firstname} successfully deleted!"
        else:
            return f"{firstname} is invalid!"
    
    # Save dictionary to file
    def save_to_file(self):
        if Database.database:
            file.write(self.myfile, str(Database.database))
        else:
            return 'No new data registered!'

    # All data are organized into a particular table with all their data listed
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
        file.write(self.myfile, str(Database.database))

    

# Creating objects of the Database class
database = Database('database.txt')


database.register('alice', 'keys', 'alicekeys53@gmail.com', 'Well done! Keep up the good work!')
database.register('joshua', 'jacob', 'joshuajacob412@gmail.com', 'Wonderful!')
database.register('queen', 'elizabeth', 'queenelizabeth228@gmail.com', 'Hard work really pays!')
# database.register('queeneth', 'elizabeth', 'queenethelizabeth228@gmail.com', 'Hard work pays!')

print(database.organize())
# database.save_to_file()


print(database.details('alice', 'comment'))







# obj = [{
#     'name': 'jerry',
#     'age': 20
# }]

# obj = str(obj)
# import ast
# obj = ast.literal_eval(obj)
# for o in obj:
#     for n in o:
#         print(n)
#         break