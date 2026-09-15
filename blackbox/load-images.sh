#!/usr/bin/env bash
set -euo pipefail

docker load --input "$(dirname "$0")/images.tar"
