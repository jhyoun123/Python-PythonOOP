class Patient(object):
    def __init__(self, id, name, allergies, bed):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed = bed
    
class Hosptial(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    def admit(self, name, allergies):
        if (len(self.patients) >= self.capacity):
            print "The hospital is full"
        else:
            patients.append(Patient(len(self.patients), name, allergies, len(self.patients)))
            print "Admission is complete"
    def discharge(self, id):
        partients.remove(id)
        self.bed = "none"