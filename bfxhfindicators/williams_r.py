from lodash/max import _max
from lodash/min import _min
from bfxhfindicators.indicator import Indicator
class WilliamsR(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'wir',
      'name': '%R (%f)' % (period),
      'seedPeriod': period,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._p = period
    self._buffer = []

  def unserialize(self, args = []):
    return WilliamsR(args)

  def reset(self):
    super().reset()
    self._buffer = []

  def update(self, candle):
    if len(self._buffer) == 0:
      self._buffer.append(candle)
    else:
      self._buffer[-1] = candle
    if len(self._buffer) == self._p:
      undefined = candle
      high = _max(self._buffer.map())
      low = _min(self._buffer.map())
      super().update(((high - close) / (high - low)) * -100)
    return self.v()

  def add(self, candle):
    self._buffer.append(candle)
    if len(self._buffer) > self._p:
      del self._buffer[0]
    else:
      if len(self._buffer) < self._p:
        return self.v()
    undefined = candle
    high = _max(self._buffer.map())
    low = _min(self._buffer.map())
    return super().add(((high - close) / (high - low)) * -100)


