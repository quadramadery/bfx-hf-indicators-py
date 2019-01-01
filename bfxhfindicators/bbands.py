from lodash/sum import _sum
from lodash/isFinite import _isFinite
from bfxhfindicators.sma import SMA
from bfxhfindicators.stddev import StdDeviation
from bfxhfindicators.indicator import Indicator
class BollingerBands(Indicator):
  def __init__(self, args = []):
    [ period = 20, mul = 2 ] = args
    super().__init__({
      'args': args,
      'id': 'bbands',
      'name': 'BBANDS(%f, %f)' % (period, mul),
      'seedPeriod': period
    })
    self._p = period
    self._m = mul
    self._ema = SMA([period])
    self._stddev = StdDeviation([period])

  def unserialize(self, args = []):
    return BollingerBands(args)

  def reset(self):
    super().reset()
    if self._ema:
      self._ema.reset()
    if self._stddev:
      self._stddev.reset()

  def update(self, value):
    self._ema.update(value)
    self._stddev.update(value)
    middle = self._ema.v()
    stddev = self._stddev.v()
    return super().update({
      'top': middle + (self._m * stddev),
      'middle': middle,
      'bottom': middle - (self._m * stddev)
    })

  def add(self, value):
    self._ema.add(value)
    self._stddev.add(value)
    middle = self._ema.v()
    stddev = self._stddev.v()
    return super().add({
      'top': middle + (self._m * stddev),
      'middle': middle,
      'bottom': middle - (self._m * stddev)
    })

  def ready(self):
    return _isFinite(self.v() or {}.middle)

  def crossed(self, target):
    if self.l() < 2:
      return false
    v = self.v().middle
    prev = self.prev().middle
    return v >= target and prev <= target or v <= target and prev >= target

  def avg(self, n = 2):
    return _sum(map(lambda v: v.middle, self.nValues(n))) / n


