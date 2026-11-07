import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SH = r'C:\Program Files\Git\bin\sh.exe'


class PortTheTests(unittest.TestCase):
    def run_script(self, *args):
        return subprocess.run([SH, str(ROOT / 'port-the.sh'), *args],
                              capture_output=True, encoding='utf-8')

    def test_missing_card_stops_with_usage(self):
        result = self.run_script()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Thiếu mã thẻ', result.stderr)

    def test_missing_file_list_stops_before_git_changes(self):
        result = self.run_script('C1-05')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Không có danh sách file cho C1-05', result.stderr)


if __name__ == '__main__':
    unittest.main()
