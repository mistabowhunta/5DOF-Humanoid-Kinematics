# 5DOF-Gauntlet-Telemetry

## Overview
This repository contains the CircuitPython firmware and PC-side UDP transmission logic for a 5-Degree-of-Freedom (5-DOF) robotic hand. 

The architecture is built on a Raspberry Pi Pico W (RP2040) and utilizes a non-blocking UDP socket server to receive real-time kinematic commands via WiFi. This allows for near-zero latency actuation of 5 independent PWM servos without hard-locking the main mechanical control loop.

## Architecture Highlights
* **Non-Blocking UDP Server:** Implemented in `code.py` using CircuitPython's `socketpool` to ensure continuous listening without halting the mechanical loop.
* **Modular Networking:** Separated WiFi authentication (`wifi_connect.py`) utilizing standard `.toml` credential management.
* **Decoupled Kinematics:** The network receiver is decoupled from the physical PWM logic (`left.py`), allowing for easy scaling to a 6-DOF system (adding wrist articulation) in future iterations.

## Hardware
* Raspberry Pi Pico W
* 5x PWM 35KG Servo Motors
* 3D Printed Gauntlet Assembly
