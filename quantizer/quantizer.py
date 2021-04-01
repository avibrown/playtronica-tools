import pygame.mixer as mixer
import pygame.midi as midi
import keyboard
import threading
import pygame
import time
import os

class Player():
    def __init__(self, quantize=True, sample_pack_path=None, metronome=True, tempo=60):
        pygame.init()
        mixer.init()
        midi.quit()
        midi.init()
        mixer.set_num_channels(32)

        self.state = True


        self.quantize = quantize
        quit_thread = threading.Thread(target=self.quit)
        quit_thread.start()

        # Fetches Playtron from list of available MIDI input devices
        self.input = self.get_input()

        # Creates list of samples from folder "samples". Place up to 16 audio files (.mp3, .wav, etc.) in this folder.
        if sample_pack_path:
            self.samples = self.get_samples(sample_pack_path)
        else:
            self.samples = self.get_samples('samples')

        # Tempo is passed to object in BPM, and here converted to value in seconds
        self.tempo = round(1 / (tempo / 60), 1)

        self.metronome = metronome

        # Initialize session
        self.session(metronome=self.metronome, tempo=self.tempo)

    def play(self, samples):
        # Checks if input has a reading, extracts the midi code(s) from note(s) in signal, and plays the note(s) 
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
        click = mixer.Sound('click.mp3')
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
            if keyboard.is_pressed('space'):
                self.state = False
                midi.quit()
            time.sleep(0.05)


    @staticmethod
    def get_input():
        # Parses available MIDI devices (input and output)
        devices = [midi.get_device_info(device) for device in range(0, midi.get_count())]

        # Locates the Playtronic input ID
        for device in devices:
            if b'Playtron' in device[1] and device[2] == 1:
                return midi.Input(devices.index(device))

    @staticmethod
    def get_samples(sample_pack_path):
        samples = {}
        files = [file for file in os.listdir(sample_pack_path)]

        # This index corresponds to the inidividual MIDI note values on the Playtronic - values from 36 to 51
        i = 36
        for file in files:
            if file.endswith('.mp3') or file.endswith('.wav'):
                samples[i] = mixer.Sound(f'{sample_pack_path}/{file}')
                i += 1
            if i >= 52:
                break
        return samples

if __name__ == "__main__":
    play = Player()