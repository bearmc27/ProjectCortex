from __future__ import print_function

"""
Objective:
- Kick-starting the program.
- Read configuration file and pass it to other class
"""
from TrackingSystem import TrackingSystem as tracking_sys

# GUI testing


def main():
    tracking_system = tracking_sys.TrackingSystem()

    # # initialize the video stream and allow the camera sensor to warmup
    # print("[INFO] warming up camera...")
    # # src=0 mean webcam device 0, i believe similar to cv2.VideoCapture(0)
    # vs = VideoStream(src = 0).start()
    # time.sleep(2.0)
    #
    # # start the app
    # pba = PhotoBoothApp(vs)
    # pba.root.mainloop()


if __name__ == '__main__':
    main()
