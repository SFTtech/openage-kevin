FROM debian:stable

# install packages
COPY sources.list /etc/apt/sources.list
RUN apt update
RUN apt upgrade -y
RUN apt install -y tini apt-utils cmake flex make git gcc g++ openssh-server clang clang-tidy cython3 libeigen3-dev libepoxy-dev libfontconfig1-dev libfreetype-dev libharfbuzz-dev libogg-dev libopus-dev libopusfile-dev libpng-dev libsdl2-dev libsdl2-image-dev python3-dev python3-mako python3-jinja2 python3-lz4 python3-numpy python3-pil python3-pip python3-pygments python3-pycodestyle pylint python3-toml libtoml11-dev qml6-module-qtquick-controls qt6-declarative-dev ccache kitty-terminfo qt6-multimedia-dev qml6-module-qtquick3d-spatialaudio

# setup proxy
COPY environment /etc/

# setup user and ssh
RUN useradd -m chantal
RUN mkdir /home/chantal/.ssh
WORKDIR /home/chantal

RUN echo "[init]\n\tdefaultBranch = master" > /home/chantal/.gitconfig
ARG authorized_keys
ENV AUTHORIZED_KEYS=$authorized_keys
RUN echo "$AUTHORIZED_KEYS" > /home/chantal/.ssh/authorized_keys && echo "$AUTHORIZED_KEYS"
RUN chmod 700 /home/chantal/.ssh && chmod 644 /home/chantal/.ssh/authorized_keys
RUN chown -R chantal:root /home/chantal/.ssh && mkdir -p /var/run/sshd /run/sshd

RUN cat /etc/ssh/ssh_host_ed25519_key.pub

EXPOSE 22

## run systemd, which starts sshd
# currently doesn't work because of cgroup permission denied?
#CMD ["/sbin/init"]

# run tini + sshd
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["/usr/sbin/sshd", "-D", "-p", "22"]
