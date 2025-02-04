

class Users:
    # class variable
    population = 0
    database = {}

    def __init__(self):
        self.my_dict = False

    # Automatically adds new object to database dictionary in the class variable
    def save(self, data):
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
            self.save(info)
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
        
    # All users are organized into a particular table with all their data listed
    def organize(self):
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
    

# Creating objects of the Users class
users = Users()
users.register('jerry', 'aribidara', 'aribidarajerry@gmail.com', 'Nice job!')
users.register('clinton', 'wonder', 'clintonwonder689@gmail.com', 'You tried but you can work more on the UI. Thanks!')
users.register('alice', 'keys', 'alicekeys53@gmail.com', 'Well done! Keep up the good work!')
users.register('joshua', 'jacob', 'joshuajacob412@gmail.com', 'Wonderful!')
users.register('queen', 'elizabeth', 'queenelizabeth228@gmail.com', 'Hard work really pays!')