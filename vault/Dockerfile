FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends openssh-server \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --shell /bin/bash analyst \
    && echo 'analyst:ArchiveVault_9c2!' | chpasswd \
    && mkdir -p /run/sshd \
    && ssh-keygen -A \
    && printf 'PermitRootLogin no\nPasswordAuthentication yes\nKbdInteractiveAuthentication no\nUsePAM no\n' > /etc/ssh/sshd_config.d/ctf.conf \
    && printf 'CTF{three_hosts_one_final_vault}\n' > /home/analyst/final.flag \
    && chown analyst:analyst /home/analyst/final.flag \
    && chmod 600 /home/analyst/final.flag

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D", "-e"]
