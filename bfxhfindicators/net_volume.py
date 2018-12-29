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
    if candle.close >= candle.open:
      return super().update(candle.vol)
    else:
      return super().update(-candle.vol)

  def add(self, candle):
    if candle.close >= candle.open:
      return super().add(candle.vol)
    else:
      return super().add(-candle.vol)


