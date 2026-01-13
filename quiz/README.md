# Python Quiz Game (Example: Sound Chapter)

This is a **command-line quiz game** written in Python.
Currently, the quiz uses **Sound chapter questions** only as an **example**.
You can easily replace them with questions from **any subject**.

---

## Features
- Multiple choice questions (MCQs)
- Retry option for wrong answers
- Instant feedback (correct / wrong)
- Explanation shown after each question
- Beginner-friendly Python logic

---

## Main Data Structure (IMPORTANT)

All quiz content is stored inside a single list called `quiz_data`.

```python
quiz_data = [
    questions_dict,
    options_list,
    explanations_list
]
**must be the same**.

Example:
- 5 questions → 5 option lists → 5 explanations

If these lengths do not match, the quiz may show wrong options or crash.
