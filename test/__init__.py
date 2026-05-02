import unittest


def run_all_tests():
    loader = unittest.TestLoader()
    tests = loader.discover('.')
    runner = unittest.runner.TextTestRunner(verbosity=2)
    runner.run(tests)


if __name__ == '__main__':
    run_all_tests()
