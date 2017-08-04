from unittest import TestCase

class TestIs_prime(TestCase):
    def test_is_prime(self):
        from idedemo.primes import is_prime
        self.assertTrue(is_prime(5))
