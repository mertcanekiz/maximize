#!/usr/bin/env python3
import os
import argparse

parser = argparse.ArgumentParser(description='maximize.py')
parser.add_argument('width', metavar='WIDTH', type=int, help='Width of the screen resolution you want')
parser.add_argument('height', metavar='HEIGHT', type=int, help='Height of the screen resolution you want')
parser.add_argument('screen', metavar='SCREEN', type=str, help='Name of the display (from xrandr)')
args = parser.parse_args()

w = args.width
h = args.height
screen = args.screen
gtf = os.popen(f'gtf {w} {h} 60').read()
gtf = gtf[gtf.find("Modeline") + len("Modeline"):]
gtf = gtf.strip()
modename = gtf[gtf.find('"'):gtf.find('"', 1)+1]
os.popen(f'sleep 5 && xrandr --newmode {gtf} && xrandr --addmode {screen} {modename} && xrandr --output {screen} --mode {modename}')
