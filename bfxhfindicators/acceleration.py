from lodash/isEmpty import _isEmpty
from bfxhfindicators.indicator import Indicator
from bfxhfindicators.roc import ROC
class Acceleration(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'acc',
      'name': 'Acceleration(%f)' % (period),
      'seedPeriod': period
    })
    self._roc = ROC([period])
    self._p = period

  def unserialize(self, args = []):
    return Acceleration(args)

  def reset(self):
    super().reset()
    self._buffer = []
    if self._roc:
      self._roc.reset()

  def update(self, value):
    self._roc.update(value)
    roc = self._roc.v()
    if roc == None:
      return
    if len(self._buffer) == 0:
      self._buffer.append(roc)
    else:
      self._buffer[-1] = roc
    if len(self._buffer) < self._p:
      return
    return super().update(roc - self._buffer[0])

  def add(self, value):
    self._roc.add(value)
    roc = self._roc.v()
    if roc == None:
      return
    if len(self._buffer) == self._p:
      super().add(roc - self._buffer[0])
    self._buffer.append(roc)
    if len(self._buffer) > self._p:
      del self._buffer[0]
    return self.v()


