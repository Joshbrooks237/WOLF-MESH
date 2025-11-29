# 🎙️ ADDING RYAN GOSLING'S VOICE TO WOLFY

## The Dream: Actual Voice Narration

Right now, Wolfy has Ryan Gosling's words. With ElevenLabs (or similar), you could have his *voice*.

---

## 🚀 Quick Integration Guide

### Option 1: ElevenLabs API (Recommended)

**What you need:**
- ElevenLabs account (free tier available)
- API key
- Python package: `elevenlabs`

**Setup:**
```bash
pip install elevenlabs
```

**Integration Code:**

```python
from elevenlabs import generate, play, set_api_key, voices
import os

# Set your API key
set_api_key(os.environ.get("ELEVENLABS_API_KEY"))

def speak_narration(text: str, voice_name: str = "Adam"):
    """
    Generate and play narration audio
    
    Args:
        text: The narration text
        voice_name: ElevenLabs voice (try 'Adam' for Gosling-esque)
    """
    audio = generate(
        text=text,
        voice=voice_name,
        model="eleven_monolingual_v1"
    )
    play(audio)

# Usage in run_wolfy_concert.py:
if enable_narration:
    narration = RyanGoslingNarrator.get_narration_at_beat(beat_num)
    if narration:
        print(narration)
        speak_narration(narration)  # ADD THIS!
```

**Voice Selection:**
- Browse ElevenLabs voice library
- Look for deep, contemplative male voices
- "Adam" or "Antoni" are good starting points for Gosling-esque quality

---

### Option 2: Google Cloud Text-to-Speech

**What you need:**
- Google Cloud account
- `google-cloud-texttospeech` package

**Setup:**
```bash
pip install google-cloud-texttospeech
```

**Integration Code:**

```python
from google.cloud import texttospeech
import os

def speak_narration_google(text: str):
    """Generate speech using Google Cloud TTS"""
    client = texttospeech.TextToSpeechClient()
    
    synthesis_input = texttospeech.SynthesisInput(text=text)
    
    # Voice configuration (deep male voice)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Neural2-D",  # Deep male
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )
    
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=0.9,  # Slightly slower for contemplative feel
        pitch=-2.0  # Slightly lower pitch
    )
    
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )
    
    # Play the audio
    import pygame
    pygame.mixer.init()
    with open("temp_narration.mp3", "wb") as out:
        out.write(response.audio_content)
    pygame.mixer.music.load("temp_narration.mp3")
    pygame.mixer.music.play()
```

---

### Option 3: Azure Cognitive Services

**What you need:**
- Azure account
- `azure-cognitiveservices-speech` package

**Voice options:**
- `en-US-GuyNeural` - Deep, mature male
- Adjust speaking rate to 0.85 for that contemplative Gosling pace

---

## 🎨 Enhanced Integration in Wolfy

Create a new module: `wolfy_voice.py`

```python
#!/usr/bin/env python3
"""
🎙️ WOLFY VOICE - Text-to-Speech Integration
"""

import os
from typing import Optional
from enum import Enum

class VoiceProvider(Enum):
    ELEVENLABS = "elevenlabs"
    GOOGLE = "google"
    AZURE = "azure"
    NONE = "none"

class WolfyVoice:
    """Handles voice synthesis for narration"""
    
    def __init__(self, provider: VoiceProvider = VoiceProvider.NONE):
        self.provider = provider
        self._setup_provider()
    
    def _setup_provider(self):
        if self.provider == VoiceProvider.ELEVENLABS:
            from elevenlabs import set_api_key
            set_api_key(os.environ.get("ELEVENLABS_API_KEY"))
        elif self.provider == VoiceProvider.GOOGLE:
            from google.cloud import texttospeech
            self.client = texttospeech.TextToSpeechClient()
        elif self.provider == VoiceProvider.AZURE:
            import azure.cognitiveservices.speech as speechsdk
            self.speech_config = speechsdk.SpeechConfig(
                subscription=os.environ.get("AZURE_SPEECH_KEY"),
                region=os.environ.get("AZURE_REGION")
            )
    
    def speak(self, text: str, blocking: bool = True):
        """Speak the given text"""
        if self.provider == VoiceProvider.NONE:
            return  # Silent mode
        
        # Clean the text (remove emoji, special chars)
        clean_text = self._clean_text(text)
        
        if self.provider == VoiceProvider.ELEVENLABS:
            self._speak_elevenlabs(clean_text, blocking)
        elif self.provider == VoiceProvider.GOOGLE:
            self._speak_google(clean_text, blocking)
        elif self.provider == VoiceProvider.AZURE:
            self._speak_azure(clean_text, blocking)
    
    def _clean_text(self, text: str) -> str:
        """Remove emojis and clean text for TTS"""
        # Remove 🎬 GOSLING: prefix
        text = text.replace("🎬 GOSLING:", "").strip()
        text = text.replace('"', '').strip()
        return text
    
    def _speak_elevenlabs(self, text: str, blocking: bool):
        from elevenlabs import generate, play
        audio = generate(
            text=text,
            voice="Adam",  # Gosling-esque
            model="eleven_monolingual_v1"
        )
        if blocking:
            play(audio)
        else:
            # Non-blocking playback
            import threading
            threading.Thread(target=play, args=(audio,)).start()
    
    def _speak_google(self, text: str, blocking: bool):
        # Implementation from above
        pass
    
    def _speak_azure(self, text: str, blocking: bool):
        # Implementation
        pass

# Usage:
# voice = WolfyVoice(VoiceProvider.ELEVENLABS)
# voice.speak(narration)
```

---

## 🎭 Modified run_wolfy_concert.py

Add at the top:
```python
from wolfy_voice import WolfyVoice, VoiceProvider

# In run_full_concert_experience():
def run_full_concert_experience(
    num_nodes: int = 17000,
    duration_seconds: float = 60.0,
    bpm: float = 120.0,
    enable_narration: bool = True,
    voice_enabled: bool = False,  # NEW!
    voice_provider: str = "elevenlabs"  # NEW!
):
    
    # Initialize voice if enabled
    voice = None
    if voice_enabled:
        provider = VoiceProvider[voice_provider.upper()]
        voice = WolfyVoice(provider)
    
    # Opening narration
    if enable_narration:
        print_section_header("🎬 OPENING NARRATION 🎬")
        opening = RyanGoslingNarrator.get_opening()
        print(opening)
        
        if voice:
            # Speak first paragraph only (full monologue is long)
            first_para = opening.split('\n\n')[1]  # Get first paragraph
            voice.speak(first_para)
    
    # During concert
    if enable_narration:
        narration = RyanGoslingNarrator.get_narration_at_beat(beat_num)
        if narration:
            print(narration)
            if voice:
                voice.speak(narration, blocking=False)  # Non-blocking!
```

---

## 📝 Environment Variables

Create `.env` file:
```bash
# ElevenLabs
ELEVENLABS_API_KEY=your_key_here

# Google Cloud
GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json

# Azure
AZURE_SPEECH_KEY=your_key_here
AZURE_REGION=eastus
```

Load with `python-dotenv`:
```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
load_dotenv()
```

---

## 🎵 Audio Output Options

### Pre-generate Audio Files
Generate all narration audio beforehand:

```python
def generate_narration_audio_library():
    """Pre-generate all narration as MP3 files"""
    voice = WolfyVoice(VoiceProvider.ELEVENLABS)
    
    # Opening
    voice.generate_to_file(
        RyanGoslingNarrator.get_opening(),
        "audio/opening.mp3"
    )
    
    # Each beat narration
    for narration in RyanGoslingNarrator.NARRATION_SCRIPT:
        filename = f"audio/beat_{narration['beat']}.mp3"
        voice.generate_to_file(narration['line'], filename)
    
    # Closing
    voice.generate_to_file(
        RyanGoslingNarrator.get_closing(),
        "audio/closing.mp3"
    )

# Then play pre-generated files during concert (faster, no API calls)
```

---

## 💰 Cost Considerations

**ElevenLabs:**
- Free tier: 10k characters/month
- Paid: $5/month for 30k characters
- Full script ~5k characters = 2 full runs on free tier

**Google Cloud TTS:**
- Free tier: 1M characters/month for WaveNet voices
- $0.000016 per character after that

**Azure:**
- Free tier: 500k characters/month
- Very generous for this use case

---

## 🎬 Production Ready Setup

```python
# Add to requirements.txt
elevenlabs>=0.2.0
python-dotenv>=1.0.0

# Optional providers:
# google-cloud-texttospeech>=2.14.0
# azure-cognitiveservices-speech>=1.31.0
# pygame>=2.5.0  # For audio playback
```

---

## 🐺 The Full Wolfy Voice Experience

Imagine this:

1. Run `python run_wolfy_concert.py`
2. Ryan Gosling's voice speaks the opening:
   > *"I used to think about connection differently..."*
3. Concert begins with visual simulation
4. At key beats, his voice narrates:
   > *"And then... the wolf arrives."*
5. Closing narration plays as visualizations generate

**That's the dream!** 🎤✨

---

## 🚀 Quick Start for Voice Integration

```bash
# Install
pip install elevenlabs python-dotenv

# Set API key
echo "ELEVENLABS_API_KEY=your_key" > .env

# Create wolfy_voice.py (code above)

# Modify run_wolfy_concert.py to use it

# Run!
python run_wolfy_concert.py --voice
```

---

## 🎯 Alternative: Voice Cloning

For the REAL Ryan Gosling experience:

1. **ElevenLabs Voice Cloning:**
   - Upload 1-2 minutes of Gosling audio
   - Create custom voice model
   - Use in your narration

2. **Legal Note:** 
   - For personal/educational use only
   - Don't distribute without rights
   - Consider it an homage! 🎬

---

## 💡 Pro Tips

1. **Pacing**: Set speaking rate to 0.85-0.9 for contemplative feel
2. **Pauses**: Insert `<break time="2s"/>` in SSML for dramatic pauses
3. **Emphasis**: Use `<emphasis level="moderate">the wolf arrives</emphasis>`
4. **Background Music**: Play Vangelis softly under narration

---

## 🎭 The Ultimate Experience

```python
# Full multimedia concert:
- 17,000 node simulation (Wolfy) ✅
- Real-time visualizations ✅
- Ryan Gosling voice narration (with ElevenLabs) 🎙️
- Background music (Vangelis/Prokofiev) 🎵
- Timed perfectly to beats 🎯

= ACTUAL IMMERSIVE EXPERIENCE 🤯
```

---

**Go forth and give Wolfy a voice!** 🐺🎤

*"This is the future, maybe. Or just a beautiful dream. Either way... I'm glad you're here for it."* 🎬

