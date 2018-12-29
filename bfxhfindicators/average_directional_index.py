from bfxhfindicators.sma import SMA
from bfxhfindicators.atr import ATR
from bfxhfindicators.indicator import Indicator
class ADX(Indicator):
  def __init__(self, args = []):
    [ smoothing, length ] = args
    super().__init__({
      'args': args,
      'id': 'adx',
      'name': 'ADX(%f, %f)' % (smoothing, length),
      'seedPeriod': Math.max(smoothing, length),
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._lastCandle = None
    self._adxSMA = SMA([smoothing])
    self._upSMA = SMA([length])
    self._downSMA = SMA([length])
    self._atr = ATR([length])

  def unserialize(self, args = []):
    return ADX(args)

  def reset(self):
    super().reset()
    if self._adxSMA:
      self._adxSMA.reset()
    if self._upSMA:
      self._upSMA.reset()
    if self._downSMA:
      self._downSMA.reset()
    if self._atr:
      self._atr.reset()
    self._lastCandle = None

  def calcUpdate(self, candle = {}, lastCandle = {}, indicators = {}, type):
    if type !== 'add' and type !== 'update':
      
    undefined = indicators
    undefined = candle
    upMove = high - lastCandle.high
    downMove = lastCandle.low - low
    dmUp = upMove if upMove > downMove and upMove > 0 else 0
    dmDown = downMove if downMove > upMove and downMove > 0 else 0
    atr[type](candle)
    upSMA[type](dmUp)
    downSMA[type](dmDown)
    atrV = atr.v()
    if atrV == 0:
      return 0
    diUp = (upSMA.v() / atrV) * 100
    diDown = (downSMA.v() / atrV) * 100
    adxSMA[type](Math.abs((diUp - diDown) / (diUp + diDown)))
    return 100 * adxSMA.v()

  def update(self, candle):
    if self._lastCandle == None:
      return
    adx = ADX.calcUpdate(candle, self._lastCandle, {
      'atr': self._atr,
      'upSMA': self._upSMA,
      'downSMA': self._downSMA,
      'adxSMA': self._adxSMA
    }, 'update')
    return super().update(adx)

  def add(self, candle):
    if self._lastCandle == None:
      self._lastCandle = candle
      return
    adx = ADX.calcUpdate(candle, self._lastCandle, {
      'atr': self._atr,
      'upSMA': self._upSMA,
      'downSMA': self._downSMA,
      'adxSMA': self._adxSMA
    }, 'add')
    super().add(adx)
    self._lastCandle = candle
    return self.v()

