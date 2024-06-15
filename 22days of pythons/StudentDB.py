class Std:
    def __init__(self):
        self.Name=None
        self.USN=None
        self.Marks =[]
        self.Percentage=None
        self.stdDetail()
    def stdDetail(self):
        self.Name=input('enter ur name:')
        self.USN=input('enter ur usn:')
        for i in range(5):
            marks=int(input('enter ur marks:'))
            self.Marks.append(marks)
    def percentage(self):
        self.Percentage = (sum(self.Marks)/len(self.Marks)*100)/100
        return self.Percentage
    def dispDetails(self):
        print('Name',self.Name)
        print('USN',self.USN)
        print('Marks',self.Marks)
        print('Percentage',self.percentage())

ob=Std()
ob.dispDetails()