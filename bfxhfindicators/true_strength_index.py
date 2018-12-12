from lodash/max import _max
from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA
class TSI(Indicator):
  def __init__(self, args = []):
    [ long, short, signal ] = args
    super().__init__({
      'args': args,
      'id': 'tsi',
      'name': 'TSI(%f, %f, %f)' % (long, short, signal),
      'seedPeriod': _max([long, short, signal])
    })
    self._pcEMA = EMA([long])
    self._pc2EMA = EMA([short])
    self._apcEMA = EMA([long])
    self._apc2EMA = EMA([short])
    self._sEMA = EMA([signal])
    self._lastPrice = None

  def unserialize(self, args = []):
    return TSI(args)

  def reset(self):
    super().reset()
    if self._pcEMA:
      self._pcEMA.reset()
    if self._pc2EMA:
      self._pc2EMA.reset()
    if self._apcEMA:
      self._apcEMA.reset()
    if self._apc2EMA:
      self._apc2EMA.reset()
    if self._sEMA:
      self._sEMA.reset()
    self._lastPrice = None

  def update(self, v):
    if not self._lastPrice:
      return self.v()
    pc = v - self._lastPrice
    apc = Math.abs(v - self._lastPrice)
    self._pcEMA.update(pc)
    self._apcEMA.update(apc)
    if self._pcEMA.ready():
      self._pc2EMA.update(self._pcEMA.v())
    else:
      return self.v()
    if self._apcEMA.ready():
      self._apc2EMA.update(self._apcEMA.v())
    else:
      return self.v()
    if not self._pc2EMA.ready() or not self._apc2EMA.ready():
      return self.v()
    tsi = 100 * (self._pc2EMA.v() / self._apc2EMA.v())
    self._sEMA.update(tsi)
    return super().update({
      'v': tsi,
      'signal': self._sEMA.v()
    })

  def add(self, v):
    if not self._lastPrice:
      self._lastPrice = v
      return self.v()
    pc = v - self._lastPrice
    apc = Math.abs(v - self._lastPrice)
    self._pcEMA.add(pc)
    self._apcEMA.add(apc)
    if self._pcEMA.ready():
      self._pc2EMA.add(self._pcEMA.v())
    else:
      return self.v()
    if self._apcEMA.ready():
      self._apc2EMA.add(self._apcEMA.v())
    else:
      return self.v()
    if not self._pc2EMA.ready() or not self._apc2EMA.ready():
      return self.v()
    tsi = 100 * (self._pc2EMA.v() / self._apc2EMA.v())
    self._sEMA.add(tsi)
    super().add({
      'v': tsi,
      'signal': self._sEMA.v()
    })
    self._lastPrice = v
    return self.v()

  def ready(self):
    return _isObject(self.v())


