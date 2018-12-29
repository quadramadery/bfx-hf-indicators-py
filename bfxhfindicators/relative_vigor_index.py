from bignumber.js import BigN
from bfxhfindicators.sma import SMA
from bfxhfindicators.indicator import Indicator
class RVGI(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'rvgi',
      'name': 'RVGI(%f)' % (period),
      'seedPeriod': period,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._numeratorSMA = SMA([period])
    self._denominatorSMA = SMA([period])

  def unserialize(self, args = []):
    return RVGI(args)

  def reset(self):
    super().reset()
    if self._numeratorSMA:
      self._numeratorSMA.reset()
    if self._denominatorSMA:
      self._denominatorSMA.reset()
    self._buffer = []

  def calc(self, candle, buffer):
    barA = candle.close - candle.open
    barB = buffer[2].candle.close - buffer[2].candle.open
    barC = buffer[1].candle.close - buffer[1].candle.open
    barD = buffer[0].candle.close - buffer[0].candle.open
    RVGI.calc(candle, self._buffer).num = ((barA + (barB * 2)) + (barC * 2)) + barD.div(6)
    e = candle.high - candle.low
    f = buffer[2].candle.high - buffer[2].candle.low
    g = buffer[1].candle.high - buffer[1].candle.low
    h = buffer[0].candle.high - buffer[0].candle.low
    RVGI.calc(candle, self._buffer).den = ((e + (f * 2)) + (g * 2)) + h.div(6)
    return {
      'RVGI.calc(candle, self._buffer).num': RVGI.calc(candle, self._buffer).num,
      'RVGI.calc(candle, self._buffer).den': RVGI.calc(candle, self._buffer).den
    }

  def update(self, candle):
    if len(self._buffer) == 0:
      self._buffer.append(candle)
    else:
      self._buffer[-1] = candle
    if len(self._buffer) < 4:
      return super().update(0)
    self._numeratorSMA.update(RVGI.calc(candle, self._buffer).num)
    self._denominatorSMA.update(RVGI.calc(candle, self._buffer).den)
    rvi = self._numeratorSMA.v() / self._denominatorSMA.v()
    signal = 0
    if self.l() >= 3:
      i = self.v().rvi
      j = self.prev(1).rvi
      k = self.prev(2).rvi
      signal = ((rvi + (i * 2)) + (j * 2)) + k.div(6)
    return super().update({
      'rvi': rvi,
      'signal': signal
    })

  def add(self, candle):
    self._buffer.append(candle)
    if len(self._buffer) > 4:
      del self._buffer[0]
    else:
      if len(self._buffer) < 4:
        return self.v()
    self._numeratorSMA.add(RVGI.calc(candle, self._buffer).num)
    self._denominatorSMA.add(RVGI.calc(candle, self._buffer).den)
    rvi = self._numeratorSMA.v() / self._denominatorSMA.v()
    signal = 0
    if self.l() >= 4:
      i = self.prev(1).rvi
      j = self.prev(2).rvi
      k = self.prev(3).rvi
      signal = ((rvi + (i * 2)) + (j * 2)) + k.div(6)
    return super().add({
      'rvi': rvi,
      'signal': signal
    })

  def ready(self):
    return _isObject(self.v())


