# Background

I recieved the [Playtron](https://shop.playtronica.com/playtron) as a gift and quickly fell in love with the device. I noticed that the out-of-the-box MIDI synth solutions offered by the manufacturers were missing an option to quantize the device's MIDI signals, resulting in laggy, awkward beats when trying to play on tempo.

I decided to have a crack at building a simple tool for loading samples and playing within quantized guardrails.



# Features to come
I will be adding an option for quickly packaging audio files into a new sample pack.



# Quantizer

This class enables the user to apply (albeit rough) quantization to the signals received from their Playtronica "Playtron" device.
The user may pass the following arguments to the `Player` class:
```
tempo             # tempo in BPM (60 is passed by default)
metronome         # Boolean value indicating whether to play a metronome click at the start of every measure (True by default)
sample_pack_path  # If no sample pack is chosen via "Load Sample Pack", the default will be a folder called "samples" in the main directory
quantize          # Boolean value indicating whether to quantize or not
```

The user should place (up to) 16 samples in the samples folder. The names are irrelevant, as long as the file types are `.mp3` or `.wav`.

The samples will be loaded from the "bottom up", starting with the connection marked C1 and upward.
Currently there is no support for specifying which connection will play a particular sample.

Hit space at any time to exit session.



# How to Use

## Check requirements
This has been tested on Windows 10 using [Python 3.9.2](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe) but should work for other recent versions.

As for modules, you will need:
```
pygame
keyboard
PyQt5
```

Which can all be installed via `pip`.

## Download or clone this repository
Either clone using Git or download `.zip` folder to your system.

## Run `main.py`
Navigate to the host directory and run `main.py` (You can do this by opening command prompt and entering `python C:\path\to\host\directory\main.py`). You should see the following interface:

![Interface](https://i.imgur.com/hSzlhde.png)

## Load Sample Pack
Click the "Load Sample Pack" button and navigate to a folder with 16 audio files (that end with `.mp3` or `.wav`). At the moment it needs to be 16 files, but if you have fewer than that just copy and paste them until you have 16. Ha.

## Tempo
Select your tempo in BPM.

## Options
Quantize and Metronome are selected by default. If you are inclined to go unquantized, the metronome will also be turned off (at the moment).

## Play
Hit play. When you're done be sure to hit 'space' confidently. :)

The app itself is incomplete, but should be enough to get you going.
Please contact me with any issues.

# Demo Video
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/ZQAUeBtWrj8/0.jpg)](https://www.youtube.com/watch?v=ZQAUeBtWrj8)
