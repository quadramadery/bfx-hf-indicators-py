from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA
class MACD(Indicator):
  def __init__(self, args = []):
    [ fastMA, slowMA, signalMA ] = args
    super().__init__({
      'args': args,
      'id': 'macd',
      'name': 'MACD(%f,%f,%f)' % (fastMA, slowMA, signalMA),
      'seedPeriod': Math.max(fastMA, slowMA) + signalMA
    })
    self._slowEMA = EMA([slowMA])
    self._fastEMA = EMA([fastMA])
    self._signalEMA = EMA([signalMA])

  def unserialize(self, args = []):
    return MACD(args)

  def reset(self):
    super().reset()
    if self._slowEMA:
      self._slowEMA.reset()
    if self._fastEMA:
      self._fastEMA.reset()
    if self._signalEMA:
      self._signalEMA.reset()

  def update(self, value):
    slowEMA = self._slowEMA.update(value)
    fastEMA = self._fastEMA.update(value)
    macd = fastEMA - slowEMA
    signalEMA = self._signalEMA.update(macd)
    histogram = macd - signalEMA
    return super().update({
      'macd': macd,
      'signal': signalEMA,
      'histogram': histogram
    })

  def add(self, value):
    slowEMA = self._slowEMA.add(value)
    fastEMA = self._fastEMA.add(value)
    macd = fastEMA - slowEMA
    signalEMA = self._signalEMA.add(macd)
    histogram = macd - signalEMA
    return super().add({
      'macd': macd,
      'signal': signalEMA,
      'histogram': histogram
    })

  def ready(self):
    return _isObject(self.v())


