import SH1106
import time
import paho.mqtt.client as paho
broker="10.8.0.1"

from PIL import Image,ImageDraw,ImageFont

try:
    disp = SH1106.SH1106()

    print("\r\1.3inch OLED")
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

    print ("received message =",str(message.payload.decode("utf-8")))
    draw.text((30,0), 'Waveshare ', font = font10, fill = 0)
    draw.text((28,20), u'微<9B><94><90> ', font = font, fill = 0)

    # image1=image1.rotate(180)
    disp.ShowImage(disp.getbuffer(image1))
    time.sleep(2)

    print ("***draw image")
    Himage2 = Image.new('1', (disp.width, disp.height), 255)  # 255: clear the frame
    bmp = Image.open('pic.bmp')
    Himage2.paste(bmp, (0,5))
    # Himage2=Himage2.rotate(180)
    disp.ShowImage(disp.getbuffer(Himage2))

except IOError as e:
    print(e)

except KeyboardInterrupt:
    print("ctrl + c:")
    disp.RPI.module_exit()
    exit()
main.py (END)





# Define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

client= paho.Client("client-010") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")

# Bind function to callback
client.on_message=on_message

# Set username and password
client.username_pw_set(username = "iot_module", password = "parool")

print("connecting to broker ",broker)
client.connect(broker)   # connect
client.loop_start()      # start loop to process received messages
print("subscribing ")
client.subscribe("class/iot10") #subscribe
time.sleep(2)

try:
        while True:
                    time.sleep(1)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect() #disconnect
    client.loop_stop() #stop loop
