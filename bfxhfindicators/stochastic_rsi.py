from lodash/isFinite import _isFinite
from lodash/min import _min
from lodash/max import _max
from bfxhfindicators.indicator import Indicator
from bfxhfindicators.sma import SMA
from bfxhfindicators.rsi import RSI
class StochasticRSI(Indicator):
  def __init__(self, args = []):
    [ lengthRSI, lengthStochastic, smoothStoch, smoothSignal ] = args
    super().__init__({
      'args': args,
      'id': 'stochrsi',
      'name': 'Stoch RSI(%f, %f, %f, %f)' % (lengthRSI, lengthStochastic, smoothStoch, smoothSignal),
      'seedPeriod': (lengthRSI + lengthStochastic) + smoothStoch
    })
    self._buffer = []
    self._l = lengthStochastic
    self._rsi = RSI([lengthRSI])
    self._smaStoch = SMA([smoothStoch])
    self._smaSignal = SMA([smoothSignal])

  def unserialize(args = []):
    return StochasticRSI(args)

  def reset(self):
    super().reset()
    self._buffer = []
    if self._rsi:
      self._rsi.reset()
    if self._smaStoch:
      self._smaStoch.reset()
    if self._smaSignal:
      self._smaSignal.reset()

  def update(self, v):
    self._rsi.update(v)
    rsi = self._rsi.v()
    if not isfinite(rsi):
      return self.v()
    if len(self._buffer) == 0:
      self._buffer.append(rsi)
    else:
      self._buffer[-1] = rsi
    if len(self._buffer) < self._l:
      return self.v()
    low = min(self._buffer)
    high = max(self._buffer)
    stoch = 1 if high == low else (rsi - low) / (high - low)
    self._smaStoch.update(stoch * 100)
    smaStoch = self._smaStoch.v()
    if not isfinite(smaStoch):
      return self.v()
    self._smaSignal.update(smaStoch)
    smaSignal = self._smaSignal.v()
    if isfinite(smaSignal):
      super().update({
        'v': smaStoch,
        'signal': smaSignal
      })
    return self.v()

  def add(self, v):
    self._rsi.add(v)
    rsi = self._rsi.v()
    if not isfinite(rsi):
      return self.v()
    self._buffer.append(rsi)
    if len(self._buffer) > self._l:
      del self._buffer[0]
    elif len(self._buffer) < self._l:
      return self.v()
    low = min(self._buffer)
    high = max(self._buffer)
    stoch = 1 if high == low else (rsi - low) / (high - low)
    self._smaStoch.add(stoch * 100)
    smaStoch = self._smaStoch.v()
    if not isfinite(smaStoch):
      return self.v()
    self._smaSignal.add(smaStoch)
    smaSignal = self._smaSignal.v()
    if isfinite(smaSignal):
      super().add({
        'v': smaStoch,
        'signal': smaSignal
      })
    return self.v()

  def ready(self):
    return _isObject(self.v())


