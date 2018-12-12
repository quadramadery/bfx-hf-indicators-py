from lodash import undefined
from sprintf-js import undefined
class Indicator:
  def __init__(self, undefined = {}):
    if not isString(id):
      
    self._name = name
    self._seedPeriod = seedPeriod
    self._id = id
    self._args = args
    self._dataType = dataType
    self._dataKey = dataKey
    self.reset()

  def getName(self):
    return self._name

  def getSeedPeriod(self):
    return self._seedPeriod

  def getDataType(self):
    return self._dataType

  def getDataKey(self):
    return self._dataKey

  def update(self, v):
    if isEmpty(self._values):
      return self.add(v)
    self._values[-1] = v
    return v

  def add(self, v):
    self._values.append(v)
    return v

  def reset(self):
    self._values = []

  def prev(self, n = 1):
    return self._values[-n + 1]

  def v(self):
    return last(self._values)

  def l(self):
    return len(self._values)

  def nValues(self, n = 2):
    return self._values.slice(len(self._values) - n)

  def avg(self, n = 2):
    return sum(self.nValues(n)) / n

  def crossed(self, target):
    if self.l() < 2:
      return false
    v = self.v()
    prev = self.prev()
    return v >= target and prev <= target or v <= target and prev >= target

  def logStr(self, mts):
    v = self.v()
    return sprintf('%s %.2f', self._name, v if isFinite(v) else NaN)

  def ready(self):
    return isFinite(self.v())

  def serialize(self):
    return {
      'seedPeriod': self._seedPeriod,
      'name': self._name,
      'id': self._id,
      'args': self._args
    }


