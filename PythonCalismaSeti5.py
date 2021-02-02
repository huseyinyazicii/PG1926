class People:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    def giris(self):
        print(self.name+" "+self.surname+" Giriş Yaptı")
    def cikis(self):
        print(self.name+" "+self.surname+" Çıkış Yaptı")

class Student(People):
    pass
class Worker(People):
    pass
class Teacher(People):
    pass

class Class:
    def __init__(self,name,capacity,floor):
        self.name = name
        self.capacity = capacity
        self.floor = floor

class School:
    def __init__(self,name,capacity,numberOfTeachers,numberOfStudents):
        self.name = name
        self.capacity = capacity
        self.numberOfTeachers = numberOfTeachers
        self.numberOfStudents = numberOfStudents
    def schoolInformation(self):
        print("Okul Adı : "+self.name)
        print("Okul Kapasitesi : "+self.capacity)
        print("Okuldaki Öğretmen Sayısı : "+self.numberOfTeachers)
        print("Okuldaki Öğrenci Sayısı : "+self.numberOfStudents)

school1 = School("Ankara Lisesi","500","75","425")
school2 = School("İstanbul Lisesi","750","95","744")
school3 = School("Bursa Lisesi","300","43","240")

school1.schoolInformation()
print("-------------------------------------")
school2.schoolInformation()
print("-------------------------------------")
school3.schoolInformation()