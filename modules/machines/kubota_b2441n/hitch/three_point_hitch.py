from modules.machines.kubota_b2441n.hitch.hitch_data import THREE_POINT_HITCH

class ThreePointHitch:

    def __init__(self):
        self.data=THREE_POINT_HITCH

    @property
    def category(self):
        return self.data["category"]

    @property
    def lift_capacity(self):
        return self.data["lift_capacity_kg"]

    @property
    def lift_height(self):
        return self.data["max_lift_height_mm"]

    @property
    def lower_link_length(self):
        return self.data["lower_link_length_mm"]

    @property
    def top_link_length(self):
        return self.data["top_link_length_mm"]

    def can_lift(self,weight_kg):
        return weight_kg<=self.lift_capacity
