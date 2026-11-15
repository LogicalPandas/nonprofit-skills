# Skill evals

Every skill has test cases in `skills/<category>/<skill>/evals/evals.json`, in the [Agent Skills eval format](https://agentskills.io/skill-creation/evaluating-skills).

Each file has:
- `evals`: three realistic prompts: `core` (the skill's main job), `varied` (different wording and sub-task) and `edge` (an exception, failure mode, expert-review case or sibling overlap). Each has an `expected_output` and 3–6 checkable `assertions`.
- `should_not_trigger`: two near-miss requests and the library skill that should handle them instead (`none` if no skill fits). Use these to test the description.

## How to use them
1. Run each prompt twice in a fresh session: once with the skill loaded, once without.
2. Grade each assertion PASS or FAIL with evidence quoted from the response.
3. A skill earns its place when the with-skill run passes clearly more assertions. Assertions that pass both ways are too easy; replace them.
4. For descriptions, check that `should_not_trigger` queries do not load this skill.

Assertions avoid dated figures where possible. Where a figure matters, they check that the response tells the user to verify it at the source. Assertions describe what the skill teaches; they are not legal advice.

Check the files: `python3 scripts/check_evals.py skills`

The website ignores `evals/` folders; downloads and the library zip contain SKILL.md files only.
