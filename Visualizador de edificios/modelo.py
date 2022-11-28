# coding=utf-8
"""Textures and transformations in 3D"""
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import sys
import os.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import grafica.transformations as tr
import grafica.basic_shapes as bs
import grafica.easy_shaders as es
import grafica.scene_graph as sg
from grafica.assets_path import getAssetPath

__author__ = "Daniel Calderon"
__license__ = "MIT"

############################################################################

def create_floor(pipeline,pisoedificio):
    shapeFloor = bs.createTextureQuad(1, 1)
    gpuFloor = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuFloor)
    gpuFloor.texture = es.textureSimpleSetup(
        getAssetPath(pisoedificio), GL_REPEAT, GL_REPEAT, GL_LINEAR, GL_LINEAR)
    gpuFloor.fillBuffers(shapeFloor.vertices, shapeFloor.indices, GL_STATIC_DRAW)

    floor = sg.SceneGraphNode("floor")
    floor.transform = tr.matmul([tr.translate(0, 0, 0),tr.scale(2, 2, 0)])
    floor.childs += [gpuFloor]

    return floor

def Burj_Khalifa(pipeline):
    #Cubo base color gris
    GreyCube = bs.createColorNormalsCube(128/255,128/255,128/255)
    gpuGreyCube = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuGreyCube)
    gpuGreyCube.fillBuffers(GreyCube.vertices,GreyCube.indices, GL_STATIC_DRAW)

    #Paralelepipedos que se usan para ensamblar el edificio
    paralelepipedo1=sg.SceneGraphNode("paralelepipedo1")
    paralelepipedo1.transform=tr.matmul([tr.translate(0,0.406,0.15),tr.scale(0.16,0.08,0.3)])
    paralelepipedo1.childs+=[gpuGreyCube]

    paralelepipedo2=sg.SceneGraphNode("paralelepipedo2")
    paralelepipedo2.transform=tr.matmul([tr.translate(0,0.326,0.6),tr.scale(0.16,0.08,1.2)])
    paralelepipedo2.childs+=[gpuGreyCube]

    paralelepipedo3=sg.SceneGraphNode("paralelepipedo3")
    paralelepipedo3.transform=tr.matmul([tr.translate(0,0.246,1.05),tr.scale(0.16,0.08,2.1)])
    paralelepipedo3.childs+=[gpuGreyCube]

    paralelepipedo4=sg.SceneGraphNode("paralelepipedo4")
    paralelepipedo4.transform=tr.matmul([tr.translate(0,0.166,1.5),tr.scale(0.16,0.08,3)])
    paralelepipedo4.childs+=[gpuGreyCube]

    paralelepipedo5=sg.SceneGraphNode("paralelepipedo5")
    paralelepipedo5.transform=tr.matmul([tr.translate(0,0.086,1.95),tr.scale(0.16,0.08,3.9)])
    paralelepipedo5.childs+=[gpuGreyCube]

    paralelepipedo6=sg.SceneGraphNode("paralelepipedo6")
    paralelepipedo6.transform=tr.matmul([tr.translate(0,0.406,0.3),tr.scale(0.16,0.08,0.6)])
    paralelepipedo6.childs+=[gpuGreyCube]

    paralelepipedo7=sg.SceneGraphNode("paralelepipedo7")
    paralelepipedo7.transform=tr.matmul([tr.translate(0,0.326,0.75),tr.scale(0.16,0.08,1.5)])
    paralelepipedo7.childs+=[gpuGreyCube]

    paralelepipedo8=sg.SceneGraphNode("paralelepipedo8")
    paralelepipedo8.transform=tr.matmul([tr.translate(0,0.246,1.2),tr.scale(0.16,0.08,2.4)])
    paralelepipedo8.childs+=[gpuGreyCube]

    paralelepipedo9=sg.SceneGraphNode("paralelepipedo9")
    paralelepipedo9.transform=tr.matmul([tr.translate(0,0.166,1.65),tr.scale(0.16,0.08,3.3)])
    paralelepipedo9.childs+=[gpuGreyCube]

    paralelepipedo10=sg.SceneGraphNode("paralelepipedo10")
    paralelepipedo10.transform=tr.matmul([tr.translate(0,0.086,2.1),tr.scale(0.16,0.08,4.2)])
    paralelepipedo10.childs+=[gpuGreyCube]

    paralelepipedo11=sg.SceneGraphNode("paralelepipedo11")
    paralelepipedo11.transform=tr.matmul([tr.translate(0,0.406,0.45),tr.scale(0.16,0.08,0.9)])
    paralelepipedo11.childs+=[gpuGreyCube]

    paralelepipedo12=sg.SceneGraphNode("paralelepipedo12")
    paralelepipedo12.transform=tr.matmul([tr.translate(0,0.326,0.9),tr.scale(0.16,0.08,1.8)])
    paralelepipedo12.childs+=[gpuGreyCube]

    paralelepipedo13=sg.SceneGraphNode("paralelepipedo13")
    paralelepipedo13.transform=tr.matmul([tr.translate(0,0.246,1.35),tr.scale(0.16,0.08,2.7)])
    paralelepipedo13.childs+=[gpuGreyCube]

    paralelepipedo14=sg.SceneGraphNode("paralelepipedo14")
    paralelepipedo14.transform=tr.matmul([tr.translate(0,0.166,1.8),tr.scale(0.16,0.08,3.6)])
    paralelepipedo14.childs+=[gpuGreyCube]

    paralelepipedo15=sg.SceneGraphNode("paralelepipedo15")
    paralelepipedo15.transform=tr.matmul([tr.translate(0,0.086,2.25),tr.scale(0.16,0.08,4.5)])
    paralelepipedo15.childs+=[gpuGreyCube]

    paralelepipedo16=sg.SceneGraphNode("paralelepipedo16")
    paralelepipedo16.transform=tr.matmul([tr.translate(0,0,2.5),tr.scale(0.138,0.138,5)])
    paralelepipedo16.childs+=[gpuGreyCube]
    
    paralelepipedo17=sg.SceneGraphNode("paralelepipedo17")
    paralelepipedo17.transform=tr.matmul([tr.translate(0,0,3),tr.scale(0.05,0.05,6)])
    paralelepipedo17.childs+=[gpuGreyCube]

    #Parte 1 Edificio completo
    Edificio1 = sg.SceneGraphNode("Edificio1")
    Edificio1.transform = tr.identity()
    Edificio1.childs += [paralelepipedo1,paralelepipedo2,paralelepipedo3,paralelepipedo4,paralelepipedo5]

    #Parte 2 Edificio completo
    Edificio2 = sg.SceneGraphNode("Edificio2")
    Edificio2.transform = tr.rotationZ(-4*np.pi/3)
    Edificio2.childs += [paralelepipedo6,paralelepipedo7,paralelepipedo8,paralelepipedo9,paralelepipedo10]

    #Parte 3 Edificio completo
    Edificio3 = sg.SceneGraphNode("Edificio3")
    Edificio3.transform = tr.rotationZ(4*np.pi/3)
    Edificio3.childs += [paralelepipedo11,paralelepipedo12,paralelepipedo13,paralelepipedo14,paralelepipedo15]

    #Edificio completo completo
    Edificio=sg.SceneGraphNode("EdificioCompleto")
    Edificio.childs+=[Edificio1,Edificio2,Edificio3,paralelepipedo16,paralelepipedo17]

    return Edificio

def Empire(pipeline):
    #Cubo base color gris
    GreyCube = bs.createColorNormalsCube(128/255,128/255,128/255)
    gpuGreyCube = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuGreyCube)
    gpuGreyCube.fillBuffers(GreyCube.vertices,GreyCube.indices, GL_STATIC_DRAW)

    #Paralelepipedos que se usan para ensamblar el edificio
    paralelepipedo1=sg.SceneGraphNode("paralelepipedo1")
    paralelepipedo1.transform=tr.matmul([tr.translate(0,0,0.05),tr.scale(1,0.5,0.1)])
    paralelepipedo1.childs+=[gpuGreyCube]

    paralelepipedo2=sg.SceneGraphNode("paralelepipedo2")
    paralelepipedo2.transform=tr.matmul([tr.translate(0,0,0.25),tr.scale(0.9,0.4,0.5)])
    paralelepipedo2.childs+=[gpuGreyCube]

    paralelepipedo3=sg.SceneGraphNode("paralelepipedo3")
    paralelepipedo3.transform=tr.matmul([tr.translate(0,0,0.35),tr.scale(0.7,0.45,0.7)])
    paralelepipedo3.childs+=[gpuGreyCube]

    paralelepipedo4=sg.SceneGraphNode("paralelepipedo4")
    paralelepipedo4.transform=tr.matmul([tr.translate(0,0,1.05),tr.scale(0.6,0.4,2.1)])
    paralelepipedo4.childs+=[gpuGreyCube]

    paralelepipedo5=sg.SceneGraphNode("paralelepipedo5")
    paralelepipedo5.transform=tr.matmul([tr.translate(0,0,1.2),tr.scale(0.5,0.35,2.4)])
    paralelepipedo5.childs+=[gpuGreyCube]

    paralelepipedo6=sg.SceneGraphNode("paralelepipedo6")
    paralelepipedo6.transform=tr.matmul([tr.translate(0,0,1.3),tr.scale(0.45,0.3,2.6)])
    paralelepipedo6.childs+=[gpuGreyCube]

    paralelepipedo7=sg.SceneGraphNode("paralelepipedo7")
    paralelepipedo7.transform=tr.matmul([tr.translate(0,0,1.8),tr.scale(0.03,0.03,3.6)])
    paralelepipedo7.childs+=[gpuGreyCube]

    #Edificio completo completo
    Edificio=sg.SceneGraphNode("EdificioCompleto")
    Edificio.childs+=[paralelepipedo1,paralelepipedo2,paralelepipedo3,paralelepipedo4,paralelepipedo5,paralelepipedo6,paralelepipedo7]

    return Edificio

def Willis(pipeline):
    #Cubo base color gris
    GreyCube = bs.createColorNormalsCube(128/255,128/255,128/255)
    gpuGreyCube = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuGreyCube)
    gpuGreyCube.fillBuffers(GreyCube.vertices,GreyCube.indices, GL_STATIC_DRAW)

    #Paralelepipedos que se usan para ensamblar el edificio
    paralelepipedo1=sg.SceneGraphNode("paralelepipedo1")
    paralelepipedo1.transform=tr.matmul([tr.translate(0,0,0.8),tr.scale(0.6,0.6,1.6)])
    paralelepipedo1.childs+=[gpuGreyCube]

    paralelepipedo2=sg.SceneGraphNode("paralelepipedo2")
    paralelepipedo2.transform=tr.matmul([tr.translate(0.1,-0.1,0.95),tr.scale(0.4,0.4,1.9)])
    paralelepipedo2.childs+=[gpuGreyCube]

    paralelepipedo3=sg.SceneGraphNode("paralelepipedo3")
    paralelepipedo3.transform=tr.matmul([tr.translate(-0.1,0.1,0.95),tr.scale(0.4,0.4,1.9)])
    paralelepipedo3.childs+=[gpuGreyCube]

    paralelepipedo4=sg.SceneGraphNode("paralelepipedo4")
    paralelepipedo4.transform=tr.matmul([tr.translate(0.1,0,1.6),tr.scale(0.4,0.2,3.2)])
    paralelepipedo4.childs+=[gpuGreyCube]

    paralelepipedo5=sg.SceneGraphNode("paralelepipedo5")
    paralelepipedo5.transform=tr.matmul([tr.translate(0,-0.2,1.35),tr.scale(0.2,0.2,2.7)])
    paralelepipedo5.childs+=[gpuGreyCube]

    paralelepipedo6=sg.SceneGraphNode("paralelepipedo6")
    paralelepipedo6.transform=tr.matmul([tr.translate(-0.2,0,1.35),tr.scale(0.2,0.2,2.7)])
    paralelepipedo6.childs+=[gpuGreyCube]

    paralelepipedo7=sg.SceneGraphNode("paralelepipedo7")
    paralelepipedo7.transform=tr.matmul([tr.translate(0,0.2,1.35),tr.scale(0.2,0.2,2.7)])
    paralelepipedo7.childs+=[gpuGreyCube]

    #Edificio completo completo
    Edificio=sg.SceneGraphNode("EdificioCompleto")
    Edificio.childs+=[paralelepipedo1,paralelepipedo2,paralelepipedo3,paralelepipedo4,paralelepipedo5,paralelepipedo6,paralelepipedo7]

    return Edificio