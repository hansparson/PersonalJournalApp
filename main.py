import os

file_path = './data/default.jrn'

class Journal:
    def __init__(self):
        self.temporary_data = ""
        self.current_data = ""

    def check_content(self):
        with open(file_path, 'r') as file:
            content = file.read() + self.temporary_data
            content = content.split(",")[1:]
            for i, value in enumerate(content):
                print("{}. {}".format(i+1, value))
        print()
        obj.choose_action()
    
    def add_journal(self):
        journal = input("Enter your journal entry: \n") 
        self.temporary_data = self.temporary_data + "," + journal
        obj.choose_action()

    def choose_action(self):
        action = input("What do you want to do? [L]ist, [A]dd, or E[x]it?  ")
        if action == "l" or action == "L":
            self.check_content()
        elif action == "a" or action == "A":
            self.add_journal()
        elif action == "x" or action == "X":
            print("... saving to {} ...".format(file_path))
            with open(file_path, 'a') as file:
                file.write(self.temporary_data)
            print("... save complete ...")
            exit()
        else : 
            self.choose_action()

if __name__ == "__main__":
    print("... loading journal from {} ...".format(file_path))
    if os.path.getsize(file_path) == 0:
            print("... No entries to be found ...")
    else : 
        with open(file_path, 'r') as file:
            content = file.read()
            content = content.split(",")[1:]
            number_content = 0
            for i, value in enumerate(content):
                number_content = number_content + 1
            print("... loaded {} entries ...".format(number_content))
                
    obj = Journal()
    obj.choose_action()
