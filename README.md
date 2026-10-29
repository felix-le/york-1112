# LE/ENG 1112 C & D Mini Projects

Mini projects for **LE/ENG 1112 C & D: Coding and Linear Algebra** at
**York University**, Fall 2026–2027.

This repository contains work completed during York University's first-year
Block Model. The projects use Python to connect programming, mathematical
modelling, physics, and visualisation.

## Projects

### 1. Star field

[`1/stars.py`](1/stars.py) prints a small animated-style star field in the
terminal. It uses random numbers to decide where stars appear and draws a
ground line along the bottom.

Run it with:

```bash
python3 1/stars.py
```

### 2. Soccer-ball trajectories

[`1/trajectory.py`](1/trajectory.py) simulates and animates a kicked soccer
ball under three different models:

- no air resistance;
- linear air resistance; and
- quadratic air resistance.

The simulation uses numerical time-stepping and compares the resulting
trajectories in a Matplotlib graph.

## Requirements

- Python 3.9 or newer
- Matplotlib

Install Matplotlib with:

```bash
python3 -m pip install matplotlib
```

Run the trajectory simulation with:

```bash
python3 1/trajectory.py
```

## Run everything from one file

[`main.py`](main.py) is the central entry point. It runs the projects in
order, so you can use one command:

```bash
python3 main.py
```

The star field appears first in the terminal. The trajectory animation then
opens in a Matplotlib window. Close the animation window when you are done.

## Repository structure

```text
.
├── 1/
│   ├── stars.py
│   └── trajectory.py
├── main.py
└── README.md
```

## Learning goals

These mini projects provide practice with:

- Python variables, loops, functions, and conditionals;
- random simulation;
- vectors and components of velocity;
- numerical approximations using small time steps;
- comparing mathematical models; and
- presenting results with visualisations.

## Academic context

This repository is for learning and documenting coursework progress in
LE/ENG 1112 C & D. Explanations, experiments, and parameter changes may be
added as the projects develop throughout the course.
