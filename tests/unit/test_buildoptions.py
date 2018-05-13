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

    def test_combine_with_other_opts(self):
        # In the future, there might be case where we want to add more rpmopts
        # other than define, this unit test is more of proof of expected behavior
        opts = ["-ts", "--clean", "-bc",'--define "foo bar" --define "baz blar"']
        output = " ".join(opts)
        self.assertEqual(output, '-ts --clean -bc --define "foo bar" --define "baz blar"')

        empty_opts = []
        output = " ".join(empty_opts)
        self.assertEqual(output, "")

if __name__ == '__main__':
    unittest.main()
