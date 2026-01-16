from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .dataset import load_abilities
from .html_report import render
from .search import search_abilities


def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="d2q", description="d2query-cli: terminal codex search")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("abilities", help="search abilities dataset")
    a.add_argument("query", help="search string")
    a.add_argument("--class", dest="klass", default=None)
    a.add_argument("--subclass", default=None)
    a.add_argument("--top", type=int, default=5)
    a.add_argument("--dataset", default=None, help="path to abilities.json")
    a.add_argument("--html", default=None, help="write html report")

    return p


def _default_dataset() -> Path:
    here = Path(__file__).resolve().parent
    # repo ships data in ../.. when editable install; fallback to relative
    candidate = (here.parent.parent / "data" / "abilities.json")
    if candidate.exists():
        return candidate
    return Path("data/abilities.json")


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)

    if args.cmd == "abilities":
        ds = Path(args.dataset) if args.dataset else _default_dataset()
        if not ds.exists():
            print(f"d2q: dataset not found: {ds}", file=sys.stderr)
            return 2

        items = load_abilities(ds)

        # crude filtering
        if args.klass:
            items = [i for i in items if i.klass.lower() == args.klass.lower()]
        if args.subclass:
            items = [i for i in items if i.subclass.lower() == args.subclass.lower()]

        matches = search_abilities(items, args.query, top=args.top)

        # terminal cards
        for m in matches:
            it = m.item
            print(f"[{m.score:.3f}] {it.name} ({it.klass} • {it.subclass})")
            txt = it.text.strip()
            if len(txt) > 420:
                txt = txt[:419] + "…"
            for line in txt.splitlines()[:12]:
                print(f"  {line}")
            print()

        if args.html:
            Path(args.html).write_text(render(matches, query=args.query), encoding="utf-8")
            print(f"wrote html: {args.html}")

        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
