from lodash/max import _max
from lodash/min import _min
from bfxhfindicators.indicator import Indicator
from bfxhfindicators.sma import SMA
class Stochastic(Indicator):
  def __init__(self, args = []):
    [ period, smoothK, smoothD ] = args
    super().__init__({
      'args': args,
      'id': 'stoch',
      'name': 'Stoch(%f)' % (period),
      'seedPeriod': period,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._p = period
    self._kSMA = SMA([smoothK])
    self._dSMA = SMA([smoothD])

  def unserialize(self, args = []):
    return Stochastic(args)

  def reset(self):
    super().reset()
    if self._kSMA:
      self._kSMA.reset()
    if self._dSMA:
      self._dSMA.reset()
    self._buffer = []

  def update(self, candle):
    if len(self._buffer) == 0:
      self._buffer.append(candle)
    else:
      self._buffer[-1] = candle
    if len(self._buffer) < self._p:
      return self.v()
    close = candle.close
    lowestLow = _min(self._buffer.map(lambda c: c.low))
    highestHigh = _max(self._buffer.map(lambda c: c.high))
    k = 100 * ((close - lowestLow) / (highestHigh - lowestLow))
    self._kSMA.update(k)
    self._dSMA.update(self._kSMA.v())
    return super().add({
      'k': self._kSMA.v(),
      'd': self._dSMA.v()
    })

  def add(self, candle):
    self._buffer.append(candle)
    if len(self._buffer) > self._p:
      del self._buffer[0]
    else:
      if len(self._buffer) < self._p:
        return self.v()
    close = candle.close
    lowestLow = _min(self._buffer.map(lambda c: c.low))
    highestHigh = _max(self._buffer.map(lambda c: c.high))
    k = 100 * ((close - lowestLow) / (highestHigh - lowestLow))
    self._kSMA.add(k)
    self._dSMA.add(self._kSMA.v())
    return super().add({
      'k': self._kSMA.v(),
      'd': self._dSMA.v()
    })

  def ready(self):
    return _isObject(self.v())


