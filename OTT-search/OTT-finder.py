# OTT-finder.py
import golly as g

# the next three lines are just a standard Python trick to figure out where the script is saved
import os
import sys
defaultfolder = os.path.abspath(os.path.dirname(sys.argv[0]))

# Change the next line to a hard-coded path if you don't want to have to
#   choose the constellations.txt file every time you run the script
constellation_fname = "C:/users/{USERNAME}/Desktop/constellations.txt"

glider = g.parse("3o$o$bo!")

# this script doesn't add a new layer, so it will overwrite whatever's in the current Golly universe
g.new("Constellation Test")

# backup way for the script to work:  have user choose a text file containing constellations
if constellation_fname == "C:/users/{USERNAME}/Desktop/constellations.txt":  # don't edit the path in this line
   constellation_fname = g.opendialog("Open constellation list", "Text files (*.txt)|*.txt", \
                                      defaultfolder, "constellations.txt", False)
   if constellation_fname == "": g.exit("No constellation list found.  Script has exited.")

# Load all constellations from the text file into memory
with open(constellation_fname, "r") as f:
  constellations = f.readlines()

x, y, count = 0, 0, 0
for item in constellations:
  if item.startswith("#"):
    continue
  rle = item.replace("\n","")  # Python readlines() function leaves a newline at the end of each line
  pat = g.parse(rle)
  
  # TODO: remove this next part of the code --
  #       it's just here for now to test that the file is getting read correctly
  g.putcells(pat, x, y)
  count += 1
  x += 20
  if x == 1000:
    x, y = 0, y + 16
    g.fit()
    g.update()
g.note("Total constellations found in file: " + str(count))
