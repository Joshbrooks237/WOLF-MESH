#!/usr/bin/env python3
"""
🎨 WOLFY VISUALIZER 🎨
Creates beautiful visual diagrams of the mesh network concert
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np
from typing import List, Dict, Tuple
import json


class WolfyVisualizer:
    """Creates stunning visualizations of the mesh concert"""
    
    def __init__(self, wolfy_orchestrator):
        self.wolfy = wolfy_orchestrator
        self.fig = None
        self.axes = None
        
    def create_network_snapshot(self, filename: str = "wolfy_network_snapshot.png", 
                               sample_size: int = 500):
        """Create a static snapshot of the mesh network"""
        print(f"🎨 Creating network visualization (sampling {sample_size} nodes for clarity)...")
        
        # Sample nodes for visualization (17k is too many to see clearly)
        sampled_indices = np.random.choice(len(self.wolfy.nodes), 
                                          min(sample_size, len(self.wolfy.nodes)), 
                                          replace=False)
        sampled_nodes = [self.wolfy.nodes[i] for i in sampled_indices]
        sampled_ids = {n.id for n in sampled_nodes}
        
        fig, ax = plt.subplots(figsize=(16, 12))
        fig.patch.set_facecolor('#0a0a0a')
        ax.set_facecolor('#0a0a0a')
        
        # Draw connections first (so they're behind nodes)
        print("   Drawing connections...")
        for node in sampled_nodes:
            for neighbor_id in node.neighbors:
                if neighbor_id in sampled_ids:
                    neighbor = self.wolfy.nodes[neighbor_id]
                    signal_strength = node.signal_strength.get(neighbor_id, 0.5)
                    ax.plot([node.position[0], neighbor.position[0]],
                           [node.position[1], neighbor.position[1]],
                           color='cyan', alpha=signal_strength * 0.15, 
                           linewidth=0.3, zorder=1)
        
        # Draw nodes
        print("   Drawing nodes...")
        for node in sampled_nodes:
            # Color based on state and participation
            if node.state.value == "conductor":
                color = '#FFD700'  # Gold
                size = 120
                marker = '*'
            elif node.state.value == "gateway":
                color = '#FF6B6B'  # Red
                size = 60
                marker = 'o'
            else:
                # Color based on participation
                participation_normalized = min(node.participation_score / 20.0, 1.0)
                color = plt.cm.plasma(participation_normalized)
                size = 20 + participation_normalized * 30
                marker = 'o'
            
            # Light effect
            if node.current_light:
                brightness = node.current_light.intensity
                r, g, b = node.current_light.color
                color = (r/255.0 * brightness, g/255.0 * brightness, b/255.0 * brightness)
            
            ax.scatter(node.position[0], node.position[1], 
                      c=[color], s=size, marker=marker, 
                      edgecolors='white', linewidths=0.5,
                      alpha=0.8, zorder=2)
        
        # Add title and labels
        ax.set_xlim(-5, self.wolfy.arena_size[0] + 5)
        ax.set_ylim(-5, self.wolfy.arena_size[1] + 5)
        ax.set_aspect('equal')
        ax.set_xlabel('X Position (meters)', color='white', fontsize=12)
        ax.set_ylabel('Y Position (meters)', color='white', fontsize=12)
        ax.tick_params(colors='white')
        
        # Title with Wolf energy
        title = f"🐺 WOLFY'S MESH CONCERT 🐺\n"
        title += f"Network Snapshot: {len(sampled_nodes)} of {len(self.wolfy.nodes):,} nodes\n"
        title += f"Theme: {self.wolfy.current_theme.value} | Beat: {self.wolfy.beat_count}"
        ax.set_title(title, color='white', fontsize=16, fontweight='bold', pad=20)
        
        # Legend
        from matplotlib.lines import Line2D
        legend_elements = [
            Line2D([0], [0], marker='*', color='w', markerfacecolor='#FFD700', 
                   markersize=15, label='Conductor', linestyle='None'),
            Line2D([0], [0], marker='o', color='w', markerfacecolor='#FF6B6B', 
                   markersize=10, label='Gateway', linestyle='None'),
            Line2D([0], [0], marker='o', color='w', markerfacecolor='#BC13FE', 
                   markersize=8, label='Active Node', linestyle='None'),
            Line2D([0], [0], color='cyan', alpha=0.3, linewidth=2, label='Mesh Connection')
        ]
        ax.legend(handles=legend_elements, loc='upper right', 
                 facecolor='#1a1a1a', edgecolor='white', 
                 labelcolor='white', fontsize=10)
        
        plt.tight_layout()
        plt.savefig(filename, dpi=150, facecolor='#0a0a0a')
        print(f"   ✓ Network snapshot saved to {filename}")
        plt.close()
    
    def create_participation_heatmap(self, filename: str = "wolfy_heatmap.png"):
        """Create a heatmap showing node participation over time"""
        print("🔥 Creating participation heatmap...")
        
        if not self.wolfy.participation_history:
            print("   ⚠️  No participation history to visualize")
            return
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
        fig.patch.set_facecolor('#0a0a0a')
        
        # LEFT PLOT: Spatial heatmap
        ax1.set_facecolor('#0a0a0a')
        
        # Create 2D histogram of participation
        x_coords = [n.position[0] for n in self.wolfy.nodes]
        y_coords = [n.position[1] for n in self.wolfy.nodes]
        participation = [n.participation_score for n in self.wolfy.nodes]
        
        # Create heatmap
        heatmap, xedges, yedges = np.histogram2d(
            x_coords, y_coords, bins=50, 
            weights=participation
        )
        
        extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
        im1 = ax1.imshow(heatmap.T, extent=extent, origin='lower', 
                        cmap='hot', aspect='auto', interpolation='bilinear')
        
        ax1.set_xlabel('X Position (meters)', color='white', fontsize=12)
        ax1.set_ylabel('Y Position (meters)', color='white', fontsize=12)
        ax1.set_title('🔥 Spatial Participation Heatmap 🔥', 
                     color='white', fontsize=14, fontweight='bold')
        ax1.tick_params(colors='white')
        
        cbar1 = plt.colorbar(im1, ax=ax1)
        cbar1.set_label('Total Participation', color='white', fontsize=10)
        cbar1.ax.yaxis.set_tick_params(color='white')
        plt.setp(plt.getp(cbar1.ax.axes, 'yticklabels'), color='white')
        
        # RIGHT PLOT: Temporal participation
        ax2.set_facecolor('#0a0a0a')
        
        # Calculate participation over time
        time_points = list(range(len(self.wolfy.participation_history)))
        active_counts = [len(snapshot) for snapshot in self.wolfy.participation_history]
        
        ax2.fill_between(time_points, active_counts, alpha=0.6, color='#FF6B6B')
        ax2.plot(time_points, active_counts, color='#FFD700', linewidth=2)
        
        ax2.set_xlabel('Beat Number', color='white', fontsize=12)
        ax2.set_ylabel('Active Nodes', color='white', fontsize=12)
        ax2.set_title('⚡ Participation Over Time ⚡', 
                     color='white', fontsize=14, fontweight='bold')
        ax2.tick_params(colors='white')
        ax2.grid(True, alpha=0.2, color='white')
        
        # Add theme markers (approximate)
        theme_changes = [0, 16, 24, 32, 40, 48, 60, 68, 76]
        theme_names = ['BR', 'Bird', 'Duck', 'BR', 'Cat', 'Wolf', 'BR', 'Hunt', 'BR']
        for i, (beat, name) in enumerate(zip(theme_changes, theme_names)):
            if beat < len(time_points):
                ax2.axvline(x=beat, color='cyan', alpha=0.3, linestyle='--', linewidth=1)
                ax2.text(beat, max(active_counts) * 0.95, name, 
                        color='cyan', fontsize=8, rotation=90, va='top')
        
        plt.tight_layout()
        plt.savefig(filename, dpi=150, facecolor='#0a0a0a')
        print(f"   ✓ Heatmap saved to {filename}")
        plt.close()
    
    def create_gateway_network_diagram(self, filename: str = "wolfy_gateway_network.png"):
        """Visualize the gateway network topology"""
        print("🌐 Creating gateway network diagram...")
        
        fig, ax = plt.subplots(figsize=(14, 10))
        fig.patch.set_facecolor('#0a0a0a')
        ax.set_facecolor('#0a0a0a')
        
        # Get gateway nodes
        gateway_nodes = [self.wolfy.nodes[gw_id] for gw_id in self.wolfy.gateways]
        
        # Draw all nodes as small dots
        all_x = [n.position[0] for n in self.wolfy.nodes]
        all_y = [n.position[1] for n in self.wolfy.nodes]
        ax.scatter(all_x, all_y, c='white', s=1, alpha=0.1, zorder=1)
        
        # Draw gateway connections
        for i, gw1 in enumerate(gateway_nodes):
            for gw2 in gateway_nodes[i+1:]:
                if gw2.id in gw1.neighbors:
                    ax.plot([gw1.position[0], gw2.position[0]],
                           [gw1.position[1], gw2.position[1]],
                           color='#FF6B6B', alpha=0.6, linewidth=2, zorder=2)
        
        # Draw gateways
        gw_x = [n.position[0] for n in gateway_nodes]
        gw_y = [n.position[1] for n in gateway_nodes]
        ax.scatter(gw_x, gw_y, c='#FF6B6B', s=200, marker='o', 
                  edgecolors='white', linewidths=2, alpha=0.9, zorder=3)
        
        # Draw conductor
        conductor = self.wolfy.nodes[self.wolfy.conductor_id]
        ax.scatter([conductor.position[0]], [conductor.position[1]], 
                  c='#FFD700', s=400, marker='*', 
                  edgecolors='white', linewidths=2, alpha=1.0, zorder=4)
        
        # Labels
        ax.set_xlim(-5, self.wolfy.arena_size[0] + 5)
        ax.set_ylim(-5, self.wolfy.arena_size[1] + 5)
        ax.set_aspect('equal')
        ax.set_xlabel('X Position (meters)', color='white', fontsize=12)
        ax.set_ylabel('Y Position (meters)', color='white', fontsize=12)
        ax.tick_params(colors='white')
        
        title = f"🌐 GATEWAY NETWORK TOPOLOGY 🌐\n"
        title += f"{len(self.wolfy.gateways)} Gateways orchestrating {len(self.wolfy.nodes):,} nodes"
        ax.set_title(title, color='white', fontsize=16, fontweight='bold', pad=20)
        
        plt.tight_layout()
        plt.savefig(filename, dpi=150, facecolor='#0a0a0a')
        print(f"   ✓ Gateway network saved to {filename}")
        plt.close()
    
    def create_statistics_dashboard(self, filename: str = "wolfy_stats_dashboard.png"):
        """Create a comprehensive statistics dashboard"""
        print("📊 Creating statistics dashboard...")
        
        fig = plt.figure(figsize=(18, 12))
        fig.patch.set_facecolor('#0a0a0a')
        gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
        
        stats = self.wolfy.get_statistics()
        
        # 1. Overall stats (text)
        ax1 = fig.add_subplot(gs[0, :])
        ax1.axis('off')
        
        stats_text = f"""
        🐺 WOLFY'S MESH CONCERT - FINAL STATISTICS 🐺
        
        Total Nodes: {stats['total_nodes']:,}  |  Active Participants: {stats['active_nodes']:,} ({stats['participation_rate']*100:.1f}%)
        Total Beats: {stats['beats_performed']}  |  Events Logged: {stats['total_events']}
        Gateway Nodes: {len(stats['gateways'])}  |  Conductor: Node #{stats['conductor']}
        Average Participation Score: {stats['avg_participation_score']:.2f}
        """
        
        ax1.text(0.5, 0.5, stats_text, ha='center', va='center', 
                color='white', fontsize=14, fontfamily='monospace',
                bbox=dict(boxstyle='round', facecolor='#1a1a1a', 
                         edgecolor='#FFD700', linewidth=2))
        
        # 2. Node state distribution
        ax2 = fig.add_subplot(gs[1, 0])
        ax2.set_facecolor('#0a0a0a')
        
        state_counts = {}
        for node in self.wolfy.nodes:
            state_counts[node.state.value] = state_counts.get(node.state.value, 0) + 1
        
        colors = ['#FFD700', '#FF6B6B', '#00FFFF', '#FF00FF', '#808080']
        wedges, texts, autotexts = ax2.pie(state_counts.values(), 
                                            labels=state_counts.keys(),
                                            colors=colors[:len(state_counts)],
                                            autopct='%1.1f%%',
                                            startangle=90)
        
        for text in texts:
            text.set_color('white')
        for autotext in autotexts:
            autotext.set_color('black')
            autotext.set_fontweight('bold')
        
        ax2.set_title('Node State Distribution', color='white', fontweight='bold')
        
        # 3. Participation histogram
        ax3 = fig.add_subplot(gs[1, 1])
        ax3.set_facecolor('#0a0a0a')
        
        participation_scores = [n.participation_score for n in self.wolfy.nodes if n.participation_score > 0]
        ax3.hist(participation_scores, bins=30, color='#FF6B6B', alpha=0.7, edgecolor='white')
        ax3.set_xlabel('Participation Score', color='white')
        ax3.set_ylabel('Number of Nodes', color='white')
        ax3.set_title('Participation Distribution', color='white', fontweight='bold')
        ax3.tick_params(colors='white')
        ax3.grid(True, alpha=0.2, color='white')
        
        # 4. Battery levels
        ax4 = fig.add_subplot(gs[1, 2])
        ax4.set_facecolor('#0a0a0a')
        
        battery_levels = [n.battery for n in self.wolfy.nodes]
        ax4.hist(battery_levels, bins=20, color='#00FF00', alpha=0.7, edgecolor='white')
        ax4.set_xlabel('Battery Level', color='white')
        ax4.set_ylabel('Number of Nodes', color='white')
        ax4.set_title('Battery Distribution', color='white', fontweight='bold')
        ax4.tick_params(colors='white')
        ax4.grid(True, alpha=0.2, color='white')
        
        # 5. Network connectivity
        ax5 = fig.add_subplot(gs[2, 0])
        ax5.set_facecolor('#0a0a0a')
        
        neighbor_counts = [len(n.neighbors) for n in self.wolfy.nodes]
        ax5.hist(neighbor_counts, bins=30, color='#00FFFF', alpha=0.7, edgecolor='white')
        ax5.set_xlabel('Number of Neighbors', color='white')
        ax5.set_ylabel('Number of Nodes', color='white')
        ax5.set_title('Network Connectivity', color='white', fontweight='bold')
        ax5.tick_params(colors='white')
        ax5.grid(True, alpha=0.2, color='white')
        
        # 6. Event timeline
        ax6 = fig.add_subplot(gs[2, 1:])
        ax6.set_facecolor('#0a0a0a')
        
        event_types = {}
        for event in self.wolfy.event_log:
            event_types[event['type']] = event_types.get(event['type'], 0) + 1
        
        if event_types:
            ax6.barh(list(event_types.keys()), list(event_types.values()), 
                    color='#BC13FE', alpha=0.7, edgecolor='white')
            ax6.set_xlabel('Number of Events', color='white')
            ax6.set_title('Event Type Distribution', color='white', fontweight='bold')
            ax6.tick_params(colors='white')
            ax6.grid(True, alpha=0.2, color='white', axis='x')
        
        plt.savefig(filename, dpi=150, facecolor='#0a0a0a')
        print(f"   ✓ Statistics dashboard saved to {filename}")
        plt.close()
    
    def generate_all_visualizations(self):
        """Generate all visualizations at once"""
        print("\n🎨 GENERATING ALL VISUALIZATIONS 🎨\n")
        self.create_network_snapshot()
        self.create_participation_heatmap()
        self.create_gateway_network_diagram()
        self.create_statistics_dashboard()
        print("\n✨ All visualizations complete! ✨\n")


if __name__ == "__main__":
    print("This module is meant to be imported by wolfy_mesh_concert.py")

