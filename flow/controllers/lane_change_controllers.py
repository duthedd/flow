"""Contains a list of custom lane change controllers."""

from flow.controllers.base_lane_changing_controller import \
    BaseLaneChangeController


class SumoLaneChangeController(BaseLaneChangeController):
    """A controller used to enforce sumo lane-change dynamics on a vehicle."""

    def __init__(self, veh_id):
        super().__init__(veh_id, lane_change_params={})
        self.SumoController = True

    def get_lane_change_action(self, env):
        """See parent class."""
        return None


class StaticLaneChanger(BaseLaneChangeController):
    """A lane-changing model used to keep a vehicle in the same lane."""

    def get_lane_change_action(self, env):
        """See parent class."""
        return 0
