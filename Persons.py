class Persons(object):

    def __init__(self, data):
        self.persons = []
        for item in data:
            self.persons.append(item)

    def get(self):
        return self.persons

