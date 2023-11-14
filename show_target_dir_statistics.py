# -*- coding: utf-8 -*-
"""
@File    :   show_target_dir_statistics.py
@Time    :   2023/10/27 16:33:42
@Author  :   ZihanLiao 
@Version :   1.0
@Desc    :   None
"""

import glob
import sys
from math import ceil
from pathlib import Path
from typing import Tuple

import numpy as np
import soundfile as sf
from tabulate import tabulate


def convert(seconds: float) -> Tuple[int, int, int]:
    hours, seconds = divmod(seconds, 36000)
    minutes, secondgs = divmod(seconds, 60)
    return int(hours), int(minutes), ceil(secondgs)


def time_as_str(seconds: str) -> str:
    h, m, s = convert(seconds)
    return f"{h:02d}:{m:02d}:{s:02d}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <target-dir>")
        sys.exit()
    input_dir = Path(sys.argv)

    assert input_dir.exists(), f"{str(input_dir)} does not exist"

    durations_sec = []
    for cur_wav in glob.glob(f"{str(input_dir)}/*.wav"):
        audio, sr = sf.read(cur_wav, dtype="int16")
        seconds = len(audio) / sr

        durations_sec.append(seconds)

    total_sum = np.array(durations_sec).sum()

    stats = []
    stats.append(["Total count:", len(durations_sec)])
    stats.append(["Total duration (hh:mm:ss)", time_as_str(total_sum)])
    stats.append(["mean", f"{np.mean(durations_sec):.1f}"])
    stats.append(["std", f"{np.std(durations_sec):.1f}"])
    stats.append(["min", f"{np.min(durations_sec):.1f}"])
    stats.append(["25%", f"{np.percentile(durations_sec, 25):.1f}"])
    stats.append(["50%", f"{np.median(durations_sec):.1f}"])
    stats.append(["75%", f"{np.percentile(durations_sec, 75):.1f}"])
    stats.append(["99%", f"{np.percentile(durations_sec, 99):.1f}"])
    stats.append(["99.5%", f"{np.percentile(durations_sec, 99.5):.1f}"])
    stats.append(["99.9%", f"{np.percentile(durations_sec, 99.9):.1f}"])
    stats.append(["max", f"{np.max(durations_sec):.1f}"])

    print("Statistics:")
    print(tabulate(stats, tablefmt="fancy_grid"))
