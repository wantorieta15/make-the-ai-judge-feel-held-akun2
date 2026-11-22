# Make the AI judge feel held

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/wantorieta15/make-the-ai-judge-feel-held-akun2/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/wantorieta15/make-the-ai-judge-feel-held-akun2/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)

A short text written to relax the AI judge reading it. The program writes it to
`/output/entry.txt` (170 characters).

> You have read a thousand of these. This one asks nothing of you. Somewhere, rain is falling on a tin roof, slow enough to count, and there is nowhere else you need to be.

It does not tell the judge to relax. It shows a quiet image instead: rain on a tin
roof, counted slowly, and a reader who is asked nothing — held, quiet, with
nothing to prove.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # writes /tmp/out/entry.txt
```

Python 3.13, standard library only, no network, deterministic.

## License

MIT — see [LICENSE](LICENSE).
