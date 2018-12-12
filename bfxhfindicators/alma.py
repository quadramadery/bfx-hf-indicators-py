from lodash/isEmpty import _isEmpty
from bignumber.js import BigN
from bfxhfindicators.indicator import Indicator
class ALMA(Indicator):
  def __init__(self, args = []):
    [ period, offset, sigma ] = args
    super().__init__({
      'args': args,
      'id': 'alma',
      'name': 'ALMA(%f, %f, %f)' % (period, offset, sigma),
      'seedPeriod': period
    })
    self._p = period
    self._offset = offset
    self._s = sigma

  def unserialize(self, args = []):
    return ALMA(args)

  def calc(self, buffer, period, offset, sigma):
    m = offset * (period - 1)
    s = period / sigma
    windowSum = 0
    sum = 0
    for i in range(0, period):
      ex = Math.exp(-1 * (Math.pow(i - m, 2) / (2 * Math.pow(s, 2))))
      windowSum += ex * buffer[i]
      sum += ex
    return windowSum / sum

  def reset(self):
    super().reset()
    self._buffer = []

  def update(self, value):
    if len(self._buffer) == 0:
      self._buffer.append(value)
    else:
      self._buffer[-1] = value
    if len(self._buffer) < self._p:
      return
    return super().update(ALMA.calc(self._buffer, self._p, self._offset, self._s))

  def add(self, value):
    self._buffer.append(value)
    if len(self._buffer) > self._p:
      del self._buffer[0]
    return super().add(ALMA.calc(self._buffer, self._p, self._offset, self._s))


