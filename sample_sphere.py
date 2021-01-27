"""Sphere sample application"""
import time
import math
import pygame

from quaternion import Quaternion

from scene import Scene
from object3d import Object3d
from camera import Camera
from mesh import Mesh
from material import Material
from color import Color
from vector3 import Vector3

# Define a main function, just to keep things nice and tidy
def main():
    """Main function, it implements the application loop"""
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res_x = 640
    res_y = 480

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("TestScene")
    scene.camera = Camera(False, res_x, res_y)

    # Moves the camera back 2 units
    scene.camera.position -= Vector3(0, 0, 2)

    # Create a sphere and place it in a scene, at position (0,0,0)
    obj1 = Object3d("TestObject")
    obj1.scale = Vector3(1, 1, 1)
    obj1.position = Vector3(0, 0, 0)
    obj1.mesh = Mesh.create_sphere((1, 1, 1), 12, 12)
    obj1.material = Material(Color(1, 0, 0, 1), "TestMaterial1")
    scene.add_object(obj1)

    # Specify the rotation of the object. It will rotate 15 degrees around the axis given,
    # every second
    angle = 15
    axis = Vector3(1, 0.7, 0.2)
    axis.normalize()

    # Timer
    delta_time = 0
    prev_time = time.time()

    pygame.mouse.set_visible(True)
    pygame.event.set_grab(False)

    # Game loop, runs forever
    while True:
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if event.type == pygame.QUIT:
                # Exits the application immediately
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                #ESQUERDA E DIREITA (EIXO Y)
                elif event.key == pygame.K_LEFT:
                    ax = (axis * math.radians(angle) * delta_time)

                    q = Quaternion.AngleAxis(Vector3(0, 1, 0), math.radians(angle) * delta_time)
                    obj1.rotation = q * obj1.rotation
                elif event.key == pygame.K_RIGHT:
                    ax = (axis * math.radians(angle) * delta_time)

                    q = Quaternion.AngleAxis(Vector3(0, -1, 0), math.radians(angle) * delta_time)
                    obj1.rotation = q * obj1.rotation
                #CIMA E BAIXO (EIXO X)
                elif event.key == pygame.K_UP:
                    ax = (axis * math.radians(angle) * delta_time)

                    q = Quaternion.AngleAxis(Vector3(1, 0, 0), math.radians(angle) * delta_time)
                    obj1.rotation = q * obj1.rotation
                #PgUP PgDOWN (EIXO Z)
                elif event.key == pygame.K_PAGEUP:
                    ax = (axis * math.radians(angle) * delta_time)

                    q = Quaternion.AngleAxis(Vector3(0, 0, 1), math.radians(angle) * delta_time)
                    obj1.rotation = q * obj1.rotation
                elif event.key == pygame.K_PAGEDOWN:
                    ax = (axis * math.radians(angle) * delta_time)

                    q = Quaternion.AngleAxis(Vector3(0, 0, -1), math.radians(angle) * delta_time)
                    obj1.rotation = q * obj1.rotation
                #W e S (NORTE E SUL)
                elif event.key == pygame.K_w:
                    obj1.position += Vector3(0, 1, 0)
                elif event.key == pygame.K_s:
                    obj1.position += Vector3(0, -1, 0)
                #A e D (OESTE E ESTE)
                elif event.key == pygame.K_a:
                    obj1.position += Vector3(1, 0, 0)
                elif event.key == pygame.K_d:
                    obj1.position += Vector3(-1, 0, 0)
                #Q e E (FRENTE E TRAS)
                elif event.key == pygame.K_q:
                    obj1.position += Vector3(0, 0, 1)
                elif event.key == pygame.K_e:
                    obj1.position += Vector3(0, 0, -1)

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0, 0, 0))

        # Rotates the object, considering the time passed (not linked to frame rate)
        #ax = (axis * math.radians(angle) * delta_time)

        #q = Quaternion.AngleAxis(axis, math.radians(angle) * delta_time)
        #obj1.rotation = q * obj1.rotation

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()


# Run the main function
main()
