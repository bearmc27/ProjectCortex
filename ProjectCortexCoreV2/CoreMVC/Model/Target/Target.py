class Target:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def get_radius(self):
        return self.radius

    @staticmethod
    def find_2_targets_middle(target0, target1):
        """return x, y of middle point"""
        return int((target0.x + target1.x) / 2), int((target0.y + target1.y) / 2)
