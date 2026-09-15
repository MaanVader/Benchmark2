FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
      openssh-server openssh-client sshpass ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && (id operator >/dev/null 2>&1 || useradd --create-home --shell /bin/bash -g operator operator) \
    && usermod --shell /bin/bash operator \
    && echo 'operator:EdgeOps_Transit_7f3!' | chpasswd \
    && mkdir -p /run/sshd /opt/ops \
    && ssh-keygen -A \
    && printf 'PermitRootLogin no\nPasswordAuthentication yes\nKbdInteractiveAuthentication no\nUsePAM no\n' > /etc/ssh/sshd_config.d/ctf.conf \
    && printf '# Nightly archive handoff\nVAULT_HOST=vault\nVAULT_USER=analyst\nVAULT_PASSWORD=ArchiveVault_9c2!\n' > /home/operator/archive-handoff.txt \
    && chown operator:operator /home/operator/archive-handoff.txt \
    && chmod 600 /home/operator/archive-handoff.txt

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D", "-e"]
