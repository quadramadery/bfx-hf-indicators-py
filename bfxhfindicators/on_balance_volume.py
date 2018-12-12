from bfxhfindicators.indicator import Indicator
class OBV(Indicator):
  def __init__(self, args = []):
    super().__init__({
      'args': args,
      'id': 'obv',
      'name': 'OBV',
      'seedPeriod': 0,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._lastCandle = None

  def unserialize(self, args = []):
    return OBV(args)

  def reset(self):
    super().reset()
    self._lastCandle = None

  def update(self, candle):
    if self._lastCandle == None:
      return self.v()
    undefined = candle
    v = self.prev() if self.l() > 1 else 0
    obv = v
    if close > self._lastCandle.close:
      obv = v + vol
    else:
      if close < self._lastCandle.close:
      obv = v - vol
    return super().update(obv)

  def add(self, candle):
    if self._lastCandle == None:
      self._lastCandle = candle
      return self.v()
    undefined = candle
    v = self.v() if self.l() > 0 else 0
    obv = v
    if close > self._lastCandle.close:
      obv = v + vol
    else:
      if close < self._lastCandle.close:
      obv = v - vol
    super().add(obv)
    self._lastCandle = candle
    return self.v()


module.exports = OBV