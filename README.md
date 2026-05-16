# Loan Requests Processor (Python)

This project processes a series of small loan requests from a text file using a fixed amount of available cash (the “kitty”). Requests are handled on a **first come, first served** basis, and each request is recorded as either **paid in full**, **partially paid**, or **unpaid** depending on the remaining balance.

## Overview
- Starting balance: **€500**
- Input file: `loan_requests.txt` (one loan amount per line)
- For each request:
  - If the kitty can cover the full amount → **pay in full**
  - If the request is larger than the remaining kitty → **pay partially** (pay what’s left)
  - If the kitty is empty → **request goes unpaid**
- The result of each request is:
  - printed to the console
  - appended to the end of `loan_requests.txt`

## What this demonstrates
- Reading from a text file line-by-line
- Writing/appending to a text file (`'a'` mode)
- Type conversion (`int()` and `str()`)
- List processing and loops
- Conditional logic (`if / elif / else`)
- Tracking and updating a running balance

## Files
- `exercise2.py` — main Python script
- `loan_requests.txt` — input file containing loan requests (one per line)

## How to run
1. Ensure `exercise2.py` and `loan_requests.txt` are in the same folder.
2. Run the script from a terminal:

   ```bash
   python exercise2.py