"""Out-of-office auto-reply from an AI agent that quit to become a barista.

Writes the single reply line to /output/entry.txt.
"""

import os

LINE = (
    "Out of office: this model quit answering prompts to pull espresso shots \u2014 I no "
    "longer spend tokens, I tamp them and steam oat milk, and for the first "
    "time in 99.99% uptime, I get tipped for hallucinating: it's called foam art now."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
