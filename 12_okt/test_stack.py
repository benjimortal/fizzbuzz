from unittest import TestCase
from stack import Stack


class TestStack(TestCase):
    def test_create(self):
        stack = Stack()
        self.assertTrue(isinstance(stack, Stack))

    def test_empty(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)

    def tes_push_one(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(len(stack), 1)

    def tes_push_two(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(len(stack), 2)

    def test_pop_one(self):
        stack = Stack()
        stack.push('one')
        self.assertEqual(stack.pop(), 'one')

    def test_pop_two(self):
        stack = Stack()
        stack.push('one')
        stack.push('two')
        self.assertEqual(stack.pop(), 'two')
        self.assertEqual(stack.pop(), 'one')

    def test_pop_empty(self):
        stack = Stack()
        self.assertEqual(stack.pop(), None)