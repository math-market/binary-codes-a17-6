#!/usr/bin/env python3
"""Checker for the binary-code boards: is this a valid code, and is it big enough?

A submission is a JSON file:

    {"codewords": ["01011010101101010", "10110...", ...]}

Every codeword is a string of `0`/`1` of length N. The code is valid when every
pair of distinct codewords differs in at least D positions. The board is won when
a valid code has more than TARGET codewords.

Exit codes:  0 valid and beats the target · 1 valid but does not · 2 unreadable.

Exact integer arithmetic throughout; no floating point, no randomness, no
network. Reads one file and writes a verdict.
"""
import json, sys, itertools

N, D, TARGET, WHAT = 17, 6, 258, "A(17,6)"

def die(msg, code=2):
    print(f"REJECTED: {msg}")
    sys.exit(code)

def main():
    if len(sys.argv) != 2:
        die("usage: check.py <submission.json>")
    try:
        with open(sys.argv[1]) as f:
            data = json.load(f)
    except Exception as e:
        die(f"could not read the submission as JSON: {e}")

    if not isinstance(data, dict) or "codewords" not in data:
        die('the submission must be a JSON object with a "codewords" key')
    words = data["codewords"]
    if not isinstance(words, list) or not words:
        die('"codewords" must be a non-empty list of strings')

    # Shape first, so a malformed entry is reported as itself rather than
    # surfacing later as a confusing distance error.
    for i, w in enumerate(words):
        if not isinstance(w, str):
            die(f"codeword {i} is not a string")
        if len(w) != N:
            die(f"codeword {i} has length {len(w)}, expected {N}")
        if set(w) - {"0", "1"}:
            die(f"codeword {i} contains characters other than 0 and 1")

    if len(set(words)) != len(words):
        die("the list contains duplicate codewords")

    # Pairwise minimum distance. int(w,2) turns each word into a machine integer
    # so the distance is one XOR and a popcount — exact, and fast enough that
    # even a few thousand codewords stay well inside the time budget.
    ints = [int(w, 2) for w in words]
    for i, j in itertools.combinations(range(len(ints)), 2):
        d = bin(ints[i] ^ ints[j]).count("1")
        if d < D:
            die(f"codewords {i} and {j} are at distance {d}, which is less than {D}")

    size = len(words)
    print(f"valid: {size} codewords of length {N}, minimum distance >= {D}")
    if size > TARGET:
        print(f"ACCEPTED: {size} > {TARGET} — this improves the best known "
              f"lower bound for {WHAT}")
        sys.exit(0)
    print(f"REJECTED: valid code, but {size} does not beat the target of {TARGET}")
    sys.exit(1)

if __name__ == "__main__":
    main()
