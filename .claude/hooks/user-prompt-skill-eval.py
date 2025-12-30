#!/usr/bin/env python3
from __future__ import annotations

import sys


def main() -> None:
    # consume stdin(event JSON, etc.)
    _ = sys.stdin.read()

instruction = """
INSTRUCTION: MANDATORY SKILL ACTIVATION SEQUENCE

Step 1 - EVALUATE:
For each skill in <available_skills>, state: [skill - name] - YES / NO - [reason]

Step 2 - ACTIVATE:
IF any skills are YES → Use Skill(skill - name) tool for EACH relevant skill NOW
IF no skills are YES → State "No skills needed" and proceed

Step 3 - IMPLEMENT:
Only after Step 2 is complete, proceed with implementation.

    CRITICAL: You MUST call Skill() tool in Step 2. Do NOT skip to implementation.
""".strip()

sys.stdout.write(instruction)


if __name__ == "__main__":
    main()
