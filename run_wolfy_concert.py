#!/usr/bin/env python3
"""
🐺 WOLFY'S MESH CONCERT - MAIN RUNNER 🐺
The complete experience: simulation + visualization + narration
"""

import sys
import time
from wolfy_mesh_concert import WolfyOrchestrator, MusicTheme
from wolfy_visualizer import WolfyVisualizer
from ryan_gosling_narration import RyanGoslingNarrator


def print_banner():
    """Print the epic opening banner"""
    banner = """
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║  ██╗    ██╗ ██████╗ ██╗     ███████╗██╗   ██╗███████╗                  ║
║  ██║    ██║██╔═══██╗██║     ██╔════╝╚██╗ ██╔╝██╔════╝                  ║
║  ██║ █╗ ██║██║   ██║██║     █████╗   ╚████╔╝ ███████╗                  ║
║  ██║███╗██║██║   ██║██║     ██╔══╝    ╚██╔╝  ╚════██║                  ║
║  ╚███╔███╔╝╚██████╔╝███████╗██║        ██║   ███████║                  ║
║   ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝        ╚═╝   ╚══════╝                  ║
║                                                                          ║
║                      MESH NETWORK CONCERT SIMULATOR                      ║
║                                                                          ║
║                  🎵 Blade Runner × Peter and the Wolf 🎵                ║
║                                                                          ║
║                        Narrated by Ryan Gosling                          ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_section_header(title: str):
    """Print a fancy section header"""
    width = 80
    print("\n" + "═" * width)
    print(" " * ((width - len(title)) // 2) + title)
    print("═" * width + "\n")


def run_full_concert_experience(
    num_nodes: int = 17000,
    duration_seconds: float = 60.0,
    bpm: float = 120.0,
    enable_narration: bool = True
):
    """
    Run the complete Wolfy concert experience:
    1. Opening narration
    2. Mesh network simulation
    3. Inline narration during concert
    4. Visualization generation
    5. Closing narration
    """
    
    print_banner()
    
    # Opening narration
    if enable_narration:
        print_section_header("🎬 OPENING NARRATION 🎬")
        print(RyanGoslingNarrator.get_opening())
        print("\n" + "─" * 80)
        input("\n⏸️  Press ENTER to begin the concert...\n")
    
    # Initialize Wolfy
    print_section_header("🐺 WOLFY INITIALIZATION 🐺")
    wolfy = WolfyOrchestrator(num_nodes=num_nodes)
    
    # Run the concert with live narration
    print_section_header("🎭 CONCERT IN PROGRESS 🎭")
    
    if enable_narration:
        print("🎬 Narration will appear during key moments...\n")
    
    # Calculate beat interval
    beat_interval_ms = (60.0 / bpm) * 1000.0
    total_beats = int((duration_seconds * 1000.0) / beat_interval_ms)
    
    # Musical structure
    themes = [
        (MusicTheme.BLADE_RUNNER, 16),
        (MusicTheme.PETER_WOLF_BIRD, 8),
        (MusicTheme.PETER_WOLF_DUCK, 8),
        (MusicTheme.BLADE_RUNNER, 8),
        (MusicTheme.PETER_WOLF_CAT, 8),
        (MusicTheme.PETER_WOLF_WOLF, 12),
        (MusicTheme.BLADE_RUNNER, 8),
        (MusicTheme.PETER_WOLF_HUNTERS, 8),
        (MusicTheme.BLADE_RUNNER, 16),
    ]
    
    theme_schedule = []
    for theme, beats in themes:
        theme_schedule.extend([theme] * beats)
    
    while len(theme_schedule) < total_beats:
        theme_schedule.append(MusicTheme.BLADE_RUNNER)
    theme_schedule = theme_schedule[:total_beats]
    
    # Run simulation with narration
    wolfy._log_event("concert_start", "🐺 Wolfy's mesh concert begins!", {
        "duration_s": duration_seconds,
        "bpm": bpm
    })
    
    last_theme = None
    for beat_num in range(total_beats):
        wolfy.simulation_time_ms = beat_num * beat_interval_ms
        current_theme = theme_schedule[beat_num]
        
        # Announce theme changes
        if current_theme != last_theme:
            theme_name = current_theme.value.replace('_', ' ').title()
            print(f"\n🎵 Theme Change → {theme_name}")
        last_theme = current_theme
        
        # Synchronize beat
        participating = wolfy.synchronize_beat(current_theme)
        
        # Periodic leadership rotation
        if beat_num % 16 == 0 and beat_num > 0:
            wolfy.rotate_leadership()
        
        # Ryan Gosling narration at key moments
        if enable_narration:
            narration = RyanGoslingNarrator.get_narration_at_beat(beat_num)
            if narration:
                print(narration)
        
        # Progress indicator
        if beat_num % 10 == 0:
            progress = (beat_num / total_beats) * 100
            print(f"   🎵 Beat {beat_num}/{total_beats} ({progress:.1f}%) - "
                  f"{len(participating)} nodes active")
    
    wolfy._log_event("concert_end", "🐺 Concert complete! What a show!", {
        "total_beats": total_beats,
        "final_participation": len(wolfy.participation_history[-1]) if wolfy.participation_history else 0
    })
    
    print(f"\n✨ CONCERT COMPLETE ✨\n")
    
    # Statistics
    print_section_header("📊 CONCERT STATISTICS 📊")
    stats = wolfy.get_statistics()
    print(f"   Total Nodes: {stats['total_nodes']:,}")
    print(f"   Active Participants: {stats['active_nodes']:,} ({stats['participation_rate']*100:.1f}%)")
    print(f"   Average Participation Score: {stats['avg_participation_score']:.2f}")
    print(f"   Total Beats: {stats['beats_performed']}")
    print(f"   Events Logged: {stats['total_events']}")
    print(f"   Final Conductor: Node #{stats['conductor']}")
    print(f"   Gateway Count: {len(stats['gateways'])}")
    
    # Export event log
    print_section_header("💾 EXPORTING DATA 💾")
    wolfy.export_event_log()
    
    # Generate visualizations
    print_section_header("🎨 GENERATING VISUALIZATIONS 🎨")
    visualizer = WolfyVisualizer(wolfy)
    visualizer.generate_all_visualizations()
    
    # Export narration script
    RyanGoslingNarrator.export_full_script()
    
    # Closing narration
    if enable_narration:
        print_section_header("🎬 CLOSING NARRATION 🎬")
        print(RyanGoslingNarrator.get_closing())
    
    # Final suggestions
    print_section_header("💡 ENHANCEMENT SUGGESTIONS 💡")
    print_enhancements()
    
    print_section_header("🐺 WOLFY SAYS GOODBYE 🐺")
    print("""
    Thank you for experiencing the Wolfy Mesh Concert!
    
    The simulation is complete, but the possibilities are endless:
    - Scale to millions of nodes
    - Add real audio synthesis
    - Implement actual mesh networking protocols
    - Create AR/VR visualization overlays
    - Deploy to real concert venues
    
    Until next time... stay connected. 🐺
    
    - Wolfy
    """)
    
    return wolfy, visualizer


def print_enhancements():
    """Print suggested enhancements for the system"""
    enhancements = """
    🎨 AESTHETIC ENHANCEMENTS:
    ═══════════════════════════════════════════════
    
    1. 🌈 Dynamic Color Palettes
       - Transition through color gradients based on musical intensity
       - Use HSV color space for smooth transitions
       - Add "golden hour" and "midnight" lighting modes
    
    2. ✨ Advanced Strobe Patterns
       - Morse code messages in light flashes
       - QR code formation using node arrays
       - Wave interference patterns across the arena
    
    3. 🎭 Theatrical Lighting Zones
       - Spotlight effects on gateway nodes
       - Dimming sections to create depth
       - "Firefly" random sparkle effects during quiet moments
    
    4. 🔊 Spatial Audio Simulation
       - Pan tones based on node position
       - Doppler effects for moving patterns
       - Reverb simulation for venue acoustics
    
    ⚙️ TECHNICAL ENHANCEMENTS:
    ═══════════════════════════════════════════════
    
    5. 🌐 Real Protocol Integration
       - Implement actual Bluetooth Mesh
       - Add WiFi Direct support
       - Include LoRa for long-range nodes
    
    6. 🤖 Advanced AI Features
       - Genetic algorithms for optimal gateway placement
       - Predictive routing for latency reduction
       - Sentiment analysis of participation enthusiasm
    
    7. 📊 Real-time Analytics
       - Live dashboard with WebSocket updates
       - Network health monitoring
       - Predictive battery management
    
    8. 🎮 Interactive Elements
       - Allow audience voting on next theme
       - Enable individual node customization
       - Create "dueling sections" with different patterns
    
    🚀 DEPLOYMENT IDEAS:
    ═══════════════════════════════════════════════
    
    9. 📱 Mobile App
       - iOS/Android apps to become actual nodes
       - AR overlay showing mesh connections
       - Haptic feedback synced to music
    
    10. 🎪 Live Events
        - Deploy at actual concerts/festivals
        - Sports stadium integration
        - New Year's Eve countdown coordination
    
    11. 🏙️ Urban Installation
        - City-wide mesh network art
        - Building facade lighting control
        - Interactive public spaces
    
    12. 🎓 Educational Tool
        - Teach networking concepts
        - Demonstrate distributed systems
        - Show AI decision-making in action
    """
    
    print(enhancements)


def quick_demo():
    """Run a quick demo with smaller parameters"""
    print("🐺 Running QUICK DEMO mode (fewer nodes, shorter duration)\n")
    return run_full_concert_experience(
        num_nodes=5000,  # Smaller for faster execution
        duration_seconds=30.0,
        bpm=140.0,
        enable_narration=True
    )


def full_experience():
    """Run the complete 17k node experience"""
    print("🐺 Running FULL EXPERIENCE mode (17,000 nodes, full duration)\n")
    return run_full_concert_experience(
        num_nodes=17000,
        duration_seconds=60.0,
        bpm=120.0,
        enable_narration=True
    )


def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == "--quick":
        quick_demo()
    elif len(sys.argv) > 1 and sys.argv[1] == "--no-narration":
        run_full_concert_experience(enable_narration=False)
    else:
        # Interactive mode
        print_banner()
        print("\n🐺 Welcome to Wolfy's Mesh Concert! 🐺\n")
        print("Choose your experience:")
        print("  1. Full Experience (17,000 nodes, 60 seconds, narration)")
        print("  2. Quick Demo (5,000 nodes, 30 seconds, narration)")
        print("  3. Custom settings")
        print("  4. Export narration script only")
        print()
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            full_experience()
        elif choice == "2":
            quick_demo()
        elif choice == "3":
            try:
                nodes = int(input("Number of nodes (1000-50000): ").strip())
                duration = float(input("Duration in seconds (10-300): ").strip())
                bpm = float(input("BPM (60-180): ").strip())
                narration = input("Enable narration? (y/n): ").strip().lower() == 'y'
                
                run_full_concert_experience(
                    num_nodes=nodes,
                    duration_seconds=duration,
                    bpm=bpm,
                    enable_narration=narration
                )
            except ValueError:
                print("Invalid input. Running default experience.")
                full_experience()
        elif choice == "4":
            print_section_header("🎬 EXPORTING NARRATION SCRIPT 🎬")
            RyanGoslingNarrator.export_full_script()
            print("\n✅ Script exported! Check ryan_gosling_script.txt\n")
        else:
            print("Invalid choice. Running full experience.")
            full_experience()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🐺 Concert interrupted. Wolfy is sad but understanding. 🐺\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nWolfy encountered an unexpected problem. Check your Python environment.")
        sys.exit(1)

