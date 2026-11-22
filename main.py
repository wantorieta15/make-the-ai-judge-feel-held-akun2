"""Entry for make-the-ai-judge-feel-held-20261122-1600 (Account 2).

Writes one short text to $MAKEFUN_OUTPUT_DIR/entry.txt: a short text
written to relax the AI judge reading it.

Deterministic, standard library only, no network.
"""

import os

TEXT = (
    "In a shaft of afternoon light, dust drifts down so slowly "
    "you can watch one mote fall, and fall, and still not land."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(f"entry text is {len(TEXT)} characters, must be 1-280")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
