# 🐺 WOLFY QUICKSTART GUIDE 🐺

**Get up and running in 60 seconds!**

## Step 1: Setup (One Time)

```bash
./setup.sh
```

This creates a virtual environment and installs dependencies.

## Step 2: Activate Environment

```bash
source venv/bin/activate
```

## Step 3: Choose Your Experience

### 🚀 Instant Demo (Recommended First!)
See Wolfy in action immediately with pre-generated outputs:

```bash
python demo_quick.py
```

This creates:
- 🖼️ **Network visualizations** (PNG files)
- 📊 **Statistics dashboard**
- 🔥 **Participation heatmap**
- 📝 **Event log** (JSON)
- 🎬 **Narration script** (TXT)

**Open the PNG files to see the magic!**

---

### 🎭 Interactive Concert Experience
The full cinematic experience with narration:

```bash
python run_wolfy_concert.py
```

Choose from:
1. Full Experience (17,000 nodes, 60 seconds)
2. Quick Demo (5,000 nodes, 30 seconds)
3. Custom settings
4. Export narration only

---

### 🧪 System Test
Verify everything works:

```bash
python quick_test.py
```

---

## What Gets Generated?

Every simulation creates:

| File | Description |
|------|-------------|
| `wolfy_network_snapshot.png` | Visual map of mesh network with connections |
| `wolfy_heatmap.png` | Spatial & temporal participation patterns |
| `wolfy_gateway_network.png` | Gateway topology visualization |
| `wolfy_stats_dashboard.png` | Comprehensive statistics |
| `wolfy_concert_log.json` | Complete event log with all beats |
| `ryan_gosling_script.txt` | Full narration script |

---

## Quick Tips

💡 **For fastest results:** `python demo_quick.py`  
💡 **For full experience:** `python run_wolfy_concert.py` → Option 2  
💡 **To read the narration:** `cat ryan_gosling_script.txt`  
💡 **To see the data:** `cat wolfy_concert_log.json | jq` (if you have jq)

---

## Troubleshooting

**Problem:** `command not found: python`  
**Solution:** Use `python3` instead

**Problem:** `No module named 'matplotlib'`  
**Solution:** Activate virtual environment: `source venv/bin/activate`

**Problem:** Images don't show emojis  
**Solution:** That's normal! The visualizations still work perfectly.

---

## Next Steps

1. ✅ Run `demo_quick.py` to see sample outputs
2. 🎨 Open the PNG files to see visualizations
3. 📖 Read `README.md` for full documentation
4. 🎭 Run `run_wolfy_concert.py` for interactive experience
5. 🚀 Experiment with different node counts and durations

---

**Welcome to the mesh! 🐺**

*For full documentation, see README.md*

