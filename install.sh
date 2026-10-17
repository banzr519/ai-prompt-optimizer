#!/bin/sh
# Run from a reviewed checkout/archive. Never execute remote text via eval.
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ "$#" -eq 0 ]; then
    set -- install --source "$ROOT"
fi
if [ -n "${APO_PYTHON:-}" ]; then
    "$APO_PYTHON" -c 'import sys; sys.exit(sys.version_info < (3,9))' || exit 1
    exec "$APO_PYTHON" "$ROOT/scripts/manage_install.py" "$@"
fi
for candidate in python3 python; do
    if command -v "$candidate" >/dev/null 2>&1 && "$candidate" -c 'import sys; sys.exit(sys.version_info < (3,9))' 2>/dev/null; then
        exec "$candidate" "$ROOT/scripts/manage_install.py" "$@"
    fi
done
printf '%s\n' 'Python 3.9+ was not found. Ask Codex to locate an available runtime, or set APO_PYTHON to its executable path. Nothing was installed.' >&2
exit 1
