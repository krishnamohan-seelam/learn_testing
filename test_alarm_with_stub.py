import unittest
from unittest.mock import Mock
from alarm import Alarm
from sensor import Sensor

class TestAlarmWithMock(unittest.TestCase):

    def testAlarmWithStub(self):
        stub_sensor = Mock()
        stub_sensor.take_measurement.return_value = 35
        alarm_obj  = Alarm(stub_sensor)
        alarm_obj.validate()
        self.assertTrue(alarm_obj.active)

    def testAlarmWithMock(self):
        mock_sensor = Mock(Sensor)
        mock_sensor.take_measurement.return_value = 35
        alarm_obj  = Alarm(mock_sensor)
        alarm_obj.validate()
        mock_sensor.take_measurement.assert_called()
        self.assertTrue(alarm_obj.active)


if __name__ == '__main__':
    unittest.main()