class BuildingError(Exception):
    def __str__(self):
        return f"With so much material house cannot be building"

def check_material(a_mat, limit_v):
    if a_mat > limit_v:
        return "enough material"
    else:
        raise BuildingError(a_mat)


materials = 123
check_material(materials, limit_v)