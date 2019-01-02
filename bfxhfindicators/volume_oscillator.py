from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA
class VO(Indicator):
  def __init__(self, args = []):
    [ shortPeriod, longPeriod ] = args
    super().__init__({
      'args': args,
      'id': 'vo',
      'name': 'VO(%f, %f)' % (shortPeriod, longPeriod),
      'seedPeriod': longPeriod,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._shortEMA = EMA([shortPeriod])
    self._longEMA = EMA([longPeriod])

  def unserialize(args = []):
    return VO(args)

  def reset(self):
    super().reset()
    if self._shortSMA:
      self._shortSMA.reset()
    if self._longSMA:
      self._longSMA.reset()

  def update(self, candle):
    vol = candle.vol
    self._shortEMA.update(vol)
    self._longEMA.update(vol)
    short = self._shortEMA.v()
    long = self._longEMA.v()
    if long == 0:
      return super().update(0)
    return super().update(((short - long) / long) * 100)

  def add(self, candle):
    vol = candle.vol
    self._shortEMA.add(vol)
    self._longEMA.add(vol)
    short = self._shortEMA.v()
    long = self._longEMA.v()
    if long == 0:
      return super().add(0)
    return super().add(((short - long) / long) * 100)


