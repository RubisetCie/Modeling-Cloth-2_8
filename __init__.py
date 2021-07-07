#----------------------------------------------------------
# File __init__.py
#----------------------------------------------------------
 
# Addon info
bl_info = {
    "name": "Modeling Cloth",
    "author": "Rich Colburn, email: the3dadvantage@gmail.com",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Create > Modeling Cloth",
    "description": "Maintains the surface area of an object so it behaves like cloth",
    "wiki_url": "https://github.com/the3dadvantage/Modeling-Cloth-2_8",
    "category": "3D View"}

if "bpy" in locals():
    import imp
    imp.reload(ModelingCloth28)
    print("Reloaded Modeling Cloth")
else:
    from . import ModelingCloth28
    print("Imported Modeling Cloth")

def register():
    ModelingCloth28.register()

def unregister():
    ModelingCloth28.unregister()

if __name__ == "__main__":
    register()
