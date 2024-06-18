import pika
import pika.connection
import pygame

pygame.init()
pygame.joystick.init()

broker_address = "services.vayut.com"
port =5672
topic="rkcmd72"
username ="parry"
password = "parry"
virtual_host = "drone"

credentials = pika.PlainCredentials(username,password)
connection = pika.BlockingConnection(pika.ConnectionParameters(broker_address,port,virtual_host,credentials))

channel = connection.channel()

channel.exchange_declare(topic,topic,durable=True)

try:
	j = pygame.joystick.Joystick(0) # create a joystick instance
	j.init() # init instance
	print ("Enabled joystick: {0}".format(j.get_name()))
except pygame.error:
	print ("no joystick found.")
data = {}
while(1):
    for event in pygame.event.get():
        for i in range(12):
            data["button"+str(i)]=j.get_button(i)
        data["throttle"]=j.get_axis(3)*-1
        data["x"]=j.get_axis(0)
        data["y"]=j.get_axis(1)
        data["z"]=j.get_axis(2)
        channel.basic_publish(exchange=topic,routing_key=topic,body=data)
