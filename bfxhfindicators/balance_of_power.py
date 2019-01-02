from bfxhfindicators.indicator import Indicator
class BOP(Indicator):
  def __init__(self, args = []):
    super().__init__({
      'args': args,
      'id': 'bop',
      'name': 'Balance of Power',
      'seedPeriod': 0,
      'dataType': 'candle',
      'dataKey': '*'
    })

  def unserialize(args = []):
    return BOP(args)

  def update(self, candle = {}):
    if candle.high == candle.low:
      super().update(1)
    else:
      super().update((candle.close - candle.open) / (candle.high - candle.low))
    return self.v()

  def add(self, candle = {}):
    if candle.high == candle.low:
      super().add(1)
    else:
      super().add((candle.close - candle.open) / (candle.high - candle.low))
    return self.v()


