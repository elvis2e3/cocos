#
# Cocos' pause scene
#
from cocos.director import director
from cocos.layer import Layer, ColorLayer
from cocos.scene import Scene


import pyglet

__pause_scene_generator__ = None

def get_pause_scene():
    return __pause_scene_generator__()
    
def set_pause_scene_generator(generator):
    global __pause_scene_generator__
    __pause_scene_generator__ = generator
    
def default_pause_scene():
    return PauseScene(
        director.scene, ColorLayer(25,25,25,205), PauseLayer()
        )
set_pause_scene_generator( default_pause_scene )

class PauseScene(Scene):
    def __init__(self, background_scene, *layers):
        super(PauseScene, self).__init__(*layers)
        self.bg = background_scene
        
    def on_draw(self):
        self.bg.visit()
        super(PauseScene, self).on_draw()
        
class PauseLayer(Layer):
    def __init__(self):
        super(PauseLayer, self).__init__()
        
        x,y = director.get_window_size()
        
        ft = pyglet.font.load('Arial', 36)
        self.text = pyglet.font.Text(ft, 
            'PAUSED', halign=pyglet.font.Text.CENTER)
        self.text.x = x/2
        self.text.y = y/2
        
    def on_draw(self):
        self.text.draw()
        
    def on_key_press(self, k, m):
        if k == pyglet.window.key.P and m == pyglet.window.key.MOD_ACCEL:
            director.pop()
            return True
            
