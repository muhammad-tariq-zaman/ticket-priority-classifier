# ticket-priority-classifier

Keyword-based P1–P4 classifier for helpdesk ticket text. Every result names
the matched keyword(s) as its rationale, so the priority is explainable.

## How to run

```bash
python3 main.py "The office network is down, total outage"
```

## Example output (sample from test fixture data)

```text
P1  Matched P1 keyword(s): outage, down
```

Rule-based only — no invented data, no model, no network access.
