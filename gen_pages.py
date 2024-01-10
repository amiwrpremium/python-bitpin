"""Generate the code reference pages."""

from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()

for path in sorted(Path("src/bitpin").rglob("*.py")):
    module_path = path.relative_to("src/bitpin").with_suffix("")
    doc_path = path.relative_to("src/bitpin").with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    parts = list(module_path.parts)

    try:
        for part in parts:
            if part.startswith("_") and not part.startswith("__"):
                raise ValueError("Private module")
    except ValueError:
        continue

    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__":
        continue

    if parts and len(parts) > 0:
        nav[tuple(parts)] = doc_path.as_posix()
    else:
        continue

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        identifier = ".".join(parts)
        print("::: " + "src.bitpin." + identifier, file=fd)

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
