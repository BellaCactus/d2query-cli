<div align="center">

# d2query-cli

destiny 2 query cli: search a local dataset and print results as terminal-friendly cards (optional html output).

![python](https://img.shields.io/badge/python-3.11%2B-0b0b0b?style=for-the-badge)
![cli](https://img.shields.io/badge/interface-cli-ff78c8?style=for-the-badge)
![license](https://img.shields.io/badge/license-mit-0b0b0b?style=for-the-badge)

</div>

---

## what is this?

d2query-cli is a command-line search tool for a destiny 2 mini-codex dataset.

it is meant for:
- quick ability/perk lookups
- "what does this thing do again?" checks
- generating a small html report for sharing

note: this project does not require a backend. it is designed to be lightweight and offline-friendly.

---

## install

requires python 3.11+.

```bash
python -m venv .venv
# windows
.venv\Scripts\activate
# mac/linux
source .venv/bin/activate

python -m pip install -U pip
python -m pip install -e .
```

---

## usage

search abilities:

```bash
d2q abilities "threaded" --top 5
```

point at a dataset file:

```bash
d2q abilities "spike" --dataset data/abilities.json --top 10
```

write html output:

```bash
d2q abilities "threaded spike" --class hunter --subclass strand --top 5 --html out.html
```

---

## license

MIT. see `LICENSE`.
