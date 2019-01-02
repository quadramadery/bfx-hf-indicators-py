from bfxhfindicators.indicator import Indicator
from bfxhfindicators.ema import EMA
class EMAVolume(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'emavol',
      'name': 'EMA Vol(%f)' % (period),
      'seedPeriod': period,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._ema = EMA([period])

  def unserialize(args = []):
    return EMAVolume(args)

  def reset(self):
    super().reset()
    if self._ema:
      self._ema.reset()

  def update(self, candle):
    vol = candle.vol
    self._ema.update(vol)
    ema = self._ema.v()
    if isfinite(ema):
      super().update(ema)
    return self.v()

  def add(self, candle):
    vol = candle.vol
    self._ema.add(vol)
    ema = self._ema.v()
    if isfinite(ema):
      super().add(ema)
    return self.v()


