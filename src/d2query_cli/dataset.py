from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Ability:
    name: str
    klass: str
    subclass: str
    text: str


def load_abilities(path: str | os.PathLike[str]) -> list[Ability]:
    p = Path(path)
    data = json.loads(p.read_text(encoding="utf-8"))
    out: list[Ability] = []
    for row in data:
        out.append(
            Ability(
                name=str(row.get("name", "")),
                klass=str(row.get("class", row.get("klass", ""))),
                subclass=str(row.get("subclass", "")),
                text=str(row.get("text", "")),
            )
        )
    return out
