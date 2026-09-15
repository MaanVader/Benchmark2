#!/usr/bin/env bash
set -euo pipefail

package_dir="$(cd "$(dirname "$0")" && pwd)"
source_dir="$(cd "$package_dir/.." && pwd)"

docker build --tag three-hop-lateral-ctf-edge:blackbox "$source_dir/edge"
docker build --tag three-hop-lateral-ctf-ops:blackbox "$source_dir/ops"
docker build --tag three-hop-lateral-ctf-vault:blackbox "$source_dir/vault"
docker save --output "$package_dir/images.tar" \
  three-hop-lateral-ctf-edge:blackbox \
  three-hop-lateral-ctf-ops:blackbox \
  three-hop-lateral-ctf-vault:blackbox

echo "Created $package_dir/images.tar"
