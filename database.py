import file

file_name = 'test.txt'

# Count the registered dictionaries and increase the population to the number

# Anytime I save to a file, the dictionary should be emptied

class Users:
    # class variable
    population = 0
    database = {}

    def __init__(self, f):
        self.myfile = f
        self.my_dict = False
        # Read the file using the parameter in the class (Users) instance
        self.content = file.get(self.myfile)


    # If something is inside the file, let the database be equal to the file content which is a dictionary
    def update_database(self):
        import ast
        if self.content and Users.database=={}:

            # Convert file content to dictionaries
            content = ast.literal_eval(self.content)
            Users.database = content

            # Clear file after updating database with the file content so that when writing back to the file, it doesn't create duplicates
            file.clear_file(self.myfile)

            for c in content:
                Users.population += 1


    # Automatically adds new object to database dictionary in the class variable
    def save(self, data, f_name):
        self.my_dict = data
        Users.database[Users.population] = data

    # To verify if a user exists for authentication purposes
    def admitted(self, firstname):
        verify = False
        for key, value in Users.database.items():
            if (firstname.lower() == value["firstname"]):
                verify = True
                return value
        if verify != True:
            return False
        
    # To register a new user through an object
    def register(self, fname, lname, mail, comment):
        self.update_database()
        verified = self.admitted(fname)
        if not verified:
            # Auto increment and saves if user firstname doesn't exist already
            Users.population+=1
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
    

    # Save dictionary to file
    def save_to_file(self):
        verify = input('Are you sure you want to save? Yes(Y) or No(N): ')
        if Users.database and verify.upper()=='Y':
            file.write(self.myfile, str(Users.database))
        elif verify.upper()=='N':
            return 'Continue editing!'
        else:
            return 'No new data registered!'

    # All users are organized into a particular table with all their data listed
    def organize(self):
        self.update_database()
        
        dash = "-"
        for key, value in Users.database.items():
            dict_keys = ""
            for k, v in value.items():
                dict_keys += f"{k.title():<20}"
            print(f"{dict_keys}\n{dash*80}") 
            break
        for key, value in Users.database.items():
            dict_values = ""
            for k, v in value.items():
                if len(v) > 15:
                    v = v[:8] + '...'
                    dict_values += f"{v:<20}"
                else:
                    dict_values += f"{v:<20}"
            print(f"{dict_values}\n{dash*80}")
        
        # Save file again because the file is emptied after updating and dictionary automatically removes (no input)
        file.write(self.myfile, str(Users.database))
    

# Creating objects of the Users class
users = Users('text.txt')
users.register('jerry', 'aribidara', 'aribidarajerry@gmail.com', 'Nice job!')
users.register('clinton', 'wonder', 'clintonwonder689@gmail.com', 'You tried but you can work more on the UI. Thanks!')
users.register('alice', 'keys', 'alicekeys53@gmail.com', 'Well done! Keep up the good work!')
users.register('joshua', 'jacob', 'joshuajacob412@gmail.com', 'Wonderful!')
users.register('queen', 'elizabeth', 'queenelizabeth228@gmail.com', 'Hard work really pays!')
users.register('queeneth', 'elizabeth', 'queenethelizabeth228@gmail.com', 'Hard work really pays!')


print(users.organize())
# print(users.save_to_file())
