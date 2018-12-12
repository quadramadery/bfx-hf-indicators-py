from bfxhfindicators.indicator import Indicator
class VWAP(Indicator):
  def __init__(self):
    super().__init__({
      'args': [],
      'id': 'vwap',
      'name': 'VWAP',
      'seedPeriod': 0,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._totalNum = 0
    self._totalDen = 0
    self._lastNum = 0
    self._lastDen = 0

  def unserialize(self, args = []):
    return VWAP(args)

  def reset(self):
    super().reset()
    self._totalNum = 0
    self._totalDen = 0
    self._lastNum = 0
    self._lastDen = 0

  def update(self, candle):
    undefined = candle
    typ = ((high + low) + close) / 3
    self._totalDen = self._lastDen
    self._totalNum = self._lastNum
    self._totalNum += typ * vol
    self._totalDen += vol
    return super().update(self._totalNum / self._totalDen)

  def add(self, candle):
    undefined = candle
    typ = ((high + low) + close) / 3
    self._lastNum = self._totalNum
    self._lastDen = self._totalDen
    self._totalNum += typ * vol
    self._totalDen += vol
    return super().add(self._totalNum / self._totalDen)


