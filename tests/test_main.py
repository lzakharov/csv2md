from unittest import TestCase, mock

from csv2md.__main__ import main


class TestMainExceptions(TestCase):
    @mock.patch("sys.argv", ["csv2md", "missing.csv"])
    def test_missing_file(self):
        with self.assertRaises(SystemExit) as cm:
            main()

        self.assertEqual(
            cm.exception.code,
            "Error: file 'missing.csv' not found",
        )

    @mock.patch("sys.argv", ["csv2md", "secret.csv"])
    @mock.patch("builtins.open", side_effect=PermissionError)
    def test_permission_denied(self, mock_open):
        with self.assertRaises(SystemExit) as cm:
            main()

        self.assertEqual(
            cm.exception.code,
            "Error: open 'secret.csv': permission denied",
        )
