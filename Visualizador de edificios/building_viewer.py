
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import sys
import os.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import grafica.transformations as tr
import grafica.easy_shaders as es
import grafica.scene_graph as sg
import grafica.lighting_shaders as ls
from grafica.assets_path import getAssetPath

import modelo

EMPIRE=0
WILLIS=1
BURJ=2

cam1=0
cam2=1
cam3=2
cam4=3
cam5=4

DIA=0
NOCHE=1
# A class to store the application control
class Controller:
    def __init__(self):
        self.fillPolygon = True
###########################################################
        self.theta = np.pi
        self.eye = [0, 0, 0.1]
        self.at = [0, 1, 0.1]
        self.up = [0, 0, 1]
        self.edificio=EMPIRE
        self.camara=cam1
        self.iluminacion=DIA
###########################################################


# global controller as communication with the callback function
controller = Controller()

def on_key(window, key, scancode, action, mods):

    if action != glfw.PRESS and action != glfw.REPEAT:
        return
    
    global controller

    if key == glfw.KEY_SPACE:
        controller.fillPolygon = not controller.fillPolygon

    #Seleccion de edificios
    elif key == glfw.KEY_E:
        controller.edificio = EMPIRE

    elif key == glfw.KEY_W:
        controller.edificio = WILLIS

    elif key == glfw.KEY_B:
        controller.edificio = BURJ

    #Seleccion de camaras
    if key == glfw.KEY_1:
        controller.camara = cam1

    elif key == glfw.KEY_2:
        controller.camara = cam2

    elif key == glfw.KEY_3:
        controller.camara = cam3

    elif key == glfw.KEY_4:
        controller.camara = cam4

    elif key == glfw.KEY_5:
        controller.camara = cam5

    elif key == glfw.KEY_ESCAPE:
        glfw.set_window_should_close(window, True)

    #Dia y noche
    if key==glfw.KEY_L:
        controller.iluminacion=(controller.iluminacion+1)%2


if __name__ == "__main__":

    # Initialize glfw
    if not glfw.init():
        glfw.set_window_should_close(window, True)

    width = 600
    height = 600

    window = glfw.create_window(width, height, "Visualizador de edificios xd", None, None)

    if not window:
        glfw.terminate()
        glfw.set_window_should_close(window, True)

    glfw.make_context_current(window)

    # Connecting the callback function 'on_key' to handle keyboard events
    glfw.set_key_callback(window, on_key)

    # Creating shader programs for textures and for colors
    textureShaderProgram = es.SimpleTextureModelViewProjectionShaderProgram()
    lightShaderProgram = ls.SimpleGouraudShaderProgram()

    # Setting up the clear screen color
    glClearColor(0.85, 0.85, 0.85, 1.0)

    # As we work in 3D, we need to check which part is in front,
    # and which one is at the back
    glEnable(GL_DEPTH_TEST)

    # Creating shapes on GPU memory
    gpuPisoEmpire=modelo.create_floor(textureShaderProgram,"empire.png")
    gpuPisoWillis=modelo.create_floor(textureShaderProgram,"willis.png")
    gpuPisoBurj=modelo.create_floor(textureShaderProgram,"burj.jpg")

    gpuEdificioEmpire=modelo.Empire(lightShaderProgram)
    gpuEdificioWillis= modelo.Willis(lightShaderProgram)
    gpuEdificioBurj=modelo.Burj_Khalifa(lightShaderProgram)

    #Camaras
    posicion1=np.array([0,-5,3])
    posicion2=np.array([-5,-5,4])
    posicion3=np.array([5,5,4])
    posicion4=np.array([0,0,8])

    #Vistas
    projection1 = tr.perspective(60, float(width)/float(height), 0.1, 10)
    projection2 = tr.ortho(-2, 2, -2, 2, 0.1, 10)

    #Luz ligeramente azul (Empire State Building)
    KdEmpireDia=np.array([0.8,0.8,1])
    KdEmpireNoche=np.array([0.2,0.2,0.4])
    KdEmpireInicial=np.array([0.8,0.8,1])
    #Luz blanca (Willis Tower)
    KdWillisDia=np.array([1,1,1])
    KdWillisNoche=np.array([0.2,0.2,0.2])
    KdWillisInicial=np.array([1,1,1])
    #Luz ligeramente amarilla (Burj Khalifa)
    KdBurjDia=np.array([1,1,0.8])
    KdBurjNoche=np.array([0.4,0.4,0.2])
    KdBurjInicial=np.array([1,1,0.8])

    t0 = glfw.get_time()

    #Angulo inicial de la camara cuanndo se quiere usar la camara numero 5
    camera_theta = -3 * np.pi / 4

    # glfw will swap buffers as soon as possible
    glfw.swap_interval(0)

    camZ=1
    
    while not glfw.window_should_close(window):
        # Using GLFW to check for input events
        glfw.poll_events()
        at = np.array([0, 0, camZ])
        up=np.array([0,0,camZ])
        # Getting the time difference from the previous iteration
        t1 = glfw.get_time()
        dt = t1 - t0
        t0 = t1

        # Filling or not the shapes depending on the controller state
        if (controller.fillPolygon):
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        R = 5
        #Cambio de edificios
        if controller.edificio == EMPIRE:
            edificio = gpuEdificioEmpire
            gpuFloor = gpuPisoEmpire
            if controller.iluminacion==DIA:
                Kd=KdEmpireDia
            else:
                Kd=KdEmpireNoche
            if Kd[1]<KdEmpireInicial[1] and abs(Kd[1]-KdEmpireInicial[1])>0.05:
                for i in range(0,3):
                    KdEmpireInicial[i]-=dt
            elif Kd[1]>KdEmpireInicial[1] and abs(Kd[1]-KdEmpireInicial[1])>0.05:
                for i in range(0,3):
                    KdEmpireInicial[i]+=dt
            else:
                KdEmpireInicial=Kd
            Kd=KdEmpireInicial
        elif controller.edificio == WILLIS:
            edificio = gpuEdificioWillis
            gpuFloor = gpuPisoWillis
            if controller.iluminacion==DIA:
                Kd=KdWillisDia
            else:
                Kd=KdWillisNoche
            if Kd[1]<KdWillisInicial[1] and abs(Kd[1]-KdWillisInicial[1])>0.05:
                for i in range(0,3):
                    KdWillisInicial[i]-=dt
            elif Kd[1]>KdWillisInicial[1] and abs(Kd[1]-KdWillisInicial[1])>0.05:
                for i in range(0,3):
                    KdWillisInicial[i]+=dt
            else:
                KdWillisInicial=Kd
            Kd=KdWillisInicial
        elif controller.edificio == BURJ:
            edificio = gpuEdificioBurj
            gpuFloor = gpuPisoBurj
            if controller.iluminacion==DIA:
                Kd=KdBurjDia
            else:
                Kd=KdBurjNoche
            if Kd[1]<KdBurjInicial[1] and abs(Kd[1]-KdBurjInicial[1])>0.05:
                for i in range(0,3):
                    KdBurjInicial[i]-=dt
            elif Kd[1]>KdBurjInicial[1] and abs(Kd[1]-KdBurjInicial[1])>0.05:
                for i in range(0,3):
                    KdBurjInicial[i]+=dt
            else:
                KdBurjInicial=Kd
            Kd=KdBurjInicial
        #Cambio de camaras
        if controller.camara == cam1:
            viewPos=posicion1
            at = np.array([0, 0, 1.5])
            proyeccion=projection2
        elif controller.camara==cam2:
            viewPos=posicion2
            at = np.array([0, 0, 3])
            proyeccion=projection1
        elif controller.camara==cam3:
            viewPos=posicion3
            at = np.array([0, 0, 1.5])
            proyeccion=projection2
        elif controller.camara==cam4:
            viewPos=posicion4
            at=np.array([0, 0, 0])
            up=np.array([0,1,0])
            proyeccion=projection2
        elif controller.camara==cam5:
            camX = R * np.sin(camera_theta)
            camY = R * np.cos(camera_theta)
            if (glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS):
                camera_theta += 2 * dt
            if (glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS):
                camera_theta -= 2 * dt
            if (glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS):
                camZ += 2 * dt
            if (glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS):
                camZ -= 2 * dt
            viewPos = np.array([camX, camY, camZ])
            at = np.array([0, 0, camZ])
            proyeccion=projection1
        view = tr.lookAt(viewPos,at,up)

        #Cambio de dia y noche
        # if Kd
###########################################################################

        # Drawing dice (with texture, another shader program)
        glUseProgram(textureShaderProgram.shaderProgram)
        glUniformMatrix4fv(glGetUniformLocation(textureShaderProgram.shaderProgram, "projection"), 1, GL_TRUE, proyeccion)
        glUniformMatrix4fv(glGetUniformLocation(textureShaderProgram.shaderProgram, "view"), 1, GL_TRUE, view)
        sg.drawSceneGraphNode(gpuFloor, textureShaderProgram, "model")


        glUseProgram(lightShaderProgram.shaderProgram)
        glUniformMatrix4fv(glGetUniformLocation(lightShaderProgram.shaderProgram, "view"), 1, GL_TRUE, view)
        glUniformMatrix4fv(glGetUniformLocation(lightShaderProgram.shaderProgram, "projection"), 1, GL_TRUE, proyeccion)
        # Esto es para indicarle al shader de luz parámetros, pero por ahora no lo veremos
        lightShaderProgram.set_light_attributes(Kd)

        
        #Se dibuja
        sg.drawSceneGraphNode(edificio, lightShaderProgram, "model")

        # Once the drawing is rendered, buffers are swap so an uncomplete drawing is never seen.
        glfw.swap_buffers(window)
    # freeing GPU memory
    gpuPisoEmpire.clear()
    gpuPisoWillis.clear()
    gpuPisoBurj.clear()
    gpuEdificioEmpire.clear()
    gpuEdificioWillis.clear()
    gpuEdificioBurj.clear()

    glfw.terminate()
