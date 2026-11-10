import io
from contextlib import redirect_stderr
from unittest import TestCase
from unittest.mock import patch

from csv2md.__main__ import main


class TestMissingFile(TestCase):
    def test_missing_file_exits_cleanly(self):
        stderr = io.StringIO()
        with patch("sys.argv", ["csv2md", "does-not-exist.md"]):
            with redirect_stderr(stderr):
                with self.assertRaises(SystemExit) as ctx:
                    main()
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("does-not-exist.md", stderr.getvalue())
        self.assertNotIn("Traceback", stderr.getvalue())

    def test_missing_file_does_not_skip_remaining_files(self):
        import os
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            valid = os.path.join(tmp, "valid.csv")
            with open(valid, "w") as f:
                f.write("a,b\n1,2\n")
            out = io.StringIO()
            err = io.StringIO()
            with patch("sys.argv", ["csv2md", "does-not-exist.md", valid]):
                with patch("sys.stdout", out), redirect_stderr(err):
                    with self.assertRaises(SystemExit) as ctx:
                        main()
        # the valid file is still processed although the first file is missing
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("does-not-exist.md", err.getvalue())
        self.assertIn("| a | b |", out.getvalue())
