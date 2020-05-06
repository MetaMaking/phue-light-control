from phue import Bridge

b = Bridge('192.168.1.124')
b.connect()

lights_list = b.get_light_objects('list')

for light in lights_list:
   light.on = False


