from selfdrive.mapd.lib.WayRelation import WayRelation
from selfdrive.mapd.lib.geo import DIRECTION
from selfdrive.config import Conversions as CV

class DPWayRelation(WayRelation):
  @property
  def speed_limit(self):
    self._speed_limit = super().speed_limit
    if self._speed_limit is not None:
      return self._speed_limit

    # make sure we have priority here, e.g. stop sign should have higher priority than roundabout

    # stop sign
    stop_sign_str = self.way.tags.get("highway")
    if stop_sign_str is not None and stop_sign_str == "stop":
      direction = self.way.tags.get("direction")
      limit_to = None
      # if we don't have a direction tag, we slow it down to 5km/h
      if direction is None:
        limit_to = 5.
      # if we have direction and it's either forward or both, then we slow it down to 1km/h
      else:
        if direction == "both":
          limit_to = 1.
        elif self.direction == DIRECTION.FORWARD and direction == "forward":
          limit_to = 1.
        elif self.direction == DIRECTION.BACKWARD and direction == "backward":
          limit_to = 1.
      if limit_to is not None:
        self._speed_limit = limit_to * CV.KPH_TO_MS
        return self._speed_limit

    # roundabout, by arne
    junction_string = self.way.tags.get("junction")
    if junction_string is not None and junction_string == "roundabout":
      self._speed_limit = 25.0 * CV.KPH_TO_MS
      return self._speed_limit

    return self._speed_limit
