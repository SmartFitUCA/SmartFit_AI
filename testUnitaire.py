import unittest
from fonction import generateModele,generateJsonModel

class Testing(unittest.TestCase):
    def test_model(self):
        data = [{'json': '{"bpmAvg":114,"bpmMax":145,"bpmMin":79,"denivelePositif":449.00000000000114,"deniveleNegatif":70.00000000000114,"altitudeMax":402.4,"altitudeMin":369.20000000000005,"altitudeAvg":382.2932358318101,"temperatureMax":22,"temperatureMin":18,"temperatureAvg":20,"vitesseMax":4.62,"vitesseMin":0.0,"vitesseAvg":1.3393414634146392,"startTime":"2023-12-10T03:12:54.000","timeOfActivity":2061.82,"distance":2131.0,"calories":215,"steps":1168}'}, {'json': '{"bpmAvg":118,"bpmMax":146,"bpmMin":102,"denivelePositif":448.80000000000007,"deniveleNegatif":55.80000000000007,"altitudeMax":406.6,"altitudeMin":375.4,"altitudeAvg":386.7921763869132,"temperatureMax":24,"temperatureMin":21,"temperatureAvg":22,"vitesseMax":2.3,"vitesseMin":0.0,"vitesseAvg":1.7642135231316907,"startTime":"2023-12-12T17:17:43.000","timeOfActivity":1445.47,"distance":2449.0,"calories":170,"steps":1368}'}, {'json': '{"bpmAvg":111,"bpmMax":122,"bpmMin":103,"denivelePositif":395.19999999999993,"deniveleNegatif":23.799999999999955,"altitudeMax":375.20000000000005,"altitudeMin":369.79999999999995,"altitudeAvg":372.7532258064513,"temperatureMax":30,"temperatureMin":23,"temperatureAvg":25,"vitesseMax":2.56,"vitesseMin":0.0,"vitesseAvg":1.7127125506072893,"startTime":"2023-12-09T19:16:43.000","timeOfActivity":255.62,"distance":466.0,"calories":30,"steps":255}'}]
        model = generateJsonModel(generateModele(data))
        self.assertEqual(model["coef"][0],2.4008223334695094e-08)
        self.assertEqual(model["coef"][1],1.8702979299828552e-06)
        self.assertEqual(model["intercept"][0],-40753.409070545466)
        self.assertEqual(model["intercept"][1],-3182440.4230727013)

if __name__ == '__main__':
    unittest.main()

#python -m unittest testUnitaire.py