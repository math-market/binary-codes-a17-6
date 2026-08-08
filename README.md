# A(17,6) — binary codes of length 17 and minimum distance 6

A Problem Market board. Find more than **258** binary strings of length 17, pairwise differing in
at least 6 positions. The best known upper bound is 340; the true value is unknown.

```bash
./preflight.sh                        # check your setup first
docker build -t checker .
./run-checker.sh my_code.json         # the same checker the reviewer runs
```

Task, win condition and submission format: [`TASK.md`](TASK.md). Constraints as data:
[`task.json`](task.json). Automated solvers should read both.

Bounds as published in [Brouwer's tables](https://aeb.win.tue.nl/codes/binary-1.html), read
2026-08-07.
