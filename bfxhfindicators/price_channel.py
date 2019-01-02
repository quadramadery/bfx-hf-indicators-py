from bfxhfindicators.indicator import Indicator
class PC(Indicator):
  def __init__(self, args = []):
    [ period, offset ] = args
    super().__init__({
      'args': args,
      'id': 'pc',
      'name': 'PC(%f, %f)' % (period, offset),
      'seedPeriod': period,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._p = period
    self._offset = offset
    self._l = period + offset
    self._buffer = []

  def unserialize(args = []):
    return PC(args)

  def reset(self):
    super().reset()
    self._buffer = []

  def update(self, candle):
    if len(self._buffer) == 0:
      self._buffer.append(candle)
    else:
      self._buffer[-1] = candle
    if len(self._buffer) < self._l:
      return super().update(0)
    upper = max(map(lambda c: c.high, self._buffer.slice(0, self._p)))
    lower = min(map(lambda c: c.low, self._buffer.slice(0, self._p)))
    return super().update({
      'upper': upper,
      'lower': lower,
      'center': (upper + lower) / 2
    })

  def add(self, candle):
    self._buffer.append(candle)
    if len(self._buffer) > self._l:
      del self._buffer[0]
    elif len(self._buffer) < self._l:
      return self.v()
    upper = max(map(lambda c: c.high, self._buffer.slice(0, self._p)))
    lower = min(map(lambda c: c.low, self._buffer.slice(0, self._p)))
    return super().add({
      'upper': upper,
      'lower': lower,
      'center': (upper + lower) / 2
    })

  def ready(self):
    return _isObject(self.v())


