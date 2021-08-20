#!/usr/bin/env python3

import argparse
import os
import subprocess


def main():
    cli = argparse.ArgumentParser()
    cli.add_argument("--fresh", "-f", action="store_true")
    args = cli.parse_args()

    builddir = os.path.dirname(os.path.abspath(__file__))

    print(builddir)

    with open("/home/kevin/.ssh/id_rsa.pub") as fd:
        keys = fd.read()

    podman = [
        f"podman build -t sft/openage:sid",
        f'--build-arg authorized_keys="{keys}"',
        f"{builddir}/.",
    ]

    if args.fresh:
        podman.append("--no-cache")


    cmd = ['su', '-', 'falk', '-c', " ".join(podman)]
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd)


if __name__ == "__main__":
    main()
