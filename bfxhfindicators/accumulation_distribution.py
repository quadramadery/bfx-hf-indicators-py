from math import isfinite
from bfxhfindicators.indicator import Indicator
class AccumulationDistribution(Indicator):
  def __init__(self, args = []):
    super().__init__({
      'args': args,
      'id': 'ad',
      'name': 'Accum/Dist',
      'dataType': 'candle',
      'dataKey': '*'
    })

  def unserialize(args = []):
    return AccumulationDistribution(args)

  def reset(self):
    super().reset()

  def update(self, candle):
    moneyFlowMult = 0 if candle.high == candle.low else ((candle.close - candle.low) - (candle.high - candle.close)) / (candle.high - candle.low)
    moneyFlowVol = moneyFlowMult * candle.vol
    prev = self.prev()
    return super().update(prev + moneyFlowVol if isfinite(prev) else moneyFlowVol)

  def add(self, candle):
    moneyFlowMult = 0 if candle.high == candle.low else ((candle.close - candle.low) - (candle.high - candle.close)) / (candle.high - candle.low)
    moneyFlowVol = moneyFlowMult * candle.vol
    prev = self.v()
    return super().add(prev + moneyFlowVol if isfinite(prev) else moneyFlowVol)


