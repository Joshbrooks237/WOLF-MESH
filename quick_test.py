#!/usr/bin/env python3
"""
Quick validation test to ensure all components work together
"""

import sys

print("🐺 WOLFY SYSTEM TEST 🐺\n")

# Test imports
print("Testing imports...")
try:
    from wolfy_mesh_concert import WolfyOrchestrator, MusicTheme, AudienceNode
    print("  ✓ wolfy_mesh_concert")
except ImportError as e:
    print(f"  ✗ wolfy_mesh_concert: {e}")
    sys.exit(1)

try:
    from wolfy_visualizer import WolfyVisualizer
    print("  ✓ wolfy_visualizer")
except ImportError as e:
    print(f"  ✗ wolfy_visualizer: {e}")
    sys.exit(1)

try:
    from ryan_gosling_narration import RyanGoslingNarrator
    print("  ✓ ryan_gosling_narration")
except ImportError as e:
    print(f"  ✗ ryan_gosling_narration: {e}")
    sys.exit(1)

print("\n✅ All imports successful!")

# Test basic functionality
print("\nTesting basic functionality...")

# Test node creation
print("  Creating test node...")
node = AudienceNode(id=0, position=(10.0, 20.0))
assert node.id == 0
assert node.position == (10.0, 20.0)
print("  ✓ Node creation works")

# Test narrator
print("  Testing narrator...")
opening = RyanGoslingNarrator.get_opening()
assert len(opening) > 0
assert "Wolfy" in opening or "mesh" in opening or "connection" in opening
print("  ✓ Narrator works")

# Test small orchestrator
print("  Creating mini orchestrator (100 nodes)...")
mini_wolfy = WolfyOrchestrator(num_nodes=100)
assert len(mini_wolfy.nodes) == 100
assert len(mini_wolfy.gateways) > 0
assert mini_wolfy.conductor_id is not None
print(f"  ✓ Orchestrator initialized ({len(mini_wolfy.gateways)} gateways)")

# Test beat synchronization
print("  Testing beat synchronization...")
participating = mini_wolfy.synchronize_beat(MusicTheme.BLADE_RUNNER)
assert len(participating) > 0
print(f"  ✓ Beat synchronized ({len(participating)} nodes participating)")

# Test statistics
print("  Testing statistics...")
stats = mini_wolfy.get_statistics()
assert stats['total_nodes'] == 100
assert 'active_nodes' in stats
print("  ✓ Statistics generation works")

print("\n🎉 ALL TESTS PASSED! 🎉")
print("\n✨ Wolfy is ready to rock! Run 'python run_wolfy_concert.py' to start the full experience.\n")

