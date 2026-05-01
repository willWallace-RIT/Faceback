import numpy as np

def compute_error(back_real: np.ndarray, back_est: np.ndarray) -> np.ndarray:
    return np.linalg.norm(back_real - back_est, axis=1)

def error_stats(errors: np.ndarray) -> dict:
    return {
        "mean": float(errors.mean()),
        "max": float(errors.max()),
        "std": float(errors.std())
    }
