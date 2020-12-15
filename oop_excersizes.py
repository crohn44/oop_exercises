class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_greeting_count = 0
        self.greeted_people = []

    def __str__(self):
        return 'Name: {}\nEmail: {}\nPhone: {}'.format(self.name, self.email, self.phone)

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        
        if other_person in self.greeted_people:
            pass
        else:
            self.unique_greeting_count += 1
        self.greeted_people.append(other_person)

    def print_contact_info(self):
        print("{}'s email: {}\n{}'s phone: {}".format(self.name, self.email, self.name, self.phone))
    
    def add_friend(self, friend):
        self.friends.append(friend)
    
    def num_friends(self):
        print(len(self.friends))

    def num_people_greeted(self):
        print('People Greeted: ' + str(self.greeting_count))

    def num_unique_people_greeted(self):
        print('Unique People Greeted: ' + str(self.unique_greeting_count))

sonny = Person('sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('jordan', 'jordan@aol.com', '495-586-3456')
greg = Person('greg', 'greg@gmail.com', '555-555-5555')

sonny.greet(jordan)
jordan.greet(sonny)


jordan.num_unique_people_greeted()

jordan.greet(greg)
jordan.num_unique_people_greeted()

jordan.greet(sonny)
jordan.num_unique_people_greeted()