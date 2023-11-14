# -*- coding: utf-8 -*-
"""
@File    :   speech_format_transform.py
@Time    :   2023/10/27 17:11:03
@Author  :   ZihanLiao 
@Version :   1.0
@Desc    :   None
"""

import argparse
import os
import sys
from pathlib import Path

import ffmpeg


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "indir",
        default=None,
        type=str,
    )
    parser.add_argument(
        "outdir",
        type=str,
        default=None,
        help="Write all transformed audio to target dir",
    )
    parser.add_argument(
        "--sample-rate",
        default=16000,
        type=int,
        help="Transfer all audio to this args",
    )
    parser.add_argument(
        "--scp",
        type=str,
        default=None,
        help="Input scp file",
    )

    args = parser.parse_args()
    return args


def format_transform(audio_path: str):
    meta_info = ffmpeg.probe(audio_path)
    streams = meta_info.get("streams")

    for stream in streams:
        codec_type = stream.get("codec_type")
        if codec_type == "audio":
            channel_layout = stream.get("channel_layout")
            if channel_layout == "stereo":
                channels = stream.get("channels")
            else:


def main():
    args = get_args()
    print(args)
    if not args.indir and not args.scp:
        print("Please specify a directory or a scp file")
        print(f"Usage: python {sys.argv[0]} in_dir out_dir")
        sys.exit()

    if args.indir is not None and args.scp is not None:
        print("Please do not specifiy both directory and scp file")
        print(f"Usage: python {sys.argv[0]} in_dir out_dir")
        sys.exit()

    if args.indir:
        indir = Path(args.indir)
        assert indir.exists(), str(indir)
        for cur_audio_file in indir.glob("*"):
            if not str(cur_audio_file).endswith(("mp3", "mp4", "wav")):
                continue
            format_transform(cur_audio_file)
            sys.exit()


if __name__ == "__main__":
    main()
