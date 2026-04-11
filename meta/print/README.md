# Printable technical v0.1 bundle

The script `bundle_v01_technical.py` **only reads** canonical markdown under this repository (and optionally the sibling `oesis-runtime/README.md`). It **writes** under `build/print/`, which is gitignored—your source specs are never modified.

## Makefile (from repo root)

| Target | What it builds |
|--------|------------------|
| `make print-bundle` | Core `architecture/current` reading order only |
| `make print-bundle-full` | Core + extras + bench-air + runtime README (if sibling exists) |
| `make print-bundle-pdf` | Same as full, then [Pandoc](https://pandoc.org/) → `.pdf` |

## CLI

```bash
# Core frozen lane only (architecture/current reading order)
python3 meta/print/bundle_v01_technical.py

# Include alignment docs, implementation matrix, operator quickstart
python3 meta/print/bundle_v01_technical.py --extras

# Also append bench-air hardware guides
python3 meta/print/bundle_v01_technical.py --extras --bench-air

# Custom output path
python3 meta/print/bundle_v01_technical.py -o /tmp/v01.md

# After writing markdown, run pandoc (must be on PATH)
python3 meta/print/bundle_v01_technical.py --extras --bench-air --pdf
python3 meta/print/bundle_v01_technical.py --pdf --pdf-output /tmp/v01.pdf
```

Default markdown output: `build/print/v0.1-technical-bundle.md`. With `--pdf`, the default PDF is the same path with a `.pdf` suffix.

## PDF

`--pdf` shells out to `pandoc <md> -o <pdf>`. You need a working PDF engine (often LaTeX or another backend Pandoc is configured to use). If `pandoc` is missing, the script exits with an error after writing the `.md`.
