# d2query-cli

terminal codex search (v1).

this repo is a scaffold: it ships with a tiny sample dataset so the CLI works offline.

## install

```bash
python -m pip install -e .
```

## usage

```bash
# search abilities
d2q abilities "threaded" --top 5

# use a custom dataset json
d2q abilities "spike" --dataset ./data/abilities.json

# write html report
d2q abilities "threaded" --top 5 --html out.html
```

## dataset format (v1)
`abilities.json` is a list of objects:

```json
[{"name":"Threaded Spike","class":"Hunter","subclass":"Strand","text":"..."}]
```
