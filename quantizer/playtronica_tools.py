import os

import pygame.midi as midi
import pygame.mixer as mixer


class Input:
    def get_input():
        playtron = None
        midi.init()

        # Parses available MIDI devices (input and output)
        devices = [
            midi.get_device_info(device) for device in range(0, midi.get_count())
        ]

        # Locates the Playtronic input ID
        if len(devices) > 0:
            for device in devices:

                # Searching for Playtron's name and the INPUT connection
                if b"Playtron" in device[1] and device[2] == 1:
                    playtron = midi.Input(devices.index(device))

        if playtron:
            return playtron

        else:
            raise ValueError("No Playtron device found connected.")


class Samples:
    def get_samples(sample_pack_path):
        mixer.init()
        samples = {}

        if sample_pack_path:
            files = [file for file in os.listdir(sample_pack_path)]

            # "Plumps" sample pack to 16 files (repeats last file) if there are too few
            if not len(files) == 16:
                last = files.index(files[-1])
                for i in range(last + 1, 17):
                    files.append(files[last])

            # The Playtron sends MIDI codes between 36-51
            i = 36
            for file in files:
                if file.endswith(".mp3") or file.endswith(".wav"):
                    samples[i] = mixer.Sound(f"{sample_pack_path}/{file}")
                    i += 1
                if i >= 52:
                    break

            return samples

        else:
            return None
