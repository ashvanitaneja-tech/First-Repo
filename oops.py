class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_total(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hey", self.name , " Your avg score is :", sum/3)

s1 = student("lucky", [32 , 54, 42])
s1.get_total()