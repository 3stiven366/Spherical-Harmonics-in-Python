# Spherical Harmonics Visualization in Python

This project provides an interactive 3D visualization of **spherical harmonics** using Python and Plotly. Spherical harmonics are mathematical functions that appear in many fields of physics and engineering, especially in quantum mechanics, electromagnetism, and gravitational fields.

## 🌐 Description

The script computes and renders spherical harmonics \( Y_l^m(\theta, \phi) \) for given values of quantum numbers `l` and `m`. The visualization is generated using Plotly's 3D surface plotting capabilities, allowing for intuitive exploration of the angular part of solutions to the Laplace and Schrödinger equations in spherical coordinates.

## 📁 Structure

├── SphericalHarmonics.py
├── README.md
├── requirements.txt


## ⚙️ Dependencies

Make sure you have the following packages installed:

* `numpy`
* `scipy`
* `plotly`

You can install them via pip:

```
pip install -r requirements.txt

```

## ▶️ How to Run

1. Clone repository:

```
git clone https://github.com/yourusername/sphericalharmonics.git
cd sphericalharmonics
```

2. Run the script

```
python SphericalHarmonics.py

```
A 3D interactive plot will be displayed in your default web browser.

## 🔢 Parameters

Inside the script, you can change the values of l and m to generate different spherical harmonics. The valid range is:

- $l \geq 0$
- $-l \leq m \leq l $


