# Mscript
> **Warning:** These scripts automate Minecraft actions. Use only on singleplayer or servers where automation is permitted. Using these on public or multiplayer servers may result in a ban.

A collection of Python automation scripts for Minecraft using [Minescript](https://minescript.net/).

## Requirements

- Minecraft (Java Edition)
- [Minescript mod](https://minescript.net/) installed
- Python 3.x (bundled with Minescript)

## Installation

1. Install the Minescript mod for your Minecraft version
2. Clone or download this repo into your `minecraft/minescript/` folder:

```bash
git clone https://github.com/yourusername/mscripts
```

3. Run any script from the in-game chat:

```
\script_name
```

## Scripts
```
src/
├── farms/
│   └── mining/
│       └── auto_cobble.py
└── macros/
    ├── auto_attack.py
    └── auto_strafe.py
```

## Usage Tips

- To stop any running script, type `\kill -1` in chat
- To prevent Minecraft from pausing when you tab out, go to **Esc - Open to LAN - Start LAN World**

## Controls

| Action | Command |
|--------|---------|
| Run a script | `\script_name` |
| List running scripts | `\jobs` |
| Stop all scripts | `\kill -1` |
| Pause a script | `\suspend` |
| Resume a script | `\resume` |
