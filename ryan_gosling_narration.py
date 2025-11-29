#!/usr/bin/env python3
"""
🎬 RYAN GOSLING NARRATION SCRIPT 🎬
The poetic, contemplative voice-over for Wolfy's mesh concert
Delivered with that characteristic Gosling gravitas
"""

from typing import List, Dict


class RyanGoslingNarrator:
    """
    Ryan Gosling's voice, in text form.
    Contemplative. Moody. Slightly cryptic.
    Perfect for a Blade Runner-inspired mesh network concert.
    """
    
    NARRATION_SCRIPT = [
        {
            "timestamp": "00:00",
            "beat": 0,
            "line": "I've seen things you people wouldn't believe... "
                    "Seventeen thousand phones, synchronized in the dark."
        },
        {
            "timestamp": "00:05",
            "beat": 10,
            "line": "Each one... a node. Each node... a voice. "
                    "Together, they become something more."
        },
        {
            "timestamp": "00:12",
            "beat": 24,
            "line": "The bird speaks first. High notes, dancing through the mesh. "
                    "Light. Almost innocent."
        },
        {
            "timestamp": "00:18",
            "beat": 32,
            "line": "Then the duck. Lower. Playful. "
                    "The network pulses with cyan and blue."
        },
        {
            "timestamp": "00:25",
            "beat": 40,
            "line": "There's a cat now. Prowling through the connections. "
                    "Purple lights flicker. Some nodes hesitate."
        },
        {
            "timestamp": "00:32",
            "beat": 48,
            "line": "And then... *pause* ...the wolf arrives."
        },
        {
            "timestamp": "00:38",
            "beat": 56,
            "line": "Deep tones. Red lights bleeding through the crowd. "
                    "This is what they came for."
        },
        {
            "timestamp": "00:45",
            "beat": 68,
            "line": "The hunters march. Orange strobes. "
                    "The mesh network becomes a living organism."
        },
        {
            "timestamp": "00:52",
            "beat": 80,
            "line": "We return to the beginning. The Vangelis melody. "
                    "Neon blue washing over everything."
        },
        {
            "timestamp": "00:58",
            "beat": 92,
            "line": "Seventeen thousand nodes. One consciousness. "
                    "This is what connection looks like."
        },
        {
            "timestamp": "01:00",
            "beat": 100,
            "line": "And then... silence. The lights fade. "
                    "But the network remembers."
        }
    ]
    
    OPENING_MONOLOGUE = """
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║                    🎬 RYAN GOSLING PRESENTS 🎬                    ║
║                                                                    ║
║                        "WOLFY'S MESH DREAM"                        ║
║                                                                    ║
║              A Story of Connection, Music, and Light               ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝

GOSLING:
    I used to think about connection differently.
    
    Before tonight, a concert was just... people in a room.
    Passive. Watching. Separate.
    
    But Wolfy showed me something else.
    
    Seventeen thousand phones. Not just recording.
    Not just consuming. *Creating*.
    
    Each one a node in a mesh network. Each one listening
    to its neighbors. Making decisions. Choosing when to shine,
    when to sing, when to fall silent.
    
    There's an AI at the heart of it all. Wolfy. The orchestrator.
    She doesn't control everything. She *guides*. She *suggests*.
    The network decides for itself.
    
    Leadership rotates. Power shifts. It's democratic in a way
    I never imagined a concert could be.
    
    We're going to play you some Vangelis. Some Prokofiev.
    We're going to paint the arena in light.
    
    And you're going to feel what it's like when seventeen thousand
    devices stop being separate... and start being one.
    
    This is the future, maybe. Or just a beautiful dream.
    Either way...
    
    *pause*
    
    ...I'm glad you're here for it.

    - RG
    
"""
    
    CLOSING_MONOLOGUE = """
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║                         FINAL THOUGHTS                             ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝

GOSLING:
    The concert's over now. The nodes are going dark.
    
    But something happened here tonight that can't unhappen.
    
    Seventeen thousand strangers... their devices found each other
    in the dark. They synchronized. They created something together
    without even trying.
    
    That's the thing about mesh networks. About true connection.
    You don't need a center. You don't need someone at the top
    telling everyone what to do.
    
    You just need... neighbors. Trust. A willingness to listen.
    
    Wolfy orchestrated it, sure. But the music? The light?
    The *feeling*?
    
    That was all of us.
    
    I'll remember the wolf's theme. The red lights, washing over
    thousands of phones held high. The way the network *pulsed*
    with something alive.
    
    Maybe you will too.
    
    *long pause*
    
    Or maybe this was all just a simulation. Code on a screen.
    Seventeen thousand imaginary nodes in a digital void.
    
    But it felt real to me.
    
    And isn't that what matters?
    
    Goodnight. Stay connected.
    
    - Ryan

"""
    
    SPONTANEOUS_OBSERVATIONS = [
        "The gateways are rotating now. Like watching consciousness shift.",
        "There's a latency to it all. A delay. But it's beautiful. Like ripples on water.",
        "Some nodes are brighter than others. More eager. I wonder what that says about us.",
        "The Blade Runner theme hits different when it's played by seventeen thousand phones.",
        "I can see the mesh connections. Cyan lines in the dark. A web of light.",
        "The cat's theme is purple. Of course it is. Cats are always purple in my mind.",
        "Battery levels are dropping. The network is tired. But it keeps going.",
        "There's a moment where everyone synchronizes perfectly. That's the moment we're chasing.",
        "The wolf theme makes the whole arena pulse red. It's like a heartbeat.",
        "This is what Vangelis imagined. A future where music and technology are the same thing.",
        "Peter and the Wolf, but make it cyberpunk. Prokofiev would be confused. Or thrilled.",
        "The strobe effects are optional. Consent-based lighting. Even in a simulation, we care.",
    ]
    
    @staticmethod
    def get_opening():
        """Get the opening monologue"""
        return RyanGoslingNarrator.OPENING_MONOLOGUE
    
    @staticmethod
    def get_closing():
        """Get the closing monologue"""
        return RyanGoslingNarrator.CLOSING_MONOLOGUE
    
    @staticmethod
    def get_narration_at_beat(beat: int) -> str:
        """Get narration line closest to a specific beat"""
        for narration in RyanGoslingNarrator.NARRATION_SCRIPT:
            if abs(narration["beat"] - beat) < 3:
                return f"\n🎬 GOSLING: \"{narration['line']}\"\n"
        return ""
    
    @staticmethod
    def get_random_observation() -> str:
        """Get a random Gosling observation"""
        import random
        return random.choice(RyanGoslingNarrator.SPONTANEOUS_OBSERVATIONS)
    
    @staticmethod
    def format_narration_card(text: str, width: int = 70) -> str:
        """Format a narration as a nice card"""
        lines = []
        words = text.split()
        current_line = ""
        
        for word in words:
            if len(current_line) + len(word) + 1 <= width - 4:
                current_line += word + " "
            else:
                lines.append(current_line.strip())
                current_line = word + " "
        
        if current_line:
            lines.append(current_line.strip())
        
        card = "╔" + "═" * (width - 2) + "╗\n"
        for line in lines:
            padding = width - len(line) - 4
            left_pad = padding // 2
            right_pad = padding - left_pad
            card += "║ " + " " * left_pad + line + " " * right_pad + " ║\n"
        card += "╚" + "═" * (width - 2) + "╝"
        
        return card
    
    @staticmethod
    def export_full_script(filename: str = "ryan_gosling_script.txt"):
        """Export the complete narration script"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write(" " * 20 + "WOLFY'S MESH CONCERT\n")
            f.write(" " * 15 + "Narration by Ryan Gosling\n")
            f.write("=" * 80 + "\n\n")
            
            f.write(RyanGoslingNarrator.OPENING_MONOLOGUE)
            f.write("\n\n")
            
            f.write("=" * 80 + "\n")
            f.write(" " * 25 + "BEAT-BY-BEAT NARRATION\n")
            f.write("=" * 80 + "\n\n")
            
            for narration in RyanGoslingNarrator.NARRATION_SCRIPT:
                f.write(f"[{narration['timestamp']}] Beat {narration['beat']}\n")
                f.write(f"GOSLING: {narration['line']}\n\n")
            
            f.write("=" * 80 + "\n")
            f.write(" " * 25 + "SPONTANEOUS OBSERVATIONS\n")
            f.write("=" * 80 + "\n\n")
            
            for i, obs in enumerate(RyanGoslingNarrator.SPONTANEOUS_OBSERVATIONS, 1):
                f.write(f"{i}. {obs}\n")
            
            f.write("\n\n")
            f.write(RyanGoslingNarrator.CLOSING_MONOLOGUE)
        
        print(f"🎬 Full Gosling script exported to {filename}")


if __name__ == "__main__":
    narrator = RyanGoslingNarrator()
    print(narrator.get_opening())
    print("\n" + "="*80 + "\n")
    print("Sample narration lines:")
    for narration in narrator.NARRATION_SCRIPT[:3]:
        print(f"\n{narrator.format_narration_card(narration['line'])}")
    print("\n" + "="*80 + "\n")
    print(narrator.get_closing())
    narrator.export_full_script()

