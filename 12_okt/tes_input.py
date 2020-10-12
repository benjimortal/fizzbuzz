from unittest import TestCase, mock

from inputs import get_input


class TestInputs(TestCase):
    @mock.patch('builtins.input', lambda *args: '1')
    def test_input_int(self):
        result = get_input()
        self.assertTrue(isinstance(result, int))

    @mock.patch('builtins.input', lambda *args: '1.34')
    def test_input_float(self):
        result = get_input()
        self.assertTrue(isinstance(result, float))

    @mock.patch('builtins.input', lambda *args: 'hej')
    def test_input_str(self):
        result = get_input()
        self.assertTrue(isinstance(result, str))

    @mock.patch('builtins.input', lambda *args: 'True')
    def test_input_bool(self):
        result = get_input()
        self.assertTrue(isinstance(result, bool))



def main():
    pass


if __name__ == '__main__':
    main()
