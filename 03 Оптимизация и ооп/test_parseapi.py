import unittest
from project.main import calculate_direction, assess_intesity, get_decision


class TestTimeHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.decision_dict = {('Low', 'Spikes'): 'delete resource', ('Low', 'Drops'): 'delete resource', ('Low', 'Stable'): 'delete resource',
                              ('Medium', 'Spikes'): 'normal using', ('Medium', 'Drops'): 'delete resource', ('Medium', 'Stable'): 'normal using',
                              ('High', 'Spikes'): 'extend resource', ('High', 'Drops'): 'normal using', ('High', 'Stable'): 'normal using',
                              ('Overwhelming', 'Spikes'): 'extend resource', ('Overwhelming', 'Drops'): 'extend resource', ('Overwhelming', 'Stable'): 'extend resource'}

    def test_decision(self):
        for in_parameters_for_testing, result in self.decision_dict.items():
            self.assertEqual(result, get_decision(*in_parameters_for_testing))

    def test_intensity_none(self):
        self.assertEqual(assess_intesity(0), None)

    def test_intensity_low(self):
        self.assertEqual(assess_intesity(10), "Low")

    def test_intensity_med(self):
        self.assertEqual(assess_intesity(50), "Medium")

    def test_intensity_high(self):
        self.assertEqual(assess_intesity(90), "High")

    def test_intensity_overwhelming(self):
        self.assertEqual(assess_intesity(100), "Overwhelming")

    def test_direction_spikes(self):
        self.assertEqual(calculate_direction(100, 50), "Spikes")

    def test_direction_ok(self):
        self.assertEqual(calculate_direction(100, 90), "Stable")

    def test_direction_drops(self):
        self.assertEqual(calculate_direction(100, 150), "Drops")
