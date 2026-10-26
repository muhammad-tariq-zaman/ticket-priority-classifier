"""Ticket priority classifier: keyword-based P1-P4 with rationale words."""
import argparse
import sys

RULES = [
    ("P1", ["outage", "down", "critical", "production down", "data loss", "security breach"]),
    ("P2", ["urgent", "blocked", "cannot work", "major", "failing", "crash"]),
    ("P3", ["slow", "error", "issue", "not working", "problem", "broken"]),
    ("P4", ["question", "request", "how to", "enhancement", "suggestion", "access request"]),
]


def classify(text):
    lowered = text.lower()
    for priority, words in RULES:
        matched = [w for w in words if w in lowered]
        if matched:
            return {"priority": priority, "matched": matched,
                    "rationale": f"Matched {priority} keyword(s): {', '.join(matched)}"}
    return {"priority": "P4", "matched": [],
            "rationale": "No priority keyword matched; defaulted to P4."}


def main(argv=None):
    p = argparse.ArgumentParser(description="Classify helpdesk ticket priority.")
    p.add_argument("text", nargs="+")
    args = p.parse_args(argv)
    r = classify(" ".join(args.text))
    print(f"{r['priority']}  {r['rationale']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
