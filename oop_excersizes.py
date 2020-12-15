class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def print_contact_info(self):
        print("{}'s email: {}\n{}'s phone: {}".format(self.name, self.email, self.name, self.phone))
    
    def add_friend(self, friend):
        self.friends.append(friend)
    
    def num_friends(self):
        print(len(self.friends))


sonny = Person('sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)
sonny.print_contact_info()
jordan.add_friend(sonny)
jordan.num_friends()
