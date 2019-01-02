from lodash/isObject import _isObject
from lodash/max import _max
from bfxhfindicators.indicator import Indicator
from bfxhfindicators.roc import ROC
from bfxhfindicators.sma import SMA
class KST(Indicator):
  def __init__(self, args = []):
    [ rocA, rocB, rocC, rocD, smaA, smaB, smaC, smaD, smaSignal ] = args
    super().__init__({
      'args': args,
      'id': 'kst',
      'name': 'KST (%f)' % ([rocA, rocB, rocC, rocD, smaA, smaB, smaC, smaD, smaSignal].join(',')),
      'seedPeriod': max([rocA + smaA, rocB + smaB, rocC + smaC, rocD + smaD, smaSignal])
    })
    self._rocA = ROC([rocA])
    self._rocB = ROC([rocB])
    self._rocC = ROC([rocC])
    self._rocD = ROC([rocD])
    self._smaA = SMA([smaA])
    self._smaB = SMA([smaB])
    self._smaC = SMA([smaC])
    self._smaD = SMA([smaD])
    self._smaSignal = SMA([smaSignal])

  def unserialize(args = []):
    return KST(args)

  def reset(self):
    super().reset()
    if self._rocA:
      self._rocA.reset()
    if self._rocB:
      self._rocB.reset()
    if self._rocC:
      self._rocC.reset()
    if self._rocD:
      self._rocD.reset()
    if self._smaA:
      self._smaA.reset()
    if self._smaB:
      self._smaB.reset()
    if self._smaC:
      self._smaC.reset()
    if self._smaD:
      self._smaD.reset()
    if self._smaSignal:
      self._smaSignal.reset()

  def update(self, v):
    self._rocA.update(v)
    self._rocB.update(v)
    self._rocC.update(v)
    self._rocD.update(v)
    if self._rocA.ready():
      self._smaA.update(self._rocA.v())
    if self._rocB.ready():
      self._smaB.update(self._rocB.v())
    if self._rocC.ready():
      self._smaC.update(self._rocC.v())
    if self._rocD.ready():
      self._smaD.update(self._rocD.v())
    if not self._smaA.ready() or not self._smaB.ready() or not self._smaC.ready() or not self._smaD.ready():
      return self.v()
    kst = ((self._smaA.v() + (self._smaB.v() * 2)) + (self._smaC.v() * 3)) + (self._smaD.v() * 4)
    self._smaSignal.update(kst)
    return super().update({
      'v': kst,
      'signal': self._smaSignal.v()
    })

  def add(self, v):
    self._rocA.add(v)
    self._rocB.add(v)
    self._rocC.add(v)
    self._rocD.add(v)
    if self._rocA.ready():
      self._smaA.add(self._rocA.v())
    if self._rocB.ready():
      self._smaB.add(self._rocB.v())
    if self._rocC.ready():
      self._smaC.add(self._rocC.v())
    if self._rocD.ready():
      self._smaD.add(self._rocD.v())
    if not self._smaA.ready() or not self._smaB.ready() or not self._smaC.ready() or not self._smaD.ready():
      return self.v()
    kst = ((self._smaA.v() + (self._smaB.v() * 2)) + (self._smaC.v() * 3)) + (self._smaD.v() * 4)
    self._smaSignal.add(kst)
    return super().add({
      'v': kst,
      'signal': self._smaSignal.v()
    })

  def ready(self):
    return _isObject(self.v())


