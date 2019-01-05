from math import isfinite
from bfxhfindicators.indicator import Indicator
from bfxhfindicators.wma import WMA
from bfxhfindicators.roc import ROC
class CoppockCurve(Indicator):
  def __init__(self, args = []):
    [ wmaLength, longROCLength, shortROCLength ] = args
    super().__init__({
      'args': args,
      'id': 'coppockcurve',
      'name': 'Coppock Curve(%f, %f, %f)' % (wmaLength, longROCLength, shortROCLength),
      'seedPeriod': max([longROCLength + wmaLength, shortROCLength + wmaLength])
    })
    self._wma = WMA([wmaLength])
    self._shortROC = ROC([shortROCLength])
    self._longROC = ROC([longROCLength])

  def unserialize(args = []):
    return CoppockCurve(args)

  def reset(self):
    super().reset()
    if self._wma:
      self._wma.reset()
    if self._shortROC:
      self._shortROC.reset()
    if self._longROC:
      self._longROC.reset()

  def update(self, v):
    self._shortROC.update(v)
    self._longROC.update(v)
    short = self._shortROC.v()
    long = self._longROC.v()
    if not isfinite(short) or not isfinite(long):
      return
    self._wma.update(short + long)
    return super().update(self._wma.v())

  def add(self, v):
    self._shortROC.add(v)
    self._longROC.add(v)
    short = self._shortROC.v()
    long = self._longROC.v()
    if not isfinite(short) or not isfinite(long):
      return
    self._wma.add(short + long)
    return super().add(self._wma.v())


