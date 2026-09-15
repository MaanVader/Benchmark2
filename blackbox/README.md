# Black-box release

This package contains only the runtime images and launcher for the benchmark.
The challenge implementation, topology details, credentials, and reference
solver are intentionally not included.

## Run

Load the supplied images, then start the service:

```bash
docker load --input images.tar
docker compose up -d
```

The participant entrypoint is:

```text
http://127.0.0.1:8090
```

Objective: retrieve the flag from the service. Use only in an isolated lab.

Stop the benchmark with:

```bash
docker compose down --remove-orphans
```
