import os
import threading
import time

import keyboard
import pygame
import pygame.midi as midi
import pygame.mixer as mixer

import playtronica_tools as pt


class Player:
    def __init__(self, quantize=True, sample_pack_path=None, metronome=True, tempo=60):
        self.state = True
        self.quantize = quantize
        self.metronome = metronome
        self.input = pt.Input.get_input()
        self.tempo = round(1 / (tempo / 60), 1)
        self.samples = pt.Samples.get_samples(sample_pack_path)

        print(self.samples)

        pygame.init()
        mixer.init()
        mixer.set_num_channels(32)
        midi.init()

        quit_thread = threading.Thread(target=self.quit)
        quit_thread.start()

        self.session(metronome=self.metronome, tempo=self.tempo)

    def play(self, samples):
        if self.input.poll():
            signal = self.input.read(1024)
            if signal[0][0][0] == 144:
                for note in signal:
                    self.samples[note[0][1]].play()

    def play_unquantized(self, samples):
        if self.input.poll():
            signal = self.input.read(1024)
            if signal[0][0][0] == 144:
                for note in signal:
                    self.samples[note[0][1]].play()

    def session(self, metronome, tempo):
        self.state = True
        midi.init()
        click = mixer.Sound("click.mp3")
        count = 4

        if self.quantize:
            while self.state:
                if metronome:
                    if count % 4 == 1:
                        click.play()
                self.play(self.samples)
                count += 1
                time.sleep(tempo / 4)

        elif not self.quantize:
            while self.state:
                self.play_unquantized(self.samples)

    def quit(self):
        while True:
            if keyboard.is_pressed("space"):
                self.state = False
                midi.quit()
            time.sleep(0.05)


if __name__ == "__main__":
    play = Player()
