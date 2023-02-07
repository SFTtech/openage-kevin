#!/usr/bin/env python3

import argparse
import os
import subprocess
import getpass

def main():
    cli = argparse.ArgumentParser()
    cli.add_argument("--fresh", "-f", action="store_true")
    args = cli.parse_args()

    builddir = os.path.dirname(os.path.abspath(__file__))

    print(builddir)

    with open("/home/kevin/.ssh/id_rsa.pub") as fd:
        keys = fd.read()

    podman = [
        "podman", "build", "-t", "sft/openage:sid",
        "--build-arg", f'authorized_keys={keys}',
        f"{builddir}/.",
    ]

    if args.fresh:
        podman.append("--no-cache")

    if getpass.getuser() != 'falk':
        cmd = ['su', '-', 'falk', '-c', " ".join(podman)]
    else:
        cmd = podman
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd)


if __name__ == "__main__":
    main()
