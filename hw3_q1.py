class Patient:
    """ base class"""
    def __init__(self, name):
        self.name = name

    def discharged(self):
        raise NotImplementedError("This is an abstract method and nees to be implemented in derived classes.")

class EmergencyPatient:
    def __init__(self, name):
        Patient.__init__(self, name)
        self.ecost=1000

    def discharge(self):
        print(self.name, type(self))

class HospitalizedPatient:
    def __init__(self, name):
        Patient.__init__(self, name)
        self.ecost=2000  #same cost for each patient, no need to input attributes

    def discharge(self):
        print(self.name,type(self))


class Hospital:
    def __init__(self): #internally store patients and cost
        self.patients = []
        self.cost = 0

    def admit(self,patients):
        self.patients.append(patients)

    def discharge_all(self):
        for patients in self.patients:
            patients.discharge()
            self.cost += patients.ecost

    def get_total_cost(self):
        return self.cost

P1 = EmergencyPatient("P1")
P2 = EmergencyPatient("P2")
P3 = HospitalizedPatient('P3')
P4 = HospitalizedPatient('P4')
P5 = HospitalizedPatient('P5')
YNHH= Hospital()

YNHH.admit(P1)
YNHH.admit(P2)
YNHH.admit(P3)
YNHH.admit(P4)
YNHH.admit(P5)
YNHH.discharge_all()
print(YNHH.get_total_cost())


# myHospital.discharge_all()

