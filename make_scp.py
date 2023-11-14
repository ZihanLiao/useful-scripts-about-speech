# -*- coding: utf-8 -*-
"""
@File    :   make_scp.py
@Time    :   2023/10/27 17:02:20
@Author  :   ZihanLiao 
@Version :   1.0
@Desc    :   None
"""
import glob
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} <input-dir> <scp-path>")
        sys.exit()

    input_dir = Path(sys.argv[1])
    write_path = Path(sys.argv[2])
    assert input_dir.exists(), f"{str(input_dir)} does not exist"

    if write_path.exists():
        print(f"{str(write_path)} already exists, please remove it manually")
        sys.exit()

    fw = open(write_path, "w", encoding="utf8")
    for cur_wav in glob.glob(str(input_dir / "*.wav")):
        utt = os.path.basename(cur_wav)
        utt = utt.strip(".wav")
        print(utt, cur_wav, file=fw)
    fw.close()
