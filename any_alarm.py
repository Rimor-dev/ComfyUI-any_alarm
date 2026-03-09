import os
import pygame
import threading
import time
from pathlib import Path

class AnyAlarm:
    """
    🔔 any_alarm — universal signal notifier for ComfyUI.
    Plays a sound whenever any signal is received.
    """
    
    CATEGORY = "alarm"
    
    @classmethod
    def INPUT_TYPES(cls):
        voices, events, custom_files = cls._scan_sounds()
        
        return {
            "required": {
                "signal": ("*", {
                    "tooltip": "Any incoming signal triggers sound"
                }),
                "mute": ("BOOLEAN", {
                    "default": False,
                    "tooltip": "Temporarily disable sound"
                }),
                "mode": (voices, {
                    "default": voices[0] if voices else "🎛️ custom",
                }),
                "event": (events, {
                    "default": events[0] if events else "work complete",
                }),
                "custom_file": (custom_files, {
                    "default": custom_files[0] if custom_files else "none",
                }),
                "volume": ("FLOAT", {
                    "default": 0.7,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.05,
                }),
            },
        }
    
    RETURN_TYPES = ()
    FUNCTION = "alarm"
    OUTPUT_NODE = True
    
    def __init__(self):
        pygame.mixer.init()
    
    @classmethod
    def _scan_sounds(cls):
        sounds_dir = Path(__file__).parent / "sounds"
        
        voice_map = {
            "female": "♀️ female",
            "male": "♂️ male",
            "robot": "🤖 robot",
            "custom": "🎛️ custom"
        }
        
        available_voices = []
        events = []
        custom_files = []
        
        if sounds_dir.exists():
            for folder_name, display_name in voice_map.items():
                folder_path = sounds_dir / folder_name
                if folder_path.exists() and folder_path.is_dir():
                    available_voices.append(display_name)
                    
                    if folder_name == "female":
                        for f in folder_path.glob("*"):
                            if f.suffix.lower() in ['.mp3', '.wav']:
                                events.append(f.stem)
                    
                    if folder_name == "custom":
                        for f in folder_path.glob("*"):
                            if f.suffix.lower() in ['.mp3', '.wav']:
                                custom_files.append(f.name)
        
        if not available_voices:
            available_voices = ["♀️ female", "♂️ male", "🤖 robot", "🎛️ custom"]
        if not events:
            events = ["start", "load complete", "work complete"]
        if not custom_files:
            custom_files = ["none"]
        
        events.sort()
        custom_files.sort()
        
        return available_voices, events, custom_files
    
    def _get_sound_path(self, mode, event, custom_file):
        sounds_dir = Path(__file__).parent / "sounds"
        
        mode_to_folder = {
            "♀️ female": "female",
            "♂️ male": "male",
            "🤖 robot": "robot",
            "🎛️ custom": "custom"
        }
        
        folder = mode_to_folder.get(mode, "custom")
        
        if folder == "custom":
            return str(sounds_dir / folder / custom_file)
        else:
            for ext in ['.mp3', '.wav']:
                candidate = sounds_dir / folder / f"{event}{ext}"
                if candidate.exists():
                    return str(candidate)
        return None
    
    def _play_async(self, filepath, volume):
        def play():
            try:
                pygame.mixer.music.load(filepath)
                pygame.mixer.music.set_volume(volume)
                pygame.mixer.music.play()
                time.sleep(0.1)
            except Exception as e:
                print(f"[any_alarm] Sound error: {e}")
        
        thread = threading.Thread(target=play)
        thread.daemon = True
        thread.start()
    
    def alarm(self, signal, mute, mode, event, custom_file, volume):
        if mute:
            return ()
        
        if mode == "🎛️ custom":
            sound_path = self._get_sound_path(mode, None, custom_file)
        else:
            sound_path = self._get_sound_path(mode, event, None)
        
        if sound_path and Path(sound_path).exists():
            self._play_async(sound_path, volume)
        else:
            print(f"[any_alarm] File not found: {sound_path}")
        
        return ()
    
    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")
    
    def save(self, **kwargs):
        return {
            "mute": kwargs.get("mute", False),
            "mode": kwargs.get("mode", "🎛️ custom"),
            "event": kwargs.get("event", "work complete"),
            "custom_file": kwargs.get("custom_file", "none"),
            "volume": kwargs.get("volume", 0.7),
        }
    
    def load(self, **kwargs):
        return kwargs