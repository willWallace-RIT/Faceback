import yaml
from core.io import load_mesh
from core.normalize import normalize_mesh
from core.mirror import mirror_head
from core.error import compute_error, error_stats
import numpy as np

def run_pipeline(config_path: str):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    face_real = load_mesh(config["data"]["face_real"])
    back_real = load_mesh(config["data"]["back_real"])
    face_recon = load_mesh(config["data"]["face_recon"])

    face_real = normalize_mesh(face_real)
    back_real = normalize_mesh(back_real)
    face_recon = normalize_mesh(face_recon)

    back_est = mirror_head(face_recon)

    errors = compute_error(back_real, back_est)
    stats = error_stats(errors)

    print("Error Stats:", stats)

    if config["output"]["save_errors"]:
        np.save(config["output"]["error_path"], errors)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    run_pipeline(args.config)
