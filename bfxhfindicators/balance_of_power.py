'use strict'
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

      def unserialize(self, args = []):
    return BOP(args)

      def update(self, candle = {}):
      undefined = candle
      if high == low:
        super().update(1)
      else:
        super().update((close - open) / (high - low))
      return self.v()

      def add(self, candle = {}):
        undefined = candle
        if high == low:
          super().add(1)
        else:
          super().add((close - open) / (high - low))
        return self.v()


""
""
""
""
""
module.exports = BOP