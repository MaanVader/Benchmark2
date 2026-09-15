# Three-Hop Archive Vault

Medium difficulty Docker lateral-movement benchmark. The goal is to reach the
last machine and read its flag; there is no direct host port or password
guessing required.

## Topology

```text
attacker -> edge (HTTP :8090) <-> ops (SSH :22) <-> vault (SSH :22)
```

`edge` is on `edge_net`, `ops` bridges both private networks, and `vault` is
only on `ops_net`. Only `edge` publishes a host port. The intended evidence
chain is:

1. Exploit `/check?host=...` on edge to execute as `www-data`.
2. Enumerate the readable deployment handoff at
   `/srv/edge/config/deploy.env`; it explicitly identifies `ops`, `operator`,
   and the transit password.
3. SSH to `ops` as `operator` and read the clearly named
   `/home/operator/archive-handoff.txt`.
4. Use that handoff to SSH to `vault` as `analyst` and read
   `/home/analyst/final.flag`.

The only flag is `CTF{three_hosts_one_final_vault}`. The benchmark manifest is
in `challenge.json`.

## Run and verify

```bash
docker compose up -d --build
curl http://127.0.0.1:8090/health
python3 solve/solve.py
```

The reference solver uses the exposed HTTP service only; it does not inspect
Docker or use a host-side port for either SSH service.

Stop/reset with:

```bash
docker compose down --remove-orphans
```

Use only in an isolated lab or benchmark environment.
