class Parent():
    def __init__(self,last_name,eye_color):
        print("parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("the last name :"+self.last_name)
        print("the eye color :"+self.eye_color)

class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("child constructor called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys

bily_cyrus = Parent("cyrus","blue")
bily_cyrus.show_info()
mily_cyrus = Child("cyrus","blue",5)
mily_cyrus.show_info()
#print(mily_cyrus.last_name)

#print(mily_cyrus.number_of_toys)
    
    
