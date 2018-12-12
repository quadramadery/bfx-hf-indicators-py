from bfxhfindicators.indicator import Indicator
from bfxhfindicators.sma import SMA
class DPO(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'dpo',
      'name': 'DPO(%f)' % (period),
      'seedPeriod': period
    })
    self._pricePeriod = Math.floor(period / 2) + 1
    self._sma = SMA([period])

  def unserialize(self, args = []):
    return DPO(args)

  def reset(self):
    super().reset()
    if self._sma:
      self._sma.reset()

  def update(self, v):
    self._sma.update(v)
    return super().update(v - self._sma.prev(self._pricePeriod - 1))

  def add(self, v):
    self._sma.add(v)
    return super().add(v - self._sma.prev(self._pricePeriod))


