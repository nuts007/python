#coding: utf-8

import numpy as np
import pandas as pd
import io
import os
import sys
import csv
import json
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", default=None)
    args = parser.parse_args()
    if args.filename == None:
        print("don't find config file")
    else:
        with open(args.filename, "r") as f:
            config = json.load(f)
            print(config)

if __name__ == "__main__":
    main()



