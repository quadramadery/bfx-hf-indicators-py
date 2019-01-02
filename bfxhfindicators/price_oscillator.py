from bfxhfindicators.ema import EMA
from bfxhfindicators.indicator import Indicator
class PPO(Indicator):
  def __init__(self, args = []):
    [ shortPeriod, longPeriod ] = args
    super().__init__({
      'args': args,
      'id': 'ppo',
      'name': 'PPO(%f, %f)' % (shortPeriod, longPeriod),
      'seedPeriod': longPeriod
    })
    self._shortEMA = EMA([shortPeriod])
    self._longEMA = EMA([longPeriod])
    self._signalEMA = EMA([9])

  def unserialize(args = []):
    return PPO(args)

  def reset(self):
    super().reset()
    if self._shortEMA:
      self._shortEMA.reset()
    if self._longEMA:
      self._longEMA.reset()
    if self._signalEMA:
      self._signalEMA.reset()

  def update(self, v):
    self._shortEMA.update(v)
    self._longEMA.update(v)
    short = self._shortEMA.v()
    long = self._longEMA.v()
    ppo = 0 if long == 0 else ((short - long) / long) * 100
    self._signalEMA.update(ppo)
    return super().update(self._signalEMA.v())

  def add(self, v):
    self._shortEMA.add(v)
    self._longEMA.add(v)
    short = self._shortEMA.v()
    long = self._longEMA.v()
    ppo = 0 if long == 0 else ((short - long) / long) * 100
    self._signalEMA.add(ppo)
    return super().add(self._signalEMA.v())


