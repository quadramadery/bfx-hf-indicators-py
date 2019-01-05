from bfxhfindicators.indicator import Indicator
class SMA(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'sma',
      'name': 'SMA(%f)' % (period),
      'seedPeriod': period
    })
    self._p = period

  def unserialize(args = []):
    return SMA(args)

  def reset(self):
    super().reset()
    self._buffer = []

  def update(self, value):
    if len(self._buffer) == 0:
      self._buffer.append(value)
    else:
      self._buffer[-1] = value
    if len(self._buffer) < self._p:
      return self.v()
    return super().update(sum(self._buffer) / self._p)

  def add(self, value):
    self._buffer.append(value)
    if len(self._buffer) > self._p:
      del self._buffer[0]
    return super().add(sum(self._buffer) / self._p)


