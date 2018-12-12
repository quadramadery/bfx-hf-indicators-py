from bfxhfindicators.indicator import Indicator
class PVT(Indicator):
  def __init__(self, args = []):
    super().__init__({
      'args': args,
      'id': 'pvt',
      'name': 'PVT',
      'seedPeriod': 0,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._lastCandle = None

  def unserialize(self, args = []):
    return PVT(args)

  def reset(self):
    super().reset()
    self._lastCandle = None

  def update(self, candle):
    if self._lastCandle == None:
      return self.v()
    undefined = candle
    pvt = ((close - self._lastCandle.close) / self._lastCandle.close) * vol
    v = self.prev() if self.l() > 1 else 0
    return super().update(pvt + v)

  def add(self, candle):
    if self._lastCandle == None:
      self._lastCandle = candle
      return self.v()
    undefined = candle
    pvt = ((close - self._lastCandle.close) / self._lastCandle.close) * vol
    v = self.v() if self.l() > 0 else 0
    super().add(pvt + v)
    self._lastCandle = candle
    return self.v()


module.exports = PVT