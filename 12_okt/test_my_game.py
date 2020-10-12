from unittest import TestCase
from my_game import Ball

class TestBall(TestCase):
    def tets_collision_true(self):
        ball1 = Ball(100, 100, 0, (0, 0, 0), 25)
        ball2 = Ball(120, 135, 0, (0, 0, 0), 10)
        self.assertTrue(ball1.collide(ball2))

    def tets_collision_false(self):
        ball1 = Ball(100, 100, 0, (0, 0, 0), 25)
        ball2 = Ball(120, 135, 0, (0, 0, 0), 10)
        self.assertFalse(ball1.collide(ball2))