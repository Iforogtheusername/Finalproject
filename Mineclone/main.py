#Copyright 2024##
print("Game has loaded!")
##---------------------------------------------##
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random 

class CustomEntity(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            color=color.black,
            scale=(1, 4),
            position=Vec3(40, -.5, 0),
            collider='box'
        )

    def input(self, key):
        if key == 'right mouse down' and mouse.hovered_entity == self:
            self.color = color.red
        elif key == 'right mouse up':
            self.color = color.black
    
Promptbox = CustomEntity()


jumpfiles = ['Video(3).wav', 'Video(4).wav']


# Run functionality

run = False

def update():
    global run

    if held_keys['control'] and held_keys['w']:
        run = True
        gameplay_camera.speed = 25 

    if run and not held_keys['w']:
        run = False
        gameplay_camera.speed = 10 


def lock_camera_controls():
    camera.ignore_input = True

def unlock_camera_controls():
    camera.ignore_input = False

def reset_camera_position():
    camera.position = Vec3(0, 2, -10)

app = Ursina(borderless=True)

# Window_setup
window.title = "Cursed Parkour - V1.0 - Mango Soda"
window.cog_button.enabled = False
window.fps_counter.enabled = False
window.entity_counter.enabled = False
# Entity positioning
window.collider_counter.enabled = False
window.fullscreen = True
window.borderless = False

start_screen_camera = Entity(model='cube', scale=(0.01, 0.01, 0.01))
start_screen_camera.position = (0, 10, -20)
gameplay_camera = FirstPersonController()
gameplay_camera.cursor.scale *= 1
gameplay_camera.enabled = False

# Entity spawning

cube = Entity(model="cube", texture="Metal.jpg", collider="mesh", scale=(25, 3, 25))
cube2 = Entity(model="cube", texture="rock.jpeg", collider="mesh", scale=(20, 2, 21))
cube3 = Entity(model="cube", texture="Metal.jpg", collider="mesh", scale=(4, 2, 3))
cube4 = Entity(model="cube", texture="Wood.jpg", collider="mesh", scale=(2, 2, 2))
cube5 = Entity(model="cube", texture="Wood.jpg", collider="mesh", scale=(2, 2, 2))
cube6 = Entity(model="cube", texture="Wood.jpg", collider="mesh", scale=(10, 2, 10))
cube7 = Entity(model="cube", texture="Wood.jpg", collider="mesh", scale=(2, 2, 2))
cube8 = Entity(model="cube", texture="Wood.jpg", collider="mesh", scale=(10, 2, 10))
Lavacube = Entity(model="cube", texture="Lava.jpg", scale=(100, 1, 60))
Sphere = Entity(model="sphere", collider="box", texture="AdvancedRock.jpg", scale=(2,2,2))
Sphere2 = Entity(model="sphere", collider="mesh", texture="AdvancedRock.jpg", scale=(2,2,2))
Sphere3 = Entity(model="sphere", collider="mesh", texture="AdvancedRock.jpg", scale=(2,2,2))
e = Entity(model=Cone(3), collider="box", texture='brick')
e2 = Entity(model=Cone(3), collider="box", texture='brick')
e3 = Entity(model=Cone(3), collider="box", texture='brick')
e4 = Entity(model=Cone(3), collider="box", texture='brick')

# Entity positioning

cube2.position = Vec3(0, 2, 2)
cube7.position = Vec3(0, 4.2, 14)


cube3.position = Vec3(0, 9, 25)
cube4.position = Vec3(-2, 11, 28.5)
cube5.position = Vec3(-2, 12, 31.5)
cube6.position = Vec3(10, 12, 33.5)
cube8.position = Vec3(10, 10, 58)
e.position = Vec3(-0.5, 12, 33.5)
e2.position = Vec3(1, 12, 33.5)
e3.position = Vec3(3, 12, 33.5)
e4.position = Vec3(4, 12, 33.5)
Lavacube.position = Vec3(0, 0, 40)
Sphere.position = Vec3(0, 6, 17)
Sphere2.position = Vec3(0, 8, 20)
Sphere3.position = Vec3(0, 10, 22)
arm = Entity(
    model='cube',
    parent=camera.ui,
    texture='Skin.jpg',
    position=(0.75, -0.6),
    rotation=(150, -10, 6),
    scale=(0.4, 0.4, 1.5)
)

gun = Entity(
    model="Sniper.obj",
    texture="kar1_diffuseOriginal.png",
    parent=camera.ui,
     position=(0.70, -0.3),
    rotation=(180,100,180),
    scale=(0.3 , 0.3, 0.3)
)

mario = Entity(
    model="Mario.obj",
    texture="0xbc4e9ae5.png",
    scale=1,
    position = Vec3(1, 0, -10),
    collision = 'mesh'
)

QR = Entity(
    model="QR.obj",
    texture="cow_plushie.png",
    scale=0.1,
    position = Vec3(35, -.5, 0),
    collision = 'mesh'
)

# Menu screen functionality
def start():
    maintxt.enabled = False  
    startbtn.enabled = False 
    versiontxt.enabled = False
    dekuline1.enabled = False
    menumusic.enabled = False

    start_screen_camera.enabled = False
    gameplay_camera.enabled = True
    gameplay_camera.cursor.locked = False

versiontxt = Text(text="V1.0", scale=2, x=-.05 , y=-.4)
maintxt = Text(text="Cursed Parkour Game", scale=2, x=-.3, y=.5)
startbtn = Button(text="Start!", scale=(0.3, 0.1), x=0)
startbtn.on_click = start

dekuline1 = Audio (
     'Titlespeech.wav',
      autoplay=True,
      loop=False
    )

menumusic = Audio (
    'My Song 20.mp3',
    autoplay=True,
    loop=True
)

def input(key):
    if key == 'p':
        quit()
    if key == 'space':
        selected_audio = random.choice(jumpfiles)
        jumpeffect = Audio(selected_audio, loop=False, autoplay=False, volume=.25)
        if not jumpeffect.playing:
            jumpeffect.play()


# Ground
ground = Entity(model="plane", texture="Grass.jpg", scale=(100, 1, 100), collider="mesh")
ground.y -= 0.5 

window.exit_button.disabled = True

Sky()

app.run()

#--Code end__POP>