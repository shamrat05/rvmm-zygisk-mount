from pathlib import Path
import unittest


SOURCE = (Path(__file__).parents[1] / "zygisk/jni/module.cpp").read_text()


class NativeSafetyTests(unittest.TestCase):
    def test_process_name_is_checked_before_jni_conversion(self):
        guard = "args->nice_name == nullptr"
        conversion = "GetStringUTFChars(args->nice_name"
        self.assertIn(guard, SOURCE)
        self.assertLess(SOURCE.index(guard), SOURCE.index(conversion))

    def test_companion_handoff_rejects_invalid_lengths(self):
        self.assertIn("proc_len == 0 || proc_len > 4096", SOURCE)
        self.assertIn("readFull(fd, proc.data(), proc_len)", SOURCE)


if __name__ == "__main__":
    unittest.main()
