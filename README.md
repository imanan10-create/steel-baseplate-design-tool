# steel-baseplate-design-tool
Python tool for preliminary steel base plate design checks
# Steel Base Plate Design Tool

A small Python-based structural engineering tool developed to automate part of the preliminary design workflow for steel column base plates.

## Overview
This project translates a manual base plate design process into a repeatable Python calculation workflow.

The script accepts key design inputs such as axial loads, moments, section dimensions, material strengths, and anchor layout parameters, then performs preliminary checks related to:
- factored load combinations
- load eccentricity
- concrete bearing pressure
- anchor force demand
- plate thickness estimation

## Main Inputs
- Dead load
- Live load
- Dead moment
- Live moment
- Section flange width
- Section depth
- Concrete compressive strength
- A2/A1 ratio
- Steel yield strength

## Main Outputs
- Base plate dimensions
- Estimated plate thickness
- Anchor arrangement
- Anchor rod diameter estimate
- Preliminary design-check messages

## Tech Stack
- Python
- NumPy
- math

## How to Run
```bash
pip install numpy
python newpy.py
