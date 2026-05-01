FaceBack: Head Reconstruction Error Pipeline

Overview

FaceBack evaluates how well a reconstructed face (e.g. from Unreal Engine 5 MetaHuman)
can predict the back of a head using symmetry assumptions.

Pipeline

1. Capture real face + back-of-head
2. Generate reconstructed face (UE5 MetaHuman)
3. Mirror reconstructed face to estimate back
4. Compare against real back
5. Output error metrics

Features

- Mesh normalization
- Symmetry-based inference
- Error computation (per-vertex + aggregate)
- Modular + testable

Install

pip install -r requirements.txt

Run

python pipeline.py --config config.yaml

Structure

faceback/
├── core/
├── models/
├── tests/
├── data/
├── pipeline.py
├── config.yaml
