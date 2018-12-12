from lodash/isFinite import _isFinite
from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA
class RSI(Indicator):
  def __init__(self, args = []):
    [period] = args
    super().__init__({
      'args': args,
      'id': 'rsi',
      'name': 'RSI(%f)' % (period),
      'seedPeriod': period
    })
    self._p = period
    self._uEMA = EMA([period])
    self._dEMA = EMA([period])
    self._prevInputValue = None

  def unserialize(self, args = []):
    return RSI(args)

  def reset(self):
    super().reset()
    self._prevInputValue = None
    if self._uEMA:
      self._uEMA.reset()
    if self._dEMA:
      self._dEMA.reset()

  def _ud(self, value):
    delta = 0 if self._prevInputValue == None else value - self._prevInputValue
    return {
      'u': delta if delta > 0 else 0,
      'd': delta * -1 if delta < 0 else 0
    }

  def _rs(self):
    uAvg = self._uEMA.v()
    dAvg = self._dEMA.v()
    return None if not _isFinite(uAvg) or not _isFinite(dAvg) or dAvg == 0 else uAvg / dAvg

  def update(self, value):
    if self._prevInputValue == None:
      return self.v()
    undefined = self._ud(value)
    self._uEMA.update(u)
    self._dEMA.update(d)
    rs = self._rs()
    if _isFinite(rs):
      super().update(100 - (100 / (1 + rs)))
    return self.v()

  def add(self, value):
    if self._prevInputValue == None:
      self._prevInputValue = value
    undefined = self._ud(value)
    self._uEMA.add(u)
    self._dEMA.add(d)
    rs = self._rs()
    if _isFinite(rs):
      super().add(100 - (100 / (1 + rs)))
      self._prevInputValue = value
    return self.v()


module.exports = RSI