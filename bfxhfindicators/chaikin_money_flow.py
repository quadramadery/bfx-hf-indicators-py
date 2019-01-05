from bfxhfindicators.indicator import Indicator
class CMF(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'cmf',
      'name': 'CMF (%f)' % (period),
      'seedPeriod': period,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._p = period
    self._bufferVol = []
    self._bufferMFV = []

  def unserialize(args = []):
    return CMF(args)

  def reset(self):
    super().reset()
    self._bufferVol = []
    self._bufferMFV = []

  def update(self, candle):
    mf = 0 if candle.high == candle.low else ((candle.close - candle.low) - (candle.high - candle.close)) / (candle.high - candle.low)
    mfv = mf * candle.vol
    if len(self._bufferVol) == 0:
      self._bufferVol.append(candle.vol)
    else:
      self._bufferVol[-1] = candle.vol
    if len(self._bufferMFV) == 0:
      self._bufferMFV.append(candle.vol)
    else:
      self._bufferMFV[-1] = mfv
    if len(self._bufferMFV) < self._p or len(self._bufferVol) < self._p:
      return
    return super().update(_sum(self._bufferMFV) / _sum(self._bufferVol))

  def add(self, candle):
    mf = 0 if candle.high == candle.low else ((candle.close - candle.low) - (candle.high - candle.close)) / (candle.high - candle.low)
    mfv = mf * candle.vol
    self._bufferVol.append(candle.vol)
    self._bufferMFV.append(mfv)
    if len(self._bufferVol) > self._p:
      del self._bufferVol[0]
    if len(self._bufferMFV) > self._p:
      del self._bufferMFV[0]
    if len(self._bufferMFV) < self._p or len(self._bufferVol) < self._p:
      return
    return super().add(_sum(self._bufferMFV) / _sum(self._bufferVol))


