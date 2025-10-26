# run_test.py — path-agnostic manual runner with output saved to a .txt file
from pathlib import Path
import importlib.util, traceback, json, sys

# --- Change this number to pick a task ---
task_num = 66
print(f"--- Testing Task {task_num:03d} ---")

ROOT = Path(__file__).resolve().parent  # repo root regardless of CWD

# Create output file in same folder as this script
output_file = ROOT / f"task{task_num:03d}_output.txt"
sys.stdout = open(output_file, "w", encoding="utf-8")
sys.stderr = sys.stdout  # capture tracebacks too

print(f"--- Testing Task {task_num:03d} ---")

# Locate JSON dataset
json_candidates = [
    ROOT / "data" / f"task{task_num:03d}.json",
    ROOT / "tasks" / f"task{task_num:03d}.json",
    ROOT / f"task{task_num:03d}.json",
]
json_file = next((p for p in json_candidates if p.exists()), None)
if not json_file:
    print(f"❌ Could not find JSON for task {task_num}. Looked in:")
    for p in json_candidates:
        print("   ", p)
    sys.exit(1)

with json_file.open() as f:
    examples = json.load(f)

# Locate Python solution
py_candidates = [
    ROOT / "solutions" / f"task{task_num:03d}.py",
    ROOT / "solution" / f"task{task_num:03d}.py",
    ROOT / f"task{task_num:03d}.py",
]
task_file = next((p for p in py_candidates if p.exists()), None)
if not task_file:
    print(f"❌ Could not find solution file for task {task_num}. Looked in:")
    for p in py_candidates:
        print("   ", p)
    sys.exit(1)

# Import solution's p() function dynamically
spec = importlib.util.spec_from_file_location("task_module", str(task_file))
task_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task_module)
if not hasattr(task_module, "p"):
    print(f"❌ {task_file.name} does not define function p(g)")
    sys.exit(1)
solver = getattr(task_module, "p")

def diff_summary(expected, actual, max_show=15):
    """Return a compact summary of mismatched cells."""
    mismatches = []
    h = max(len(expected), len(actual))
    w = max(len(expected[0]), len(actual[0]))
    for i in range(h):
        for j in range(w):
            e = expected[i][j] if i < len(expected) and j < len(expected[i]) else None
            a = actual[i][j] if i < len(actual) and j < len(actual[i]) else None
            if e != a:
                mismatches.append((i, j, e, a))
                if len(mismatches) >= max_show:
                    return mismatches, True
    return mismatches, False

# Overview info
print(f"Loaded from: {json_file}")
print(f"Solution:     {task_file}")
for name in ("train", "test", "arc-gen"):
    n = len(examples.get(name, []))
    print(f"{name}: {n} example(s)")

# Run the solver
for split_name in ["train", "test", "arc-gen"]:
    print(f"\n=== {split_name.upper()} EXAMPLES ===")
    for idx, ex in enumerate(examples.get(split_name, [])):
        inp, expected = ex["input"], ex["output"]
        try:
            actual = solver(inp)
        except Exception as e:
            print(f"[{split_name} {idx}] 💥 Solver crashed!")
            print("Exception Type:", type(e).__name__)
            print("Error Message:", str(e))
            traceback.print_exc()
            continue

        if actual == expected:
            print(f"[{split_name} {idx}] ✅ Correct")
        else:
            print(f"[{split_name} {idx}] ❌ Mismatch")
            mis, truncated = diff_summary(expected, actual)
            if mis:
                print(f"  Differences (row,col exp→act):")
                for (i, j, e, a) in mis:
                    print(f"   - ({i},{j}) {e} → {a}")
                if truncated:
                    print("   … (more differences omitted)")
            print("  Expected:", expected)
            print("  Actual:  ", actual)

print(f"\n✅ Output saved to: {output_file}")
sys.stdout.close()
