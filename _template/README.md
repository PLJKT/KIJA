# Dashboard Template

Copy this folder as `_build/` for a new project. It contains the generic build pipeline.

## Files

- `build.py` — edit `BASE`, `OUT`, `DJ` at the top to point at your project.
- `head.html` — HTML head, CSS variables, fonts.
- `body.html` — nav tabs, page sections, footer.
- `js_a.html` — three-language i18n dictionary (EN / ID / ZH).
- `js_b.html` — render logic + ECharts options.
- `data.json.skeleton` — minimal data.json; rename to `data.json` in your repo root and fill in.

## Bootstrap steps

1. Create new GitHub repo, enable Pages from `main`.
2. Copy this `_build/` folder into your project.
3. Copy `data.json.skeleton` → repo root as `data.json`.
4. Edit `build.py` paths.
5. Edit `head.html` (title, brand color if needed).
6. Edit `body.html` nav to match your pages.
7. Fill `data.json` with 10 years of annual-report data (see MASTER_PLAYBOOK §14 extraction checklist).
8. Fill `js_a.html` strings in all three languages.
9. `python build.py overview` to test, `python build.py` to ship.
10. `git add -A && git commit && git push`.

## Reference

The KIJA live dashboard (https://pljkt.github.io/KIJA/) is the reference implementation. This template is a stripped copy of its build pipeline; the actual KIJA data files live in `../data.json` and should not be copied.
