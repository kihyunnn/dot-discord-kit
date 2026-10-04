import bpy, math, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blender-3d-demo')
from mathutils import Vector

# Reproducible, text-free showcase render for Squirebot/Dot Discord Kit.
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.render.engine = 'BLENDER_EEVEE'
scene.render.resolution_x = 1280
scene.render.resolution_y = 720
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = OUT + '.png'
scene.render.film_transparent = False
scene.world = bpy.data.worlds.new('Showcase World')
scene.world.color = (0.008, 0.015, 0.03)

# Materials
def mat(name, color, metallic=0.0, roughness=0.4, emission=None):
    m=bpy.data.materials.new(name); m.diffuse_color=(*color,1)
    m.use_nodes=True; bs=m.node_tree.nodes.get('Principled BSDF')
    bs.inputs['Base Color'].default_value=(*color,1)
    bs.inputs['Metallic'].default_value=metallic
    bs.inputs['Roughness'].default_value=roughness
    if emission:
        bs.inputs['Emission Color'].default_value=(*emission,1)
        bs.inputs['Emission Strength'].default_value=4.0
    return m
floor=mat('Midnight floor',(0.018,0.035,0.075),0.35,0.23)
cyan=mat('Dot cyan',(0.03,0.45,0.95),0.5,0.18, (0.01,0.28,1.0))
orange=mat('Warm accent',(1.0,0.22,0.045),0.25,0.22, (1.0,0.04,0.01))
white=mat('Soft white',(0.72,0.86,1.0),0.1,0.2, (0.25,0.55,1.0))
dark=mat('Graphite',(0.035,0.055,0.11),0.8,0.2)

# Floor
bpy.ops.mesh.primitive_plane_add(size=30, location=(0,0,-1.25)); bpy.context.object.data.materials.append(floor)

# Rounded cube helper
def cube(name, loc, scale, material, bevel=0.18):
    bpy.ops.mesh.primitive_cube_add(location=loc); o=bpy.context.object; o.name=name; o.scale=scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bev=o.modifiers.new('Soft edges','BEVEL'); bev.width=bevel; bev.segments=5
    o.data.materials.append(material); return o

# Floating conversation-card forms
cube('Message card A',(-2.15,0.25,0.15),(1.65,0.18,0.5),dark,0.22)
cube('Message card B',(1.45,0.3,0.05),(2.05,0.18,0.48),cyan,0.22)
cube('Message card C',(0.8,0.3,-0.75),(1.35,0.18,0.34),orange,0.17)

# Central glowing orb and connector rings
bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, radius=0.92, location=(0,0,0.75)); orb=bpy.context.object; orb.data.materials.append(white)
for z,scale in [(0.75,1.22),(0.75,1.42)]:
    bpy.ops.mesh.primitive_torus_add(major_radius=0.95*scale, minor_radius=0.025, major_segments=96, location=(0,0,z), rotation=(math.radians(72),0,math.radians(18)))
    bpy.context.object.data.materials.append(cyan)
# small satellites
for i,(x,z,s,m) in enumerate([(-3.25,0.2,0.24,cyan),(3.0,0.55,0.3,orange),(2.65,-0.55,0.18,white)]):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3,radius=s,location=(x,0,z)); bpy.context.object.data.materials.append(m)

# Camera
bpy.ops.object.camera_add(location=(0,-12.8,4.2)); cam=bpy.context.object; scene.camera=cam
cam.data.lens=52
def track(obj, point): obj.rotation_euler=(Vector(point)-obj.location).to_track_quat('-Z','Y').to_euler()
track(cam,(0,0,0.0))

# Lighting
def area(name, loc, energy, color, size):
    bpy.ops.object.light_add(type='AREA', location=loc); l=bpy.context.object; l.name=name; l.data.energy=energy; l.data.color=color; l.data.shape='DISK'; l.data.size=size; track(l,(0,0,0)); return l
area('Cool key',(-4,-5,7),1100,(0.18,0.42,1.0),5)
area('Warm rim',(5,-2,3),900,(1.0,0.12,0.03),4)
area('Top fill',(0,1,7),700,(0.3,0.55,1.0),3)

scene.view_settings.look='AgX - Medium High Contrast'
scene.render.filepath=OUT + '.png'
bpy.ops.wm.save_as_mainfile(filepath=OUT + '.blend')
bpy.ops.render.render(write_still=True)
