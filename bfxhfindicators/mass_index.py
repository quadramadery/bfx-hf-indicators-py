from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA
class MassIndex(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'mi',
      'name': 'Mass Index (%f)' % (period),
      'seedPeriod': 9 + period,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._smoothing = period
    self._singleEMA = EMA([9])
    self._doubleEMA = EMA([9])
    self._buffer = []

  def unserialize(args = []):
    return MassIndex(args)

  def reset(self):
    super().reset()
    self._buffer = []
    if self._singleEMA:
      self._singleEMA.reset()
    if self._doubleEMA:
      self._doubleEMA.reset()

  def update(self, candle):
    self._singleEMA.update(candle.high - candle.low)
    self._doubleEMA.update(self._singleEMA.v())
    if len(self._buffer) == 0:
      self._buffer.append(self._singleEMA.v() / self._doubleEMA.v())
    else:
      self._buffer[-1] = self._singleEMA.v() / self._doubleEMA.v()
    if len(self._buffer) < self._smoothing:
      return self.v()
    return super().update(_sum(self._buffer))

  def add(self, candle):
    self._singleEMA.add(candle.high - candle.low)
    self._doubleEMA.add(self._singleEMA.v())
    self._buffer.append(self._singleEMA.v() / self._doubleEMA.v())
    if len(self._buffer) > self._smoothing:
      del self._buffer[0]
    elif len(self._buffer) < self._smoothing:
      return self.v()
    return super().add(_sum(self._buffer))


