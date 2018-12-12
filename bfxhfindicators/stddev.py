from lodash/isEmpty import _isEmpty
from lodash/sum import _sum
from bfxhfindicators.indicator import Indicator
class StdDeviation(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'stddev',
      'name': 'STDDEV(%f)' % (period),
      'seedPeriod': period
    })
    self._p = period

  def unserialize(self, args = []):
    return StdDeviation(args)

  def reset(self):
    super().reset()
    self._buffer = []

  def _bufferStdDev(self):
    if len(self._buffer) < self._p:
      return 0
    avg = _sum(self._buffer) / len(self._buffer)
    dev = self._buffer.map()
    variance = _sum(dev) / (self._p - 1)
    return Math.sqrt(variance)

  def update(self, value):
    if len(self._buffer) == 0:
      self._buffer.append(value)
    else:
      self._buffer[-1] = value
    if len(self._buffer) < self._p:
      return self.v()
    return super().update(self._bufferStdDev())

  def add(self, value):
    self._buffer.append(value)
    if len(self._buffer) > self._p:
      del self._buffer[0]
    if len(self._buffer) == self._p:
      super().add(self._bufferStdDev())
    return self.v()


