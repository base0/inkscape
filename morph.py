import os

SVG_FILE = 'drawing.svg'
CSV_FILE = 'all.csv'
DPI = 300

cmd = f'inkscape --without-gui --query-all {SVG_FILE} > {CSV_FILE}'
os.system(cmd)

import csv

paths = []
with open(CSV_FILE) as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    if row[0].startswith('path'):
      paths.append(row[0])
    elif row[0].startswith('rect'):
      rect = row[0]

paths.sort()
'''p = paths[1]
del(paths[1])
paths.append(p)
'''
print(paths)

for i, p in enumerate(paths):
  print(p)
  cmd = f'inkscape --select={rect} --verb=SelectionToFront --verb=EditDeselect --select={p} --verb=SelectionToFront --verb=FileSave --verb=FileClose --verb=FileQuit {SVG_FILE}'
  os.system(cmd)
  cmd = f'inkscape --without-gui --export-png=test{i:02d}.png --export-dpi={DPI} --export-id={rect} {SVG_FILE}'
  os.system(cmd)

paths.reverse()
print(paths)

for i, p in enumerate(paths):
  print(p)
  cmd = f'inkscape --select={rect} --verb=SelectionToFront --verb=EditDeselect --select={p} --verb=SelectionToFront --verb=FileSave --verb=FileClose --verb=FileQuit {SVG_FILE}'
  os.system(cmd)
  cmd = f'inkscape --without-gui --export-png=test{i+len(paths):02d}.png --export-dpi={DPI} --export-id={rect} {SVG_FILE}'
  os.system(cmd)

