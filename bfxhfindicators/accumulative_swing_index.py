from bfxhfindicators.indicator import Indicator
class AccumulativeSwingIndex(Indicator):
  def __init__(self, args = []):
    [ limitMoveValue ] = args
    super().__init__({
      'args': args,
      'id': 'asi',
      'name': 'ASI(%f)' % (limitMoveValue),
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._lmv = limitMoveValue
    self._prevCandle = None

  def unserialize(args = []):
    return AccumulativeSwingIndex(args)

  def calcSI(candle, prevCandle, _lmv):
    if _lmv == 0:
      return 0
    lmv = _lmv
    open = candle.open
    high = candle.high
    low = candle.low
    close = candle.close
    prevClose = prevCandle.close
    prevOpen = prevCandle.open
    k = max([high - prevClose, prevClose - low])
    tr = max([k, high - low])
    sh = prevClose - prevOpen
    er = 0
    if prevClose > high:
      er = high - prevClose
    elif prevClose < low:
      er = prevClose - low
    r = tr - ((er * 0.5) + (sh * 0.25))
    if r == 0:
      return 0
    siNum = ((close - prevClose) + ((close - open) * 0.5)) + ((prevClose - prevOpen) * 0.25)
    si = ((k / lmv) * 50) * (siNum / r)
    return si

  def reset(self):
    super().reset()
    self._prevCandle = None

  def update(self, candle):
    if self._prevCandle == None:
      return super().update(0)
    si = AccumulativeSwingIndex.calcSI(candle, self._prevCandle, self._lmv)
    return super().update(self.prev() + si)

  def add(self, candle):
    if self._prevCandle == None:
      super().add(0)
      self._prevCandle = candle
      return
    si = AccumulativeSwingIndex.calcSI(candle, self._prevCandle, self._lmv)
    super().add(self.v() + si)
    self._prevCandle = candle
    return self.v()


