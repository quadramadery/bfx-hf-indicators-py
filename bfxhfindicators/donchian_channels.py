from lodash/max import _max
from lodash/min import _min
from bfxhfindicators.indicator import Indicator
class DC(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'dc',
      'name': 'DC (%f)' % (period),
      'seedPeriod': period,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._p = period
    self._buffer = []

  def unserialize(args = []):
    return DC(args)

  def reset(self):
    super().reset()
    self._buffer = []

  def update(self, candle):
    if len(self._buffer) == 0:
      self._buffer.append(candle)
    else:
      self._buffer[-1] = candle
    if len(self._buffer) < self._p:
      return
    max = max(map(lambda c: c.high, self._buffer))
    min = min(map(lambda c: c.low, self._buffer))
    return super().update({
      'upper': max,
      'middle': (max + min) / 2,
      'lower': min
    })

  def add(self, candle):
    self._buffer.append(candle)
    if len(self._buffer) > self._p:
      del self._buffer[0]
    elif len(self._buffer) < self._p:
      return
    max = max(map(lambda c: c.high, self._buffer))
    min = min(map(lambda c: c.low, self._buffer))
    return super().add({
      'upper': max,
      'middle': (max + min) / 2,
      'lower': min
    })

  def ready(self):
    return _isObject(self.v())


