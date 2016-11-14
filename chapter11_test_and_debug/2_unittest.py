import unittest


class TestSample(unittest.TestCase):

    def setUp(self):
        self.target = 'foo'

    def test_upper(self):
        self.assertEqual(self.target.upper(), 'FOO')

    def test_upper2(self):
        self.assertEqual(self.target.upper(), 'Foo')

    @unittest.skip
    def test_upper3(self):
        self.assertEqual(self.target.upper(), 'FOO')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSample)
    unittest.TextTestRunner(verbosity=2).run(suite)
