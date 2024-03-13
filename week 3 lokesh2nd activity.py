class person  :

    def __init__(self,n,g,a) :
        self.name=n
        self.gender=g
        self.age=a

    def talk(self) :
        print("hi I'm", self.name)
    
    def vote(self):
        if self.age<18 :
            print("i am not eligible to vote")
        else:
            print("i am eligible to vote")

obj1= person("sam","male",22)
obj2= person("Jesse","Female",16)
obj1.talk()
obj1.vote()

obj2.talk()
obj2.vote()