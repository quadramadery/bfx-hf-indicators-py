from lodash/isFinite import _isFinite
from bfxhfindicators.indicator import Indicator
from bfxhfindicators.sma import SMA
class Envelope(Indicator):
  def __init__(self, args = []):
    [ length, percent ] = args
    super().__init__({
      'args': args,
      'id': 'env',
      'name': 'Env(%f, %f)' % (length, percent),
      'seedPeriod': length
    })
    self._sma = SMA([length])
    self._p = percent / 100

  def unserialize(args = []):
    return Envelope(args)

  def reset(self):
    super().reset()
    if self._sma:
      self._sma.reset()

  def update(self, v):
    self._sma.update(v)
    basis = self._sma.v()
    if not _isFinite(basis):
      return
    delta = basis * self._p
    return super().update({
      'upper': basis + delta,
      'basis': basis,
      'lower': basis - delta
    })

  def add(self, v):
    self._sma.add(v)
    basis = self._sma.v()
    if not _isFinite(basis):
      return
    delta = basis * self._p
    return super().add({
      'upper': basis + delta,
      'basis': basis,
      'lower': basis - delta
    })

  def ready(self):
    return _isObject(self.v())


