
import unittest
import sys
import json

sys.path.append('../')
from bfxhfindicators import MACD

with open('tests/btc_candle_data.json', 'r') as f:
  btcCandleData = json.load(f)
  candles = list(map(lambda candleArray: {
    'mts': candleArray[0],
    'open': candleArray[1],
    'close': candleArray[2],
    'high': candleArray[3],
    'low': candleArray[4],
    'vol': candleArray[5],
    'symbol': 'tBTCUSD',
    'tf': '1min',
  }, btcCandleData))

expected = [
  {
    "macd": 0,
    "signal": 0,
    "histogram": 0
  },
  {
    "macd": -0.1276353276352893,
    "signal": -0.025527065527057857,
    "histogram": -0.10210826210823143
  },
  {
    "macd": 2.7014553453300323,
    "signal": 0.5198694166443601,
    "histogram": 2.181585928685672
  },
  {
    "macd": 5.716823190583455,
    "signal": 1.559260171432179,
    "histogram": 4.157563019151276
  },
  {
    "macd": 8.660295739536195,
    "signal": 2.9794672850529826,
    "histogram": 5.680828454483213
  },
  {
    "macd": 10.85976516404935,
    "signal": 4.5555268608522566,
    "histogram": 6.304238303197093
  },
  {
    "macd": 12.467215395059611,
    "signal": 6.137864567693728,
    "histogram": 6.329350827365883
  },
  {
    "macd": 13.672286483229072,
    "signal": 7.644748950800797,
    "histogram": 6.027537532428275
  },
  {
    "macd": 14.803640908624402,
    "signal": 9.076527342365518,
    "histogram": 5.727113566258884
  },
  {
    "macd": 15.617053738679715,
    "signal": 10.384632621628358,
    "histogram": 5.2324211170513575
  },
  {
    "macd": 16.06839366264103,
    "signal": 11.521384829830893,
    "histogram": 4.5470088328101355
  },
  {
    "macd": 16.526071453065924,
    "signal": 12.5223221544779,
    "histogram": 4.0037492985880245
  },
  {
    "macd": 16.680365203932524,
    "signal": 13.353930764368826,
    "histogram": 3.326434439563698
  },
  {
    "macd": 16.56329774146161,
    "signal": 13.995804159787383,
    "histogram": 2.5674935816742277
  },
  {
    "macd": 16.123278530220887,
    "signal": 14.421299033874085,
    "histogram": 1.7019794963468016
  },
  {
    "macd": 15.754337227623182,
    "signal": 14.687906672623907,
    "histogram": 1.0664305549992754
  },
  {
    "macd": 15.070359429546443,
    "signal": 14.764397224008414,
    "histogram": 0.30596220553802844
  },
  {
    "macd": 14.53823597601604,
    "signal": 14.719164974409939,
    "histogram": -0.18092899839389887
  },
  {
    "macd": 13.740267618109101,
    "signal": 14.523385503149772,
    "histogram": -0.7831178850406708
  },
  {
    "macd": 13.293537222391024,
    "signal": 14.277415846998023,
    "histogram": -0.9838786246069997
  },
  {
    "macd": 12.815973097855931,
    "signal": 13.985127297169607,
    "histogram": -1.1691541993136756
  },
  {
    "macd": 12.160149660139723,
    "signal": 13.620131769763631,
    "histogram": -1.4599821096239083
  },
  {
    "macd": 11.515727882326246,
    "signal": 13.199250992276156,
    "histogram": -1.6835231099499097
  },
  {
    "macd": 10.743993123272048,
    "signal": 12.708199418475335,
    "histogram": -1.9642062952032866
  },
  {
    "macd": 9.729739473034897,
    "signal": 12.112507429387248,
    "histogram": -2.3827679563523514
  },
  {
    "macd": 8.824216077858182,
    "signal": 11.454849159081435,
    "histogram": -2.6306330812232535
  },
  {
    "macd": 7.93442747960944,
    "signal": 10.750764823187037,
    "histogram": -2.8163373435775974
  },
  {
    "macd": 7.48192156953337,
    "signal": 10.096996172456304,
    "histogram": -2.6150746029229346
  },
  {
    "macd": 7.042130083638767,
    "signal": 9.486022954692798,
    "histogram": -2.4438928710540306
  },
  {
    "macd": 7.02414951681294,
    "signal": 8.993648267116827,
    "histogram": -1.9694987503038863
  },
  {
    "macd": 6.36363312380945,
    "signal": 8.467645238455352,
    "histogram": -2.1040121146459025
  },
  {
    "macd": 5.4146401307289125,
    "signal": 7.857044216910064,
    "histogram": -2.442404086181152
  },
  {
    "macd": 4.569535761442239,
    "signal": 7.1995425258165,
    "histogram": -2.6300067643742606
  },
  {
    "macd": 3.927137343778668,
    "signal": 6.545061489408933,
    "histogram": -2.6179241456302655
  },
  {
    "macd": 3.307285166478323,
    "signal": 5.897506224822812,
    "histogram": -2.590221058344489
  },
  {
    "macd": 3.0631584159837075,
    "signal": 5.330636663054991,
    "histogram": -2.267478247071283
  },
  {
    "macd": 3.7543621480353977,
    "signal": 5.015381760051072,
    "histogram": -1.2610196120156747
  },
  {
    "macd": 4.819500546103882,
    "signal": 4.976205517261635,
    "histogram": -0.15670497115775284
  },
  {
    "macd": 5.6629052677117215,
    "signal": 5.113545467351653,
    "histogram": 0.5493598003600688
  },
  {
    "macd": 6.362861613499263,
    "signal": 5.363408696581176,
    "histogram": 0.999452916918087
  },
  {
    "macd": 6.82279480050056,
    "signal": 5.6552859173650525,
    "histogram": 1.1675088831355076
  },
  {
    "macd": 7.105388667233456,
    "signal": 5.9453064673387335,
    "histogram": 1.1600821998947222
  },
  {
    "macd": 7.277729860061299,
    "signal": 6.211791145883247,
    "histogram": 1.0659387141780527
  },
  {
    "macd": 7.337795126692072,
    "signal": 6.436991942045013,
    "histogram": 0.9008031846470592
  },
  {
    "macd": 7.484708995116307,
    "signal": 6.646535352659272,
    "histogram": 0.8381736424570354
  },
  {
    "macd": 7.465757579834644,
    "signal": 6.810379798094346,
    "histogram": 0.6553777817402979
  },
  {
    "macd": 7.358748335043856,
    "signal": 6.920053505484249,
    "histogram": 0.4386948295596067
  },
  {
    "macd": 7.262843675050135,
    "signal": 6.988611539397427,
    "histogram": 0.2742321356527082
  },
  {
    "macd": 6.793327605994818,
    "signal": 6.949554752716905,
    "histogram": -0.15622714672208637
  },
  {
    "macd": 6.275214645726919,
    "signal": 6.814686731318909,
    "histogram": -0.5394720855919894
  },
  {
    "macd": 5.791341372288116,
    "signal": 6.61001765951275,
    "histogram": -0.8186762872246343
  },
  {
    "macd": 5.537693179454436,
    "signal": 6.395552763501088,
    "histogram": -0.8578595840466514
  },
  {
    "macd": 4.861043533451266,
    "signal": 6.088650917491123,
    "histogram": -1.2276073840398576
  },
  {
    "macd": 4.554710693609195,
    "signal": 5.781862872714738,
    "histogram": -1.227152179105543
  },
  {
    "macd": 4.717501651640305,
    "signal": 5.568990628499852,
    "histogram": -0.8514889768595468
  }
]

class MACDTest(unittest.TestCase):
  def test_add(self):
    indicator = MACD([12, 26, 9])
    for i in range(len(expected)):
      indicator.add(candles[i]['close'])
      self.assertEqual(indicator.v(), expected[i], 'candles[%d]' % i)


if __name__ == '__main__':
    unittest.main()
  
