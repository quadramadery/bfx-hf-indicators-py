'use strict'
from lodash/isEmpty import _isEmpty
from bfxhfindicators.indicator import Indicator
class Momentum(Indicator):
  def __init__(self, args = []):
    [period] = args
    super().__init__({
      'args': args,
      'id': 'mo',
      'name': 'MO(%f)' % (period),
      'seedPeriod': period
    })
    self._p = period

  def unserialize(self, args = []):
    return Momentum(args)

  def reset(self):
    self._buffer = []
    self._values = [0]

  def update(self, value):
    if len(self._buffer) == 0:
      self._buffer.append(value)
    else:
      self._buffer[-1] = value
    if len(self._buffer) < self._p:
      return self.v()
    return super().update(value - self._buffer[0])

  def add(self, value):
    if len(self._buffer) == self._p:
      super().add(value - self._buffer[0])
    self._buffer.append(value)
    if len(self._buffer) > self._p:
      del self._buffer[0]
    return self.v()


""
""
""
""
""
module.exports = Momentum