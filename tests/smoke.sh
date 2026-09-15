#!/usr/bin/env bash
set -euo pipefail

test "$(curl -fsS http://127.0.0.1:8090/health)" = "ok"
body="$(curl -fsS --get --data-urlencode \
  'host=127.0.0.1; id; cat /srv/edge/config/deploy.env' \
  http://127.0.0.1:8090/check)"
grep -q 'uid=.*www-data' <<< "$body"
grep -q 'OPS_HOST=ops' <<< "$body"
grep -q 'OPS_USER=operator' <<< "$body"
if curl -fsS --max-time 2 http://127.0.0.1:2222 >/dev/null 2>&1; then
  echo "unexpected published SSH port" >&2
  exit 1
fi
echo "smoke checks passed"
