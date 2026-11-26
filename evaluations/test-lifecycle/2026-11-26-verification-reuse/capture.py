import sys, subprocess, json, time, hashlib
from pathlib import Path
ROOT = Path(__file__).resolve().parent
project = ROOT / "project"
stage, *argv = sys.argv[1:]
if stage not in {"stage1", "stage2"} or not argv:
    raise SystemExit("Usage: capture.py stage1|stage2 command [args...]")
start = time.perf_counter()
result = subprocess.run(argv, cwd=project, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120)
revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=project, text=True).strip()
record = {"stage":stage,"argv":argv,"revision":revision,"exit_code":result.returncode,"wall_seconds":time.perf_counter()-start,"stdout":result.stdout,"stderr":result.stderr}
log = ROOT / "evidence" / (stage + "-commands.jsonl")
with log.open("a") as f:
    f.write(json.dumps(record) + "\n")
sys.stdout.write(result.stdout)
sys.stderr.write(result.stderr)
raise SystemExit(result.returncode)
