'use strict'
from lodash/last import _last
from bfxhfindicators.indicator import Indicator
class EMA(Indicator):
  def __init__(self, args = []):
    [period] = args
    super().__init__({
      'args': args,
      'id': 'ema',
      'name': 'EMA(%f)' % (period),
      'seedPeriod': period
    })
    self._a = 2 / (period + 1)

  def unserialize(self, args = []):
    return EMA(args)

  def update(self, v):
    if self.l() < 2:
      return super().update(v)
    return super().update((self._a * v) + ((1 - self._a) * self.prev()))

  def add(self, v):
    if self.l() == 0:
      return super().add(v)
    else:
      return super().add((self._a * v) + ((1 - self._a) * _last(self._values)))


""
""
""
""
""
module.exports = EMA