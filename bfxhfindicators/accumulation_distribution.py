'use strict'
from lodash/isFinite import _isFinite
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

  def unserialize(self, args = []):
    return AccumulationDistribution(args)

  def reset(self):
    super().reset()

  def update(self, candle):
    undefined = candle
    moneyFlowMult = 0 if high == low else ((close - low) - (high - close)) / (high - low)
    moneyFlowVol = moneyFlowMult * vol
    prev = self.prev()
    return super().update(prev + moneyFlowVol if _isFinite(prev) else moneyFlowVol)

  def add(self, candle):
    undefined = candle
    moneyFlowMult = 0 if high == low else ((close - low) - (high - close)) / (high - low)
    moneyFlowVol = moneyFlowMult * vol
    prev = self.v()
    return super().add(prev + moneyFlowVol if _isFinite(prev) else moneyFlowVol)


""
""
""
""
""
module.exports = AccumulationDistribution