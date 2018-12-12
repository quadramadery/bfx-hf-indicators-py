from lodash/sum import _sum
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

  def unserialize(self, args = []):
    return CMF(args)

  def reset(self):
    super().reset()
    self._bufferVol = []
    self._bufferMFV = []

  def update(self, candle):
    undefined = candle
    mf = 0 if high == low else ((close - low) - (high - close)) / (high - low)
    mfv = mf * vol
    if len(self._bufferVol) == 0:
      self._bufferVol.append(vol)
    else:
      self._bufferVol[-1] = vol
    if len(self._bufferMFV) == 0:
      self._bufferMFV.append(vol)
    else:
      self._bufferMFV[-1] = mfv
    if len(self._bufferMFV) < self._p or len(self._bufferVol) < self._p:
      return
    return super().update(_sum(self._bufferMFV) / _sum(self._bufferVol))

  def add(self, candle):
    undefined = candle
    mf = 0 if high == low else ((close - low) - (high - close)) / (high - low)
    mfv = mf * vol
    self._bufferVol.append(vol)
    self._bufferMFV.append(mfv)
    if len(self._bufferVol) > self._p:
      del self._bufferVol[0]
    if len(self._bufferMFV) > self._p:
      del self._bufferMFV[0]
    if len(self._bufferMFV) < self._p or len(self._bufferVol) < self._p:
      return
    return super().add(_sum(self._bufferMFV) / _sum(self._bufferVol))


