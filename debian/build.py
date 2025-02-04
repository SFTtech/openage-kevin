#!/usr/bin/env python3

import argparse
import os
import subprocess
import getpass
import shlex


def main():
    cli = argparse.ArgumentParser()
    cli.add_argument("variant", choices=["sid", "stable"])
    cli.add_argument("--fresh", "-f", action="store_true")
    args = cli.parse_args()

    builddir = os.path.dirname(os.path.abspath(__file__))

    print(builddir)

    with open("/home/kevin/.ssh/id_rsa.pub") as fd:
        keys = fd.read().strip()

    variant = args.variant

    podman = [
        "podman", "build", "-t", f"sft/openage:{variant}",
        "-f", f"{builddir}/{variant}/Dockerfile",
        "--build-arg", f"authorized_keys={keys}",
        f"{builddir}/{variant}/.",
    ]

    if args.fresh:
        podman.append("--no-cache")

    if getpass.getuser() != 'justin':
        cmd = ['su', '-', 'justin', '-c', shlex.join(podman)]
        print(f"$ {' '.join(cmd)}")
    else:
        cmd = podman
        print(f"$ {shlex.join(cmd)}")

    subprocess.run(cmd)


if __name__ == "__main__":
    main()
