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
    v = self.prev() if self.l() > 1 else 0
    obv = v
    if candle.close > self._lastCandle.close:
      obv = v + candle.vol
    else:
      if candle.close < self._lastCandle.close:
        obv = v - candle.vol
    return super().update(obv)

  def add(self, candle):
    if self._lastCandle == None:
      self._lastCandle = candle
      return self.v()
    v = self.v() if self.l() > 0 else 0
    obv = v
    if candle.close > self._lastCandle.close:
      obv = v + candle.vol
    else:
      if candle.close < self._lastCandle.close:
        obv = v - candle.vol
    super().add(obv)
    self._lastCandle = candle
    return self.v()


