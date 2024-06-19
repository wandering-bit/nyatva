import pygame


class controller:
    def __init__(self,id:int=None):
        pygame.init()
        pygame.joystick.init()
        self.stickcount = pygame.joystick.get_count()


        
    def detect_sticks(self):
        print(f"Number of Joysticks detected: {self.stickcount}")
        for s in  range (self.stickcount):
            j = pygame.joystick.Joystick(s)
            j.init()
            print(f"{s} : {j.get_name()}, {j.get_guid()}")
            j.quit()


    def init(self,id:int)->None:
        '''
            Initialises the connection with the joystick with the supplied id
        '''

        if(self.stickcount==0):
            return 0
        
        if(id>self.stickcount-1):
            return -1
        
        self.j = pygame.joystick.Joystick(id)
        self.j.init()
        
    
    def metadata(self):
        return {"name":self.j.get_name(),"id":self.j.get_guid()}
    
    def getbutton(self,i):
        return self.j.get_button(i)
    
  
        
class Extreme3dPro(controller):

    roll = 0
    pitch = 0
    yaw = 0
    throttle =0
    hat=(0,0)

    def hatdata(self):
        self.hat = self.j.get_hat(0)

    def update(self):
        for event in pygame.event.get():
            self.roll=self.j.get_axis(0)
            self.pitch=self.j.get_axis(1)
            self.yaw=self.j.get_axis(2)
            self.throttle=self.j.get_axis(3)

if(__name__=='__main__'):    
    c1 = Extreme3dPro()
    c1.detect_sticks()
    c1.init(id=0)

    while(0):
        c1.update()
        print(c1.roll)
    
