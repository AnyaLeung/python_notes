class User():
    country = None
    def smethod():
        print "Just a normal user"
    def cmethod(cls):
        @staticmethod
        print "Nationality: {}".format(cls)
    def hello(self):
        print "Hello, I'm User\0"

class ChineseUser(User):
    ucountry = "China"
    def hello(self):
        super(ChineseUser, self).hello() 
        print ", and I'm ChineseUser\0"

class RussianUser(User):
    ucountry = "Russia"
    def hello(self):
        super(RussianUser, self).hello()
        print ", and I'm RussianUser\0"

class ChineseRussianUser(ChineseUser, RussianUser):
    ucountry = "China && Russia"
    def smethod(self):
        User.smethod(self)
    def cmethod(self):
        User.cmethod(self)
    def hello(self):
        ChineseUser.hello(self)
        RussianUser.hello(self) 
        print "So, I'm ChineseRussianUser"
