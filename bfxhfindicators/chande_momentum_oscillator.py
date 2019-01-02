from bignumber.js import BigN
from lodash/sum import _sum
from bfxhfindicators.indicator import Indicator
class ChandeMO(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'chandemo',
      'name': 'ChandeMO (%f)' % (period),
      'seedPeriod': period,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._p = period
    self._buffer = []

  def unserialize(args = []):
    return ChandeMO(args)

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
    sU = _sum(map(lambda : close - open, filter(lambda : close > open, self._buffer)))
    sD = _sum(map(lambda : open - close, filter(lambda : close < open, self._buffer)))
    return super().update(sU - sD.div(sU + sD) * 100)

  def add(self, candle):
    self._buffer.append(candle)
    if len(self._buffer) > self._p:
      del self._buffer[0]
    elif len(self._buffer) < self._p:
      return
    sU = _sum(map(lambda : close - open, filter(lambda : close > open, self._buffer)))
    sD = _sum(map(lambda : open - close, filter(lambda : close < open, self._buffer)))
    return super().add(sU - sD.div(sU + sD) * 100)


