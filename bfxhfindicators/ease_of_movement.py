from bignumber.js import BigN
from lodash/isFinite import _isFinite
from bfxhfindicators.indicator import Indicator
from bfxhfindicators.sma import SMA
class EOM(Indicator):
  def __init__(self, args = []):
    [divisor, length] = args
    super().__init__({
      'args': args,
      'id': 'eom',
      'name': 'EOM(%f, %f)' % (divisor, length),
      'seedPeriod': length,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._d = divisor
    self._sma = SMA([length])
    self._lastCandle = None

  def unserialize(self, args = []):
    return EOM(args)

  def reset(self):
    super().reset()
    if self._sma:
      self._sma.reset()
    self._lastCandle = None

  def update(self, candle):
    if not self._lastCandle:
      return
    high = candle.high
    low = candle.low
    vol = candle.vol
    lastHigh = self._lastCandle.high
    lastLow = self._lastCandle.low
    moved = high + low.div(2) - lastHigh + lastLow.div(2)
    boxRatio = vol.div(self._d).div(high - low)
    eom = moved.div(boxRatio)
    self._sma.update(eom.toNumber())
    v = self._sma.v()
    if _isFinite(v):
      super().update(v)
    return self.v()

  def add(self, candle):
    if not self._lastCandle:
      self._lastCandle = candle
      return
    high = candle.high
    low = candle.low
    vol = candle.vol
    lastHigh = self._lastCandle.high
    lastLow = self._lastCandle.low
    moved = high + low.div(2) - lastHigh + lastLow.div(2)
    boxRatio = 1 if candle.high == candle.low else vol.div(self._d).div(high - low)
    eom = moved.div(boxRatio)
    self._sma.add(eom.toNumber())
    v = self._sma.v()
    if _isFinite(v):
      super().add(v)
    self._lastCandle = candle
    return self.v()


module.exports = EOM