import numpy as np

def mirror_head(vertices: np.ndarray) -> np.ndarray:
    mirrored = vertices.copy()
    mirrored[:, 0] *= -1  # Flip X-axis
    return mirrored
