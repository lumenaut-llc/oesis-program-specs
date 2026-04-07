# OESIS Runtime Pointer

This directory no longer hosts the runtime implementation.

The canonical runtime repository now lives at:

- `../oesis-runtime`

Use the sibling runtime repo for:

- `make oesis-demo`
- `make oesis-validate`
- `make oesis-check`
- `make oesis-http-check`

From this specs repository, those commands are proxied through the root
`Makefile` to `../oesis-runtime`.
