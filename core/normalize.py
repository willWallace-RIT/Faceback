import numpy as np

def normalize_mesh(vertices: np.ndarray) -> np.ndarray:
    center = vertices.mean(axis=0)
    vertices = vertices - center
    scale = np.linalg.norm(vertices, axis=1).max()
    return vertices / scale
