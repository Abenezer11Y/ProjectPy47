class SSN:
    name = "Abenezer"
    __SSN = 639273464
    def viewSSN(self):
        print(f"{self.name}'s Social Security Number is {SSN.__SSN}")
    def __password(self):
        print("Your password is SF_14SDvN")

person = SSN()
person.viewSSN()
person.__password()