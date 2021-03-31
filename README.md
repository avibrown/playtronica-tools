# Quantizer

This class enables the user to apply (albeit rough) quantization to the signals received from their Playtronica PLAYTRON device.
The user may pass the following arguments to the `Player` class:
```
tempo <-- tempo in BPM (60 is passed by default)
metronome <-- Boolean value indicating whether to play a metronome click at the start of every measure (True by default)
```

The user should place (up to) 16 samples in the samples folder. The names are irrelevant, as long as the file types are `.mp3` or `.wav`.

The samples will be loaded from the "bottom up", starting with the connection marked C1 and upward.
Currently there is no support for specifying which connection will play a particular sample.