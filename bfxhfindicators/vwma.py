from bignumber.js import BigN
from lodash/sum import _sum
from bfxhfindicators.indicator import Indicator
class VWMA(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'vwma',
      'name': 'VWMA (%f)' % (period),
      'seedPeriod': period,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._p = period
    self._buffer = []

  def unserialize(self, args = []):
    return VWMA(args)

  def reset(self):
    super().reset()
    self._buffer = []

  def update(self, candle):
    if len(self._buffer) == 0:
      self._buffer.append(candle)
    else:
      self._buffer[-1] = candle
    if len(self._buffer) < self._p:
      return self.v()
    
    volSum = 0
    sum = 0
    for i in range(0, len(self._buffer)):
      volSum = volSum + self._buffer[i].vol
    for i in range(0, len(self._buffer)):
      c = self._buffer[i]
      sum = sum + (c.close * c.vol.div(volSum))
    return super().update(sum)

  def add(self, candle):
    self._buffer.append(candle)
    if len(self._buffer) > self._p:
      del self._buffer[0]
    elif len(self._buffer) < self._p:
      return self.v()
    
    volSum = 0
    sum = 0
    for i in range(0, len(self._buffer)):
      volSum = volSum + self._buffer[i].vol
    for i in range(0, len(self._buffer)):
      c = self._buffer[i]
      sum = sum + (c.close * c.vol.div(volSum))
    return super().add(sum)


