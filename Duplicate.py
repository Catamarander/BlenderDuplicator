import bpy
from math import radians
import random

def copyObj(new_name, location=None, new_rotation=None, dist=0):

    # copy selected object data and create new object with that data
    obj_data = bpy.context.object.data
    new_object = bpy.data.objects.new(name=new_name, object_data=obj_data)
    
    # transform location
    if location == None:
        location = (random.uniform(-1, 1) * dist, random.uniform(-1, 1) * dist, random.uniform(-1, 1) * dist)
    new_object.location = location
    
    # transform rotation
    if new_rotation == None:
        new_rotation = (random.randint(0, 360), random.randint(0, 360), random.randint(0, 360))
    temp_rotation = new_object.rotation_euler
    for i in range(len(temp_rotation)):
        temp_rotation[i] = temp_rotation[i] + radians(new_rotation[i])
    new_object.rotation_euler = temp_rotation
    
    # link object to scene, select new object, and make new object active
    scene.objects.link(new_object)
    new_object.select = True
    scene.objects.active = new_object