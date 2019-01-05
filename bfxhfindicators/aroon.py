from lodash/findIndex import _findIndex
from bfxhfindicators.indicator import Indicator
class Aroon(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'aroon',
      'name': 'Aroon(%f)' % (period),
      'seedPeriod': period
    })
    self._p = period

  def unserialize(args = []):
    return Aroon(args)

  def reset(self):
    super().reset()
    self._buffer = []

  def update(self, value):
    if len(self._buffer) == 0:
      self._buffer.append(value)
    else:
      self._buffer[-1] = value
    if len(self._buffer) < self._p:
      return
    max = max(self._buffer)
    min = min(self._buffer)
    daysSinceMax = len(self._buffer) - _findIndex(self._buffer, lambda v: v == max)
    daysSinceMin = len(self._buffer) - _findIndex(self._buffer, lambda v: v == min)
    return super().update({
      'up': ((self._p - daysSinceMax) / self._p) * 100,
      'down': ((self._p - daysSinceMin) / self._p) * 100
    })

  def add(self, value):
    self._buffer.append(value)
    if len(self._buffer) > self._p:
      del self._buffer[0]
    elif len(self._buffer) < self._p:
      return
    max = max(self._buffer)
    min = min(self._buffer)
    daysSinceMax = len(self._buffer) - _findIndex(self._buffer, lambda v: v == max)
    daysSinceMin = len(self._buffer) - _findIndex(self._buffer, lambda v: v == min)
    return super().add({
      'up': ((self._p - daysSinceMax) / self._p) * 100,
      'down': ((self._p - daysSinceMin) / self._p) * 100
    })

  def ready(self):
    return isfinite(self.v() or {}.up)

  def crossed(self):
    return false

  def avg(self, n = 2):
    return {
      'up': sum(map(lambda v: v.up, self.nValues(n))) / n,
      'down': sum(map(lambda v: v.down, self.nValues(n))) / n
    }


