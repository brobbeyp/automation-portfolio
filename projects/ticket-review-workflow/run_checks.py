from pathlib import Path
import subprocess
import sys

CHECKS = ['test_adapter_body.py', 'test_content_type_check.py', 'test_json_boundary.py',
          'test_post_adapter.py', 'test_session_01.py', 'test_ticket_pipeline.py',
          'test_review_validator.py', 'test_review_parsing.py']

def main():
    folder = Path(__file__).resolve().parent
    failed = 0
    for name in CHECKS:
        result = subprocess.run([sys.executable, '-B', str(folder / name)], cwd=folder)
        failed += bool(result.returncode)
        print(f'{name}: {"PASS" if result.returncode == 0 else "FAIL"}', flush=True)
    print(f'{len(CHECKS)-failed}/{len(CHECKS)} assertion scripts passed')
    return bool(failed)

if __name__ == '__main__':
    raise SystemExit(main())
