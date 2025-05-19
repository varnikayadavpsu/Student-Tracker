# STUDENT TRACKER 

import json 

class StudentTracker:

    def __init__(self):
        self.data = []

    
    def add_student(self, name, score, email):
        student = {
            'name': name,
            'score': score,
            'email': email
        }

        self.data.append(student)
    
        print(f'{name} added successfully.\n')
        print()


    def delete_student(self, name):
        
        for student in self.data:

            if student['name'] == name:
                self.data.remove(student)
                print(f'{name} removed successfully.\n')
            else:  
                 print(f'{name} not found.\n')   
        print()

    
    def list_students(self):

        if not self.data:
            print('No record found.\n')  
        else:
            print('Student List:')

            for one in self.data:
                print(f"Name: {one['name']}, Score: {one['score']}, Email: {one['email']}")
        
        print()

    
    def save_to_file(self, filename = 'students.json'):

        with open(filename, 'w') as f:
            json.dump(self.data, f)
        
        print('Data saved to file.\n')

    def load_from_file(self, filename = 'students.json'):

        try:
            with open(filename, 'r') as f:
                self.data = json.load(f)
            print('Data loaded from file.\n')
        except FileNotFoundError:
            print('No previous data found.\n')


working = StudentTracker()
working.load_from_file()

def show_menu():
    print('Student Tracker Menu:')
    print('1. Add student')
    print('2. Delete student')
    print('3. List students')
    print('4. Save & Exit')


while True:
    show_menu()
    choice = input('Enter your choice(1-4): ')

    if choice == '1':
        name = input('Enter name: ')
        score = input('Enter score: ')
        email = input('Enter email: ')
        working.add_student(name, score, email)
    
    elif choice == '2':
        name = input('Enter name to delete: ')
        working.delete_student(name)
    
    elif choice == '3':
        working.list_students()
    
    elif choice == '4':
        working.save_to_file()
        print('Goodbye!')
        break

    else:
        print('Invalid choice. Try again.\n')





    

