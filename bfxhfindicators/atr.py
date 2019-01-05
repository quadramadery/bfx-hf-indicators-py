from bfxhfindicators.indicator import Indicator
class ATR(Indicator):
  def __init__(self, args = []):
    [ period ] = args
    super().__init__({
      'args': args,
      'id': 'atr',
      'name': 'ATR(%f)' % (period),
      'seedPeriod': period,
      'dataType': 'candle',
      'dataKey': '*'
    })
    self._p = period
    self._prevCandle = None

  def unserialize(args = []):
    return ATR(args)

  def seed(candles = []):
    return _sum(map(lambda c, i: ATR.tr(None if i == 0 else candles[i - 1], c), candles)) / len(candles)

  def calc(prevATR, p, prevCandle, candle):
    return ((prevATR * (p - 1)) + ATR.tr(prevCandle, candle)) / p

  def tr(prevCandle, candle = {}):
    return max([prevCandle.high - prevCandle.low if prevCandle else 0, Math.abs(candle.high - prevCandle.close) if prevCandle else 0, Math.abs(candle.low - prevCandle.close) if prevCandle else 0])

  def reset(self):
    super().reset()
    self._buffer = []
    self._prevCandle = None

  def update(self, candle):
    if self.l() == 0:
      if len(self._buffer) < self._p:
        self._buffer.append(candle)
      else:
        self._buffer[-1] = candle
      if len(self._buffer) == self._p:
        super().update(ATR.seed(self._buffer))
    else:
      super().update(ATR.calc(self.prev(), self._p, self._prevCandle, candle))
    return self.v()

  def add(self, candle):
    if self.l() == 0:
      if len(self._buffer) < self._p:
        self._buffer.append(candle)
      if len(self._buffer) == self._p:
        super().add(ATR.seed(self._buffer))
    else:
      super().add(ATR.calc(self.v(), self._p, self._prevCandle, candle))
    self._prevCandle = candle
    return self.v()


