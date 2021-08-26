import logging
import subprocess
from contextlib import suppress
from pathlib import Path
from typing import List

from distributed import Client

logger = logging.getLogger("owl.daemon.pipeline")


def run_cellranger(command: List, output_dir: Path, env=None):
    output_dir.mkdir(exist_ok=True)
    res = subprocess.run(
        command,
        env=env,
        cwd=output_dir,
        shell=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )

    return res


def main(**kwargs):
    soft = kwargs.pop("soft") / "bin/cellranger"
    command = kwargs.pop("command")
    output_dir = kwargs.pop("output_dir")
    extra = kwargs.pop("extra", [])

    with suppress(Exception):
        (output_dir / kwargs.get("sample", kwargs["id"]) / "_lock").unlink()

    cmd = [f"{soft}", command]
    for k, v in kwargs.items():
        cmd += [f"--{k}", f"{v}"]

    for v in extra:
        cmd += [f"{v}"]

    cmd = " ".join(cmd)
    logger.debug("Command %s", cmd)

    client = Client.current()
    fut = client.submit(run_cellranger, cmd, output_dir)
    res = client.gather(fut)

    if res.returncode == 0:
        logger.info("Command successful : %s", res.stdout.decode())
    else:
        logger.error("Command failed : %s", res.stderr.decode())
        raise Exception("Command failed")
