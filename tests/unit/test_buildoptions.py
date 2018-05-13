#pylint: skip-file

import unittest
from rdgo import utils

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

    def test_key_value_pair(self):
        key_value_pairs = {"foo" : "bar",
                           "baz" : "blar"}

        output = utils.convert_key_pair_into_commands(key_value_pairs, "define")
        self.assertEqual(output, '--define "foo bar" --define "baz blar"')

if __name__ == '__main__':
    unittest.main()
