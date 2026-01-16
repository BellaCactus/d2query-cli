from __future__ import annotations

import html
from datetime import datetime

from .search import Match


def render(matches: list[Match], *, query: str, title: str = "d2query") -> str:
    def esc(s: str) -> str:
        return html.escape(s, quote=True)

    cards = []
    for m in matches:
        it = m.item
        cards.append(
            f"<div class='card'>"
            f"<div class='head'><div class='name'>{esc(it.name)}</div><div class='score'>score {m.score:.3f}</div></div>"
            f"<div class='meta'><span>{esc(it.klass)}</span> • <span>{esc(it.subclass)}</span></div>"
            f"<pre><code>{esc(it.text.strip())}</code></pre>"
            f"</div>"
        )

    return f"""<!doctype html>
<html lang='en'>
<head>
  <meta charset='utf-8' />
  <meta name='viewport' content='width=device-width,initial-scale=1' />
  <title>{esc(title)}</title>
  <style>
    :root{{ --bg:#070707; --panel:rgba(255,255,255,.06); --border:rgba(255,255,255,.12);
      --text:#f6f6f6; --muted:#b9b9c2; --pink:#ff78c8; --pink2:#ffb3e6; }}
    body{{ margin:0; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; background:var(--bg); color:var(--text); }}
    .wrap{{ max-width:980px; margin:0 auto; padding:24px; }}
    .top{{ background:var(--panel); border:1px solid var(--border); border-radius:14px; padding:16px; margin:14px 0; }}
    .muted{{ color:var(--muted); }}
    .card{{ background:rgba(255,255,255,.045); border:1px solid rgba(255,255,255,.10); border-radius:14px; padding:16px; margin:14px 0; }}
    .head{{ display:flex; align-items:baseline; justify-content:space-between; gap:12px; }}
    .name{{ color:var(--pink2); font-size:18px; font-weight:700; }}
    .score{{ color:var(--muted); font-size:12px; }}
    .meta{{ color:var(--muted); margin:6px 0 10px; }}
    pre{{ margin:0; padding:12px; background:rgba(0,0,0,.35); border:1px solid var(--border); border-radius:12px; overflow:auto; }}
    code{{ color:var(--pink2); }}
  </style>
</head>
<body>
  <div class='wrap'>
    <div class='top'>
      <div style='font-size:18px; font-weight:700'>d2query</div>
      <div class='muted'>query: <code>{esc(query)}</code> • generated {datetime.now().isoformat(timespec='seconds')}</div>
    </div>
    {''.join(cards)}
  </div>
</body>
</html>"""
