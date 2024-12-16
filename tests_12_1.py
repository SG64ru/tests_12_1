import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5
        # self.distance += 10# изменение условий для 3 теста

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        walker = Runner("Tom")
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)
        # self.assertEqual(walker.distance, 55) # замена значения на ошибочное

    def test_run(self):
        runner = Runner("Sam")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        walker_1 = Runner("Tom_1")
        runner_1 = Runner("Sam_1")
        for i in range(10):
            walker_1.walk()
            runner_1.run()
        self.assertNotEqual(walker_1.distance, runner_1.distance)






