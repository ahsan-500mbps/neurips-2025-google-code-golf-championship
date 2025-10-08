# In run_test.py # If your code works great, if not, try run_test_advanced.py to see errors.
import code_golf_utils as utils

# --- Manually change this number to test a different task ---
task_num = 375

# Answer verification
print(f"--- Testing Task {task_num:03d} ---")
examples = utils.load_examples(task_num)
utils.verify_program(task_num, examples)
