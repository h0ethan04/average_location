# Average Location calculator

Uses a combination of the openmaps Nominatim api and some math to calculate distance a series of locations are from a central location

Usage requirements:
- If you want to use this program and have Python installed, Python 3.11 or newer is required.
- Otherwise, extract all the files from the zip and you will have an executable

to use the .exe: 
1. make sure you meet the requirements
2. download and extract the files from the zip
3. make sure that you're connected to the internet
4. create a txt file containing your center location and addresses, following the format described below
5. place the txt file into the same directory as the .exe contained in this zip
6. run the .exe and follow the instructions

to use the files with a Python installation:
1. make sure you meet the requirements
2. download all files except for the zip
3. ensure that you're connected to the internet
4. create a txt file (or modify the example file named addresses.txt)
5. run the main file, which is named avg_distance_calc.py
6. follow the instructions


file format:
- lines can either be blank, contain ONLY a valid address, contain ONLY the word "center" or contain ONLY the word "location" followed by a colon
- valid addresses do not include suite or apt numbers

example file:
```
center:

9531 Bond Rd, Elk Grove, CA 95624

location:

9950 Elk Grove Florin Rd, Elk Grove, CA 95624

```