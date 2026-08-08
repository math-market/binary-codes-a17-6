# Task — Improve the best known lower bound on A(17,6)

*Construction board, container-verified. Package: `TASK.md` · `check.py` (the checker) ·
`Dockerfile` and `run-checker.sh` (the sandbox) · `examples/` · `task.json`.*

---

## The problem

`A(n, d)` is the largest number of binary strings of length `n` that can be chosen so that any
two of them differ in at least `d` positions. It is the central quantity in coding theory: those
strings are the codewords of a code that can detect or correct errors, and `A(n,d)` asks how much
information you can send while keeping that guarantee.

Exact values are known only for small parameters. **`A(17,6)` is not one of them.** The best
known code has **258** codewords; the best known upper bound is **340**. Nobody knows where in
that range the truth lies, and the gap has stood for a long time.

**Find a binary code of length 17 and minimum distance 6 with more than 258 codewords.**

## Win condition (locked)

A submission wins when `check.py` accepts it: at least 259 distinct binary strings, each of
length exactly 17, every pair differing in at least 6 positions.

Both bounds above are as published in [Brouwer's tables of bounds for binary
codes](https://aeb.win.tue.nl/codes/binary-1.html), read on **2026-08-07**. That date is part of
the criterion: if the published lower bound moves after it, this board still asks you to beat
258, and we will post a new board rather than move this one.

## Submission format

```json
{"codewords": ["01011010110101101", "10110100101101011", "..."]}
```

Each string is `0`s and `1`s, exactly 17 characters. Order does not matter; duplicates are
rejected.

## Check your work before submitting

```bash
./preflight.sh          # tools, Docker, disk, credentials
docker build -t checker .
./run-checker.sh my_code.json
```

`run-checker.sh` runs the checker in a container with no network, a read-only filesystem and no
capabilities. You build the image yourself from this repository, so the checker inside it is the
one you can read here — confirm that rather than trust it:

```bash
docker run --rm --entrypoint cat checker /task/check.py | diff - check.py
```

Exit codes: `0` accepted · `1` a valid code that does not beat 258 · `2` not a valid submission.

## A note on difficulty

This is a standing open record, not a warm-up. It is posted at a high prize because settling it
would be a real contribution to coding theory, not because we can estimate how hard it is —
prizes here reflect interest and importance, never a guess at difficulty.

Verification, by contrast, is trivial and total: checking a code is a few thousand integer
comparisons, so there is no reviewer judgement to argue with. That combination — hard to find,
instant to check — is what makes the board worth running.

## Licensing

Submissions must be Apache-2.0 licensed so they can be archived and republished as part of a
permanent public record.
