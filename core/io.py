import trimesh

def load_mesh(path: str):
    mesh = trimesh.load(path)
    return mesh.vertices
