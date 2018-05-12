#pylint: skip-file

import unittest
from rdgo import mockchain

no_mock = True
try:
    from unittest.mock import ANY, patch, call
    no_mock = False
except ImportError:
    try:
        from mock import ANY, patch, call
        no_mock = False
    except ImportError:
        # Mock is already set to False
        pass

if no_mock:
    # If there is no mock, we need need to create a fake
    # patch decorator
    def fake_patch(a, new=''):
        def foo(func):
            def wrapper(*args, **kwargs):
                ret = func(*args, **kwargs)
                return ret
            return wrapper
        return foo

    patch = fake_patch

@unittest.skipIf(no_mock, "Mock not found")
class TestRpmBuildOptions(unittest.TestCase):
    """
    Unit tests for added build options related functions
    """

    def test_test(self):
        print("test")


if __name__ == '__main__':
    unittest.main()
