from lodash/isFinite import _isFinite
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

  def unserialize(self, args = []):
    return EMAVolume(args)

  def reset(self):
    super().reset()
    if self._ema:
      self._ema.reset()

  def update(self, candle):
    undefined = candle
    self._ema.update(vol)
    ema = self._ema.v()
    if _isFinite(ema):
      super().update(ema)
    return self.v()

  def add(self, candle):
    undefined = candle
    self._ema.add(vol)
    ema = self._ema.v()
    if _isFinite(ema):
      super().add(ema)
    return self.v()


