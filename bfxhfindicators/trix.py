from lodash/isFinite import _isFinite
from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA
class TRIX(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'trix',
      'name': 'TRIX(%f)' % (period),
      'seedPeriod': (period * 3) + 1
    })
    self._emaFirst = EMA([period])
    self._emaSecond = EMA([period])
    self._emaThird = EMA([period])

  def unserialize(self, args = []):
    return TRIX(args)

  def reset(self):
    super().reset()
    if self._emaFirst:
      self._emaFirst.reset()
    if self._emaSecond:
      self._emaSecond.reset()
    if self._emaThird:
      self._emaThird.reset()

  def update(self, v):
    self._emaFirst.update(v)
    self._emaSecond.update(self._emaFirst.v())
    self._emaThird.update(self._emaSecond.v())
    curr = self._emaThird.v()
    prev = self._emaThird.prev()
    if not _isFinite(curr) or not _isFinite(prev):
      return self.v()
    return super().update(((curr / prev) - 1) * 10000)

  def add(self, v):
    self._emaFirst.add(v)
    self._emaSecond.add(self._emaFirst.v())
    self._emaThird.add(self._emaSecond.v())
    curr = self._emaThird.v()
    prev = self._emaThird.prev()
    if not _isFinite(curr) or not _isFinite(prev):
      return self.v()
    return super().add(((curr / prev) - 1) * 10000)


