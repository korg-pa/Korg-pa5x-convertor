# Audio Processor Module

class AudioProcessor:
    def __init__(self):
        pass

    def create_multisamples(self, volume=1.0):
        """Automatically creates multisamples with the specified volume (default 100%)."""
        # Volume scaling logic here
        print(f"Creating multisamples with {volume * 100}% volume.")

    def create_sound_with_effects(self, effects):
        """Creates sounds with the specified effects (e.g., reverb, delay, etc.)."""
        # Effects application logic here
        for effect in effects:
            print(f"Applying {effect} effect to the sound.")

    def create_performance(self, sounds):
        """Distributes sounds across all keyboard keys from first to last."""
        # Performance creation logic here
        for i, sound in enumerate(sounds):
            print(f"Assigning {sound} to key {i + 1}.")

# Example usage:
# audio_processor = AudioProcessor()
# audio_processor.create_multisamples()
# audio_processor.create_sound_with_effects(['reverb', 'delay'])
# audio_processor.create_performance(['piano', 'string', 'brass'])