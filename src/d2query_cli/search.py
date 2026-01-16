from __future__ import annotations

import difflib
from dataclasses import dataclass

from .dataset import Ability


@dataclass(frozen=True)
class Match:
    score: float
    item: Ability


def _norm(s: str) -> str:
    return " ".join(s.lower().split())


def search_abilities(items: list[Ability], query: str, *, top: int = 5) -> list[Match]:
    q = _norm(query)
    scored: list[Match] = []
    for it in items:
        hay = _norm(f"{it.name} {it.klass} {it.subclass} {it.text}")
        # quick ratio; good enough for v1
        score = difflib.SequenceMatcher(None, q, hay).ratio()
        if q in hay:
            score += 0.25
        scored.append(Match(score=score, item=it))

    scored.sort(key=lambda m: m.score, reverse=True)
    return scored[: max(1, top)]
