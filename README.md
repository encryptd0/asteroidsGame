# Asteroid Shooter Game

**Python · Pygame · UV Package Manager**

A simple 2D asteroid shooter game built with **Pygame**. Control a player spaceship, shoot asteroids, and survive as long as possible.  

This project demonstrates Python game development concepts, sprite management, collision detection, and logging.

---

## Features

- Player-controlled spaceship
- Shootable asteroids with split behavior
- Collision detection between player and asteroids
- Collision detection between shots and asteroids
- Event and state logging
- Smooth frame-rate independent movement

---

## How It Works

1. Initializes **Pygame** and creates the main game window
2. Groups sprites into `updatable` and `drawable` for logic and rendering
3. Spawns the player and asteroid field objects
4. Runs the game loop:
   - Handles events
   - Updates all objects
   - Checks collisions
   - Logs events and states
   - Draws all drawable objects
5. Ends the game when the player collides with an asteroid

---

## Installation

### Prerequisites

- Python 3.13 (as specified in `.python-version`)
- **uv** package manager

### Install Dependencies

```bash
uv install pygame
````

> Ensure you are in the project directory and your virtual environment is active if used.

---

## Usage

Run the game with:

```bash
uv run main.py
```

Controls:

* Move the spaceship with arrow keys or WASD
* Shoot with the space bar
* Avoid asteroids

The game will exit automatically if the player collides with an asteroid.

---

## Project Structure

```text
.
├── main.py
├── constants.py
├── player.py
├── shot.py
├── asteroid.py
├── asteroidfield.py
├── logger.py
├── .gitignore
├── .python-version
└── README.md
```

* `main.py` – main game loop
* `player.py`, `shot.py`, `asteroid.py`, `asteroidfield.py` – game object classes
* `logger.py` – event and state logging
* `constants.py` – configuration like screen size

---

## Notes

* Game state and events are logged to `game_state.jsonl` and `game_events.jsonl`
* `.gitignore` ignores cache, builds, virtual environments, and log files
* Use **Python 3.13** to ensure compatibility

> This project is intended as a learning and portfolio showcase.

---

## License

MIT License


