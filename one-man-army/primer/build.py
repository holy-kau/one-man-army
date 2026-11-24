"""Build the primer: inject every kit file into the page template as JSON."""
import json, pathlib, sys

kit = pathlib.Path(sys.argv[1])
tpl = pathlib.Path(sys.argv[2])
out = pathlib.Path(sys.argv[3])

files = {p.relative_to(kit).as_posix(): p.read_text(encoding="utf-8")
         for p in sorted(kit.rglob("*.md"))}
blob = json.dumps(files, ensure_ascii=False).replace("</", "<\\/")
html = tpl.read_text(encoding="utf-8").replace("/*KIT_JSON*/", blob, 1)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(html, encoding="utf-8")
print(f"{len(files)} kit files, {len(html)//1024} KB -> {out}")
