from unittest import TestCase, mock
from prints import print_it
from io import StringIO


def fake_print(f):
    def inner(*args, **kwargs):
        x = args[0]
        return x
    return inner


class TestPrints(TestCase):
    def test_bob(self):
        expected_result = 'Hi Bob\n'

        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            print_it("Bob")
            self.assertEqual(fake_out.getvalue(), expected_result)

    def test_anna(self):
        global print
        expected_result = 'Hi Anna\n'
        old_print= print
        print = fake_print(print)
        print_it("Anna")
        print = old_print



