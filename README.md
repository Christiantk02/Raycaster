# Raycaster

## Description

This project implements a **simple raycasting engine in Python using Pygame**.  
The goal of the project is to explore how classic **pseudo-3D rendering techniques**, used in games like *Wolfenstein 3D*, work internally.

The engine renders a **3D view of a 2D tilemap** by casting rays from the player's position and calculating the distance to the nearest wall.  
Each ray corresponds to a vertical slice on the screen, creating the illusion of a 3D environment.

The project includes:

- A **tile-based map system**
- A **player with movement and rotation**
- **Raycasting-based wall rendering**
- **Distance-based lighting/shading**
- A **minimap with ray visualization for debugging**

The minimap allows the player position, rays, and map layout to be visualized while the 3D view is rendered simultaneously.

This project is primarily intended as a **learning exercise**.

---

## Installation

To run the code, install the following Python packages:  

```bash
pip install pygame
```

## Usage

1. Run the script.
2. Press -wasd for movement.
3. Press Space again to generate another labyrinth.

## Configuration

Several parameters can be modified in `settings.py`, including:

- Field of view (FOV)
- Number of rays used for rendering
- Maximum ray depth

The map layout can also be customized directly in the `Map` class by editing the `tilemap` grid.

## References

-   ChatGPT-generated structure and Markdown formatting for README.
    
