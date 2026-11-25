#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters.

Writes one Wi-Fi network name to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints the same text to stdout.

The name is fixed, deterministic, and needs no network, randomness,
or clock: the joke is baked in. The name is the password itself --
the ex's new boyfriend -- so one line tells the whole breakup:
she left, for him, and the router still remembers his name.
"""

import os
import stat

ENTRY = "Password: my ex's new boyfriend"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(ENTRY)


if __name__ == "__main__":
    main()
