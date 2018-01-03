from CoreMVC.Model.Camera.Camera import Camera


class RgbCamera(Camera):
    """
        Include RGB camera logic model
    """

    def __init__(self,camera_index):
        super().__init__(camera_index = camera_index)
