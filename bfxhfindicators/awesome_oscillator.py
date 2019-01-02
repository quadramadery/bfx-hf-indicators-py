from bfxhfindicators.sma import SMA
from bfxhfindicators.indicator import Indicator
class AO(Indicator):
  def __init__(self, args = []):
    super().__init__({
      'args': args,
      'id': 'ao',
      'name': 'AO',
      'seedPeriod': 34,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._smaShort = SMA([5])
    self._smaLong = SMA([34])

  def unserialize(args = []):
    return AO(args)

  def reset(self):
    super().reset()
    if self._smaShort:
      self._smaShort.reset()
    if self._smaLong:
      self._smaLong.reset()

  def update(self, candle = {}):
    v = (candle.high + candle.low) / 2
    self._smaShort.update(v)
    self._smaLong.update(v)
    return super().update(self._smaShort.v() - self._smaLong.v())

  def add(self, candle = {}):
    v = (candle.high + candle.low) / 2
    self._smaShort.add(v)
    self._smaLong.add(v)
    return super().add(self._smaShort.v() - self._smaLong.v())


