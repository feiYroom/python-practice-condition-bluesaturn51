# Python If-Statements — Super Easy Exercises

Ten beginner-friendly tasks focused on `if / elif / else` branching in Python.
Each task is a **single function** in `exercises/` with a short docstring.
Edit only the function bodies (they currently use `pass`).

## How to run locally
```bash
python -m pip install -r requirements.txt
pytest -q
```

## Rules / Specs
- Use basic conditionals only (no loops required unless you want).
- Keep function names the same.
- **Grade policy**: 10 points total (1 point per test file).
- Conventions used in tests:
  - `grade_letter(score)`: 90+ A, 80–89 B, 70–79 C, 60–69 D, else F.
  - `is_leap_year(y)`: leap if divisible by 400, or divisible by 4 but not by 100.
  - `ticket_price(age)`: `<13 → 5`, `13–64 → 10`, `>=65 → 7`.
  - `fizz_label(n)`: "FizzBuzz" if divisible by 3 and 5, "Fizz" if only by 3, "Buzz" if only by 5, else `str(n)`.
  - `is_vowel(ch)`: case-insensitive; only English vowels aeiou.
```
