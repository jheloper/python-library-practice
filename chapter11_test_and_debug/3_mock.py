from chapter11_test_and_debug.sample_processing import OutsideAPI, my_processing
from unittest.mock import MagicMock, patch
import unittest


api = OutsideAPI()
api.do_something = MagicMock()
print(api.do_something)

api.do_something.return_value = 'mock 객체로 대체된 결과'
print(api.do_something())

# api.do_something.side_effect = Exception('예외를 설정합니다.')
# print(api.do_something())

api.do_something.assert_called_with()
# api.do_something.assert_called_once_with()


class TestMyClass(unittest.TestCase):
    @patch('chapter11_test_and_debug.sample_processing.OutsideAPI')
    def test_my_processing(self, APIMock):
        api2 = APIMock()
        api2.do_something.return_value = 'mock 객체로 대체된 결과'
        assert my_processing() == 'mock 객체로 대체된 결과를 사용하여 무엇인가를 하고 있다.'

    def test_my_processing2(self):
        with patch('chapter11_test_and_debug.sample_processing.OutsideAPI') as APIMock:
            api3 = APIMock()
            api3.do_something.return_value = 'mock 객체로 대체된 결과'
            assert my_processing() == 'mock 객체로 대체된 결과를 사용하여 무엇인가를 하고 있다.'

        assert my_processing() == '외부 API로 어떠한 처리를 실행한 결과를 사용하여 무엇인가를 하고 있다.'


if __name__ == "__main__":
    unittest.main()
