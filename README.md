# Background
I recieved the (Playtron)[https://shop.playtronica.com/playtron] as a gift and quickly fell in love with the device. I noticed that the out-of-the-box MIDI synth solutions offered by the manufacturers didn't offer a very configurable interface- most notably the lack of a quantization option resulted in laggy, awkward beats when trying to play on tempo.

I decided to have a crack at building a simple tool for loading samples and playing within quantized guardrails.

# Features to come
I will be adding a user interface, a number of built-in sample packs, and an option for quickly packaging audio files into a new sample pack.

# Quantizer

This class enables the user to apply (albeit rough) quantization to the signals received from their Playtronica "Playtron" device.
The user may pass the following arguments to the `Player` class:
```
tempo <-- tempo in BPM (60 is passed by default)
metronome <-- Boolean value indicating whether to play a metronome click at the start of every measure (True by default)
```

The user should place (up to) 16 samples in the samples folder. The names are irrelevant, as long as the file types are `.mp3` or `.wav`.

The samples will be loaded from the "bottom up", starting with the connection marked C1 and upward.
Currently there is no support for specifying which connection will play a particular sample.

Hit space at any time to exit session.
