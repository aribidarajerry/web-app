

class Users:
    # class variable
    population = 0
    database = {}

    def __init__(self):
        self.my_dict = False

    def save(self, data):
        self.my_dict = data
        Users.database[Users.population] = data

    def admitted(self, firstname):
        verify = False
        for key, value in Users.database.items():
            if (firstname.lower() == value["firstname"]):
                verify = True
                return value
        if verify != True:
            return False
        
    def register(self, fname, lname, mail, comment):
        verified = self.admitted(fname)
        if not verified:
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

    def update(self, firstname, data, value):
        verified = self.admitted(firstname)
        if verified:
            if data == 'mail' or 'comment':
                verified[data] = value
        else:
            return 'Invalid user!'
        
    def details(self, firstname, data=False):
        verified = self.admitted(firstname)
        if verified:
            if (data=='mail'):
                return self.my_dict[data]
            elif (data=='comment'):
                return self.my_dict[data]
            else: return self.my_dict
        else:
            return 'Invalid student!'
        
    def organize(self):
        dash = "-"
        for key, value in Users.database.items():
            dict_keys = ""
            for k, v in value.items():
                dict_keys += f"{k.title():<30}"
            print(f"{dict_keys}\n{dash*66}") 
            break
        for key, value in Users.database.items():
            dict_values = ""
            for k, v in value.items():
                dict_values += f"{v:<30}"
            print(f"{dict_values}\n{dash*66}")  
    
    
users = Users()
users.register('jerry', 'aribidara', 'aribidarajerry@gmail.com', 'm')
users.register('wonder', 'aribidara', 'aribidarawonder@gmail.com', 'm')
users.register('comfort', 'aribidara', 'aribidaracomfort@gmail.com', 'f')
users.register('joshua', 'jacob', 'joshuajacob@gmail.com', 'm')
users.register('queen', 'elizabeth', 'queenelizabeth@gmail.com', 'f')
print(users.details('jerry', 'mail'))
print(users.organize())


