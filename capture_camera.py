from picamera import PiCamera
from time import sleep
import os

camera = PiCamera()

if __name__ == "__main__":
    # python program to check if a directory exists
    path = "./camera"
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print("The new directory is created!")

    i = 0
    while True:
        camera.start_preview()
        camera.capture("./camera/image%s.jpg" % i)
        print(f"image {i}")
        i += 1
        camera.stop_preview()
        sleep(5)
