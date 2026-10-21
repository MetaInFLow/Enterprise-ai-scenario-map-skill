"""Offline regression tests for the research framework CLI output streams."""

import json
import os
from pathlib import Path
import subprocess
import sys
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "deep_research_wrapper.py"


class ResearchFrameworkCLITests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True,
            check=True,
            encoding="utf-8",
            env=dict(os.environ, PYTHONIOENCODING="utf-8"),
            timeout=10,
        )

    def test_json_stdout_can_be_parsed_without_filtering(self):
        for company_name in ("Example Fixture Ltd", '示例"测试"公司'):
            with self.subTest(company_name=company_name):
                result = self.run_cli(
                    "--company-name", company_name,
                    "--country", "示例地区", "--format", "json",
                )
                framework = json.loads(result.stdout)
                self.assertEqual(framework["company_name"], company_name)
                self.assertEqual(framework["country"], "示例地区")
                self.assertTrue(framework["research_queries"])
                self.assertTrue(framework["industry_research_queries"])
                self.assertIn("[调研]", result.stderr)
                self.assertIn(company_name, result.stderr)

    def test_default_markdown_stdout_contains_only_the_document(self):
        result = self.run_cli("--company-name", "Example Fixture Ltd")
        self.assertTrue(result.stdout.startswith("# Example Fixture Ltd 企业调研框架\n"))
        self.assertIn("## 待调研问题清单（企业信息）", result.stdout)
        self.assertIn("## 待调研问题清单（行业信息）", result.stdout)
        self.assertNotIn("[调研]", result.stdout)
        self.assertIn("[调研]", result.stderr)


if __name__ == "__main__":
    unittest.main()
