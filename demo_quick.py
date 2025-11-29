#!/usr/bin/env python3
"""
Quick demo that generates all outputs without user interaction
Perfect for seeing Wolfy in action immediately!
"""

from wolfy_mesh_concert import WolfyOrchestrator
from wolfy_visualizer import WolfyVisualizer
from ryan_gosling_narration import RyanGoslingNarrator

print("=" * 80)
print("🐺" * 40)
print("=" * 80)
print(" " * 25 + "WOLFY QUICK DEMO")
print(" " * 15 + "Generating Concert Simulation & Visualizations")
print("=" * 80)
print("🐺" * 40)
print("=" * 80)
print()

# Show opening narration excerpt
print(RyanGoslingNarrator.NARRATION_SCRIPT[0]['line'])
print()

# Create and run a smaller concert for quick demo
print("🐺 Creating mesh network (1,000 nodes for quick demo)...")
wolfy = WolfyOrchestrator(num_nodes=1000, arena_size=(100, 100))

print("\n🎭 Running 20-second concert simulation...")
wolfy.simulate_concert(duration_seconds=20.0, bpm=140.0)

# Generate all visualizations
print("\n🎨 Generating visualizations...")
visualizer = WolfyVisualizer(wolfy)
visualizer.generate_all_visualizations()

# Export narration
print("\n🎬 Exporting narration script...")
RyanGoslingNarrator.export_full_script()

# Show closing narration excerpt
print("\n" + "=" * 80)
print(RyanGoslingNarrator.NARRATION_SCRIPT[-1]['line'])
print("=" * 80)

print("\n✨ DEMO COMPLETE! ✨")
print("\n📁 Generated files:")
print("   - wolfy_concert_log.json")
print("   - wolfy_network_snapshot.png")
print("   - wolfy_heatmap.png")
print("   - wolfy_gateway_network.png")
print("   - wolfy_stats_dashboard.png")
print("   - ryan_gosling_script.txt")
print("\n🐺 Open the PNG files to see the visualizations!")
print()

