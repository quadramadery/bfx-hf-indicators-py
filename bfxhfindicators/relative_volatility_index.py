from lodash/isFinite import _isFinite
from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA
from bfxhfindicators.stddev import StdDev
class RVI(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'rvi',
      'name': 'RVI(%f)' % (period),
      'seedPeriod': period
    })
    self._stddev = StdDev([period])
    self._uEMA = EMA([period])
    self._dEMA = EMA([period])
    self._prevInputValue = None

  def unserialize(self, args = []):
    return RVI(args)

  def reset(self):
    super().reset()
    if self._stddev:
      self._stddev.reset()
    if self._uEMA:
      self._uEMA.reset()
    if self._dEMA:
      self._dEMA.reset()
    self._prevInputValue = None

  def _ud(self, candlePrice, stddev):
    if self._prevInputValue == None:
      return {
        'self._ud(value, self._stddev.v()).u': 0,
        'self._ud(value, self._stddev.v()).d': 0
      }
    else:
      if candlePrice > self._prevInputValue:
        return {
          'self._ud(value, self._stddev.v()).u': stddev,
          'self._ud(value, self._stddev.v()).d': 0
        }
      else:
        if candlePrice < self._prevInputValue:
          return {
            'self._ud(value, self._stddev.v()).u': 0,
            'self._ud(value, self._stddev.v()).d': stddev
          }
        else:
          return {
            'self._ud(value, self._stddev.v()).u': 0,
            'self._ud(value, self._stddev.v()).d': 0
          }

  def update(self, value):
    if self._prevInputValue == None:
      return self.v()
    self._stddev.update(value)
    stddev = self._stddev.v()
    if not _isFinite(stddev):
      return self.v()
    self._uEMA.update(self._ud(value, self._stddev.v()).u)
    self._dEMA.update(self._ud(value, self._stddev.v()).d)
    uSum = self._uEMA.v()
    dSum = self._dEMA.v()
    if uSum == dSum:
      return super().update(0)
    else:
      return super().update(100 * (uSum / (uSum + dSum)))

  def add(self, value):
    if self._prevInputValue == None:
      self._prevInputValue = value
      return self.v()
    self._stddev.add(value)
    stddev = self._stddev.v()
    if not _isFinite(stddev):
      return self.v()
    self._uEMA.add(self._ud(value, self._stddev.v()).u)
    self._dEMA.add(self._ud(value, self._stddev.v()).d)
    uSum = self._uEMA.v()
    dSum = self._dEMA.v()
    if uSum == dSum:
      super().add(0)
    else:
      super().add(100 * (uSum / (uSum + dSum)))
    self._prevInputValue = value
    return self.v()


