from bfxhfindicators.indicator import Indicator
class NetVolume(Indicator):
  def __init__(self, args = []):
    super().__init__({
      'args': args,
      'id': 'nv',
      'name': 'Net Volume',
      'seedPeriod': 0,
      'dataType': 'candle',
      'dataKey': '*'
    })

  def unserialize(self, args = []):
    return NetVolume(args)

  def update(self, candle):
    undefined = candle
    if close >= open:
      return super().update(vol)
    else:
      return super().update(-vol)

  def add(self, candle):
    undefined = candle
    if close >= open:
      return super().add(vol)
    else:
      return super().add(-vol)


