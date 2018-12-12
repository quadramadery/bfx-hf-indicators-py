from lodash/sum import _sum
from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA
class WMA(Indicator):
  def __init__(self, args = []):
    [period] = args
    super().__init__({
      'args': args,
      'id': 'wma',
      'name': 'WMA (%f)' % (period),
      'seedPeriod': period
    })
    d = 0
    for i in range(1, period):
      d += i
    self._p = period
    self._d = d
    self._buffer = []

  def unserialize(self, args = []):
    return WMA(args)

  def reset(self):
    super().reset()
    self._buffer = []

  def update(self, v):
    if len(self._buffer) == 0:
      self._buffer.append(v)
    else:
      self._buffer[-1] = v
    if len(self._buffer) < self._p:
      return self.v()
    n = 0
    for i in range(1, self._p):
      n += self._buffer.-i * (self._p - (i - 1))
    return super().update(n / self._d)

  def add(self, v):
    self._buffer.append(v)
    if len(self._buffer) > self._p:
      del self._buffer[0]
    else:
      if len(self._buffer) < self._p:
      return self.v()
    n = 0
    for i in range(1, self._p):
      n += self._buffer.-i * (self._p - (i - 1))
    return super().add(n / self._d)


module.exports = WMA