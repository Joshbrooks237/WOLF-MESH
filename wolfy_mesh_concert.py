#!/usr/bin/env python3
"""
🐺 WOLFY - The Mesh Network Concert Orchestrator 🐺
A cinematic simulation of 17,000 audience nodes creating a synchronized
audio-visual experience through mesh networking, AI, and pure Wolf-energy.
"""

import numpy as np
import random
import time
from dataclasses import dataclass, field
from typing import List, Set, Tuple, Dict, Optional
from enum import Enum
import json
from collections import defaultdict
import math


class NodeState(Enum):
    """States a node can be in during the concert"""
    IDLE = "idle"
    GATEWAY = "gateway"
    ACTIVE = "active"
    STROBING = "strobing"
    CONDUCTOR = "conductor"


class MusicTheme(Enum):
    """Musical themes for the concert"""
    BLADE_RUNNER = "blade_runner"
    PETER_WOLF_BIRD = "peter_wolf_bird"
    PETER_WOLF_DUCK = "peter_wolf_duck"
    PETER_WOLF_CAT = "peter_wolf_cat"
    PETER_WOLF_WOLF = "peter_wolf_wolf"
    PETER_WOLF_HUNTERS = "peter_wolf_hunters"


@dataclass
class LightPattern:
    """Represents a light pattern for a node"""
    color: Tuple[int, int, int]  # RGB
    intensity: float  # 0.0 to 1.0
    frequency: float  # Hz for flashing
    phase: float  # Phase offset in radians
    
    def get_brightness_at(self, time_ms: float) -> float:
        """Calculate brightness at given time"""
        if self.frequency == 0:
            return self.intensity
        return self.intensity * (0.5 + 0.5 * math.sin(2 * math.pi * self.frequency * time_ms / 1000.0 + self.phase))


@dataclass
class TonePattern:
    """Represents a sound tone for a node"""
    frequency: float  # Hz
    duration_ms: float
    volume: float  # 0.0 to 1.0
    waveform: str  # 'sine', 'square', 'triangle'


@dataclass
class AudienceNode:
    """Individual audience member's phone node"""
    id: int
    position: Tuple[float, float]  # x, y coordinates in meters
    state: NodeState = NodeState.IDLE
    battery: float = 1.0  # 0.0 to 1.0
    consent_strobe: bool = field(default_factory=lambda: random.random() > 0.3)
    
    # Networking
    neighbors: Set[int] = field(default_factory=set)
    signal_strength: Dict[int, float] = field(default_factory=dict)
    latency_ms: float = 5.0  # Base latency
    
    # Performance
    current_light: Optional[LightPattern] = None
    current_tone: Optional[TonePattern] = None
    participation_score: float = 0.0
    
    # AI decision making
    leadership_score: float = field(default_factory=lambda: random.random())
    gateway_fitness: float = 0.0
    
    def calculate_distance(self, other: 'AudienceNode') -> float:
        """Calculate distance to another node"""
        dx = self.position[0] - other.position[0]
        dy = self.position[1] - other.position[1]
        return math.sqrt(dx * dx + dy * dy)
    
    def update_gateway_fitness(self, all_nodes: List['AudienceNode']) -> None:
        """AI: Calculate fitness as a gateway node"""
        # Factors: centrality, battery, number of neighbors, current state
        centrality = len(self.neighbors) / 50.0  # Assume max ~50 neighbors
        battery_factor = self.battery
        state_penalty = 0.5 if self.state == NodeState.GATEWAY else 1.0
        
        self.gateway_fitness = (centrality * 0.4 + battery_factor * 0.3 + 
                               self.leadership_score * 0.3) * state_penalty
    
    def make_participation_decision(self, energy_level: float) -> bool:
        """AI: Decide whether to participate based on energy and personality"""
        threshold = 0.3 + (self.leadership_score * 0.4)
        return energy_level > threshold and self.battery > 0.1


class MusicEngine:
    """Generates musical patterns for different themes"""
    
    BLADE_RUNNER_MOTIF = [
        # Vangelis-inspired tones
        (440, 500, 0.6),  # A4
        (554, 500, 0.5),  # C#5
        (659, 500, 0.7),  # E5
        (523, 1000, 0.8), # C5
    ]
    
    PETER_AND_WOLF_THEMES = {
        MusicTheme.PETER_WOLF_BIRD: [(880, 200, 0.5), (988, 200, 0.5)],  # Flute - high, light
        MusicTheme.PETER_WOLF_DUCK: [(349, 400, 0.6), (392, 400, 0.6)],  # Oboe - middle
        MusicTheme.PETER_WOLF_CAT: [(262, 300, 0.5), (294, 300, 0.5)],  # Clarinet - sneaky
        MusicTheme.PETER_WOLF_WOLF: [(196, 600, 0.8), (220, 600, 0.8)],  # French horns - ominous
        MusicTheme.PETER_WOLF_HUNTERS: [(147, 500, 0.7), (165, 500, 0.7)],  # Drums - march
    }
    
    @staticmethod
    def get_tone_for_theme(theme: MusicTheme, beat_index: int) -> TonePattern:
        """Get the appropriate tone for a theme at a given beat"""
        if theme == MusicTheme.BLADE_RUNNER:
            pattern = MusicEngine.BLADE_RUNNER_MOTIF
        else:
            pattern = MusicEngine.PETER_AND_WOLF_THEMES.get(theme, [(440, 500, 0.5)])
        
        freq, dur, vol = pattern[beat_index % len(pattern)]
        return TonePattern(frequency=freq, duration_ms=dur, volume=vol, waveform='sine')
    
    @staticmethod
    def get_light_for_theme(theme: MusicTheme, node_id: int, phase_offset: float) -> LightPattern:
        """Get the appropriate light pattern for a theme"""
        theme_colors = {
            MusicTheme.BLADE_RUNNER: (0, 150, 255),  # Neon blue
            MusicTheme.PETER_WOLF_BIRD: (255, 255, 100),  # Bright yellow
            MusicTheme.PETER_WOLF_DUCK: (100, 200, 255),  # Duck blue
            MusicTheme.PETER_WOLF_CAT: (200, 100, 255),  # Purple
            MusicTheme.PETER_WOLF_WOLF: (255, 50, 50),  # Red
            MusicTheme.PETER_WOLF_HUNTERS: (255, 150, 0),  # Orange
        }
        
        color = theme_colors.get(theme, (255, 255, 255))
        frequency = 2.0 if theme == MusicTheme.BLADE_RUNNER else 1.5
        
        return LightPattern(
            color=color,
            intensity=0.8,
            frequency=frequency,
            phase=phase_offset
        )


class WolfyOrchestrator:
    """🐺 The main AI orchestrator - Wolfy herself 🐺"""
    
    def __init__(self, num_nodes: int = 17000, arena_size: Tuple[float, float] = (200, 200)):
        self.num_nodes = num_nodes
        self.arena_size = arena_size
        self.nodes: List[AudienceNode] = []
        self.gateways: Set[int] = set()
        self.conductor_id: Optional[int] = None
        self.current_theme = MusicTheme.BLADE_RUNNER
        self.beat_count = 0
        self.simulation_time_ms = 0.0
        self.event_log: List[Dict] = []
        self.participation_history: List[Dict[int, float]] = []
        
        print("🐺 Wolfy awakening... Creating mesh network...")
        self._initialize_nodes()
        self._build_mesh_network()
        self._select_initial_gateways()
        
    def _initialize_nodes(self):
        """Create all audience nodes with realistic spatial distribution"""
        print(f"   Spawning {self.num_nodes} audience nodes...")
        
        # Create clusters (sections of the venue)
        num_clusters = 20
        cluster_centers = [
            (random.uniform(10, self.arena_size[0] - 10),
             random.uniform(10, self.arena_size[1] - 10))
            for _ in range(num_clusters)
        ]
        
        for i in range(self.num_nodes):
            # Assign to a cluster with some randomness
            cluster = random.choice(cluster_centers)
            x = cluster[0] + random.gauss(0, 15)
            y = cluster[1] + random.gauss(0, 15)
            
            # Keep within arena bounds
            x = max(0, min(self.arena_size[0], x))
            y = max(0, min(self.arena_size[1], y))
            
            node = AudienceNode(id=i, position=(x, y))
            self.nodes.append(node)
    
    def _build_mesh_network(self):
        """Connect nearby nodes in a mesh network"""
        print("   Building mesh connections...")
        max_connection_distance = 8.0  # meters (Bluetooth/WiFi range in crowd)
        
        # For efficiency with 17k nodes, use spatial hashing
        grid_size = 10.0
        spatial_grid = defaultdict(list)
        
        for node in self.nodes:
            grid_x = int(node.position[0] / grid_size)
            grid_y = int(node.position[1] / grid_size)
            spatial_grid[(grid_x, grid_y)].append(node)
        
        # Connect nodes within range
        for node in self.nodes:
            grid_x = int(node.position[0] / grid_size)
            grid_y = int(node.position[1] / grid_size)
            
            # Check neighboring grid cells
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    cell = (grid_x + dx, grid_y + dy)
                    for other in spatial_grid[cell]:
                        if node.id >= other.id:
                            continue
                        
                        distance = node.calculate_distance(other)
                        if distance <= max_connection_distance:
                            # Create bidirectional connection
                            signal_strength = 1.0 - (distance / max_connection_distance)
                            node.neighbors.add(other.id)
                            other.neighbors.add(node.id)
                            node.signal_strength[other.id] = signal_strength
                            other.signal_strength[node.id] = signal_strength
        
        avg_neighbors = sum(len(n.neighbors) for n in self.nodes) / len(self.nodes)
        print(f"   ✓ Mesh built: avg {avg_neighbors:.1f} neighbors per node")
    
    def _select_initial_gateways(self, num_gateways: int = 25):
        """AI: Select initial gateway nodes for network coordination"""
        print("   AI selecting gateway nodes...")
        
        for node in self.nodes:
            node.update_gateway_fitness(self.nodes)
        
        # Select top fitness nodes as gateways
        sorted_nodes = sorted(self.nodes, key=lambda n: n.gateway_fitness, reverse=True)
        self.gateways = {n.id for n in sorted_nodes[:num_gateways]}
        
        for gw_id in self.gateways:
            self.nodes[gw_id].state = NodeState.GATEWAY
        
        # Select one gateway as conductor
        self.conductor_id = sorted_nodes[0].id
        self.nodes[self.conductor_id].state = NodeState.CONDUCTOR
        
        print(f"   ✓ {len(self.gateways)} gateways selected, node {self.conductor_id} conducting")
        self._log_event("initialization", "Mesh network initialized", {
            "gateways": list(self.gateways),
            "conductor": self.conductor_id
        })
    
    def _log_event(self, event_type: str, message: str, data: Dict = None):
        """Log an event to the simulation log"""
        self.event_log.append({
            "time_ms": self.simulation_time_ms,
            "beat": self.beat_count,
            "type": event_type,
            "message": message,
            "data": data or {}
        })
    
    def rotate_leadership(self):
        """AI: Rotate gateway and conductor roles to balance load"""
        # Update fitness scores
        for node in self.nodes:
            node.update_gateway_fitness(self.nodes)
            # Penalize current gateways to encourage rotation
            if node.state == NodeState.GATEWAY:
                node.gateway_fitness *= 0.7
        
        # Select new gateways
        sorted_nodes = sorted(self.nodes, key=lambda n: n.gateway_fitness, reverse=True)
        new_gateways = {n.id for n in sorted_nodes[:25]}
        
        # Reset old gateways
        for old_gw in self.gateways:
            if old_gw not in new_gateways:
                self.nodes[old_gw].state = NodeState.IDLE
        
        # Set new gateways
        self.gateways = new_gateways
        for gw_id in self.gateways:
            self.nodes[gw_id].state = NodeState.GATEWAY
        
        # New conductor
        old_conductor = self.conductor_id
        self.conductor_id = sorted_nodes[0].id
        self.nodes[self.conductor_id].state = NodeState.CONDUCTOR
        
        self._log_event("leadership_rotation", 
                       f"Conductor passed from {old_conductor} to {self.conductor_id}",
                       {"new_gateways": list(self.gateways)})
    
    def synchronize_beat(self, theme: MusicTheme):
        """Synchronize a musical beat across the mesh network"""
        self.current_theme = theme
        self.beat_count += 1
        
        # Calculate which nodes participate this beat
        # Start from conductor, propagate through gateways to neighbors
        participating_nodes = set()
        participation_wave = [self.conductor_id]
        visited = {self.conductor_id}
        
        # Simulate wave propagation with latency
        wave_depth = 0
        max_depth = 10  # Limit propagation depth per beat
        
        while participation_wave and wave_depth < max_depth:
            next_wave = []
            
            for node_id in participation_wave:
                node = self.nodes[node_id]
                
                # AI decision: should this node participate?
                energy_level = 0.7 + 0.3 * math.sin(self.simulation_time_ms / 2000.0)
                if node.make_participation_decision(energy_level):
                    participating_nodes.add(node_id)
                    node.participation_score += 1.0
                    
                    # Set light and tone
                    phase_offset = wave_depth * 0.2  # Phase offset based on distance from conductor
                    node.current_light = MusicEngine.get_light_for_theme(theme, node_id, phase_offset)
                    node.current_tone = MusicEngine.get_tone_for_theme(theme, self.beat_count)
                    
                    # Propagate to neighbors
                    for neighbor_id in node.neighbors:
                        if neighbor_id not in visited:
                            # Consider signal strength for propagation
                            if node.signal_strength.get(neighbor_id, 0) > 0.3:
                                next_wave.append(neighbor_id)
                                visited.add(neighbor_id)
                    
                    # Battery drain
                    node.battery -= 0.0001
            
            participation_wave = next_wave
            wave_depth += 1
        
        # Record participation for heatmap
        participation_snapshot = {node_id: self.nodes[node_id].participation_score 
                                 for node_id in participating_nodes}
        self.participation_history.append(participation_snapshot)
        
        self._log_event("beat", f"{theme.value} beat #{self.beat_count}", {
            "participating_nodes": len(participating_nodes),
            "wave_depth": wave_depth,
            "theme": theme.value
        })
        
        return participating_nodes
    
    def simulate_concert(self, duration_seconds: float = 60.0, bpm: float = 120.0):
        """Run the full concert simulation"""
        beat_interval_ms = (60.0 / bpm) * 1000.0
        total_beats = int((duration_seconds * 1000.0) / beat_interval_ms)
        
        print(f"\n🎭 CONCERT BEGINNING 🎭")
        print(f"   Duration: {duration_seconds}s at {bpm} BPM = {total_beats} beats")
        print(f"   Themes: Blade Runner → Peter and the Wolf\n")
        
        self._log_event("concert_start", "🐺 Wolfy's mesh concert begins!", {
            "duration_s": duration_seconds,
            "bpm": bpm
        })
        
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
        
        # Pad or trim to match total beats
        while len(theme_schedule) < total_beats:
            theme_schedule.append(MusicTheme.BLADE_RUNNER)
        theme_schedule = theme_schedule[:total_beats]
        
        for beat_num in range(total_beats):
            self.simulation_time_ms = beat_num * beat_interval_ms
            current_theme = theme_schedule[beat_num]
            
            # Synchronize beat
            participating = self.synchronize_beat(current_theme)
            
            # Periodic leadership rotation
            if beat_num % 16 == 0 and beat_num > 0:
                self.rotate_leadership()
            
            # Progress indicator
            if beat_num % 10 == 0:
                progress = (beat_num / total_beats) * 100
                print(f"   🎵 Beat {beat_num}/{total_beats} ({progress:.1f}%) - "
                      f"{current_theme.value} - {len(participating)} nodes active")
        
        self._log_event("concert_end", "🐺 Concert complete! What a show!", {
            "total_beats": total_beats,
            "final_participation": len(self.participation_history[-1]) if self.participation_history else 0
        })
        
        print(f"\n✨ CONCERT COMPLETE ✨\n")
    
    def get_statistics(self) -> Dict:
        """Get concert statistics"""
        total_participation = sum(n.participation_score for n in self.nodes)
        active_nodes = sum(1 for n in self.nodes if n.participation_score > 0)
        avg_participation = total_participation / active_nodes if active_nodes > 0 else 0
        
        return {
            "total_nodes": self.num_nodes,
            "active_nodes": active_nodes,
            "participation_rate": active_nodes / self.num_nodes,
            "avg_participation_score": avg_participation,
            "total_events": len(self.event_log),
            "beats_performed": self.beat_count,
            "gateways": list(self.gateways),
            "conductor": self.conductor_id
        }
    
    def export_event_log(self, filename: str = "wolfy_concert_log.json"):
        """Export the event log to a file"""
        with open(filename, 'w') as f:
            json.dump({
                "statistics": self.get_statistics(),
                "events": self.event_log
            }, f, indent=2)
        print(f"📝 Event log exported to {filename}")


if __name__ == "__main__":
    print("=" * 70)
    print("🐺" * 35)
    print("=" * 70)
    print(" " * 20 + "WOLFY MESH CONCERT")
    print(" " * 15 + "A Digital Orchestra Experience")
    print("=" * 70)
    print("🐺" * 35)
    print("=" * 70)
    print()
    
    # Create and run the concert
    wolfy = WolfyOrchestrator(num_nodes=17000)
    wolfy.simulate_concert(duration_seconds=60.0, bpm=120.0)
    
    # Show statistics
    stats = wolfy.get_statistics()
    print("\n📊 CONCERT STATISTICS 📊")
    print(f"   Total Nodes: {stats['total_nodes']:,}")
    print(f"   Active Participants: {stats['active_nodes']:,} ({stats['participation_rate']*100:.1f}%)")
    print(f"   Average Participation Score: {stats['avg_participation_score']:.2f}")
    print(f"   Total Beats: {stats['beats_performed']}")
    print(f"   Events Logged: {stats['total_events']}")
    
    # Export log
    wolfy.export_event_log()

