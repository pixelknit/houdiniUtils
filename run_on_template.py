import hou
import os
import sys

#DIRPATH = "/Users/felipepesantez/Downloads/assets/zip_test/cgaxis_models_109_01"

def grab_sop_create(root):
    return [node for node in root.children() if node.type().name() == "sopcreate"][0]

def batch_process_usd(dir_path):
    obj_file = [file for file in os.listdir(dir_path) if file.endswith(".obj")][0]
    asset_name = obj_file[:-4]
    primitive_lop = hou.node("/stage/primitive1")
    primitive_lop.parm("primpath").set(asset_name)

    sop_create_lop = grab_sop_create(hou.node("/stage"))
    sop_context_file = hou.node(sop_create_lop.path() + "/sopnet/create/file1")
    sop_context_file.parm("file").set(dir_path + "/" + obj_file)
    sop_create_lop.setName(asset_name)

    materials = ["leaves","leaves_small","trunk","twigs"]

    matlib_lop = hou.node("/stage/materiallibrary2")

    for i,material in enumerate(materials):
        matlib_lop.parm(f"matpath{i+1}").set(f"/{asset_name}/materials/{material}")
        matlib_lop.parm(f"geopath{i+1}").set(f"/{asset_name}/{asset_name}/{material}")
        inner_subnet = hou.node(matlib_lop.path() + "/" + material)
        inner_texture_node = hou.node(inner_subnet.path() + "/usduvtexture1")
        #texture file
        if material == "leaves":
            texture_file = [file for file in os.listdir(dir_path + "/maps") if file.endswith("01.jpg")][0]
        elif material == "trunk":
            texture_file = [file for file in os.listdir(dir_path + "/maps") if file.endswith("03.jpg")][0]
        elif material == "twigs":
            texture_file = [file for file in os.listdir(dir_path + "/maps") if file.endswith("02.jpg")][0]
        elif material == "leaves_small":
            texture_file = [file for file in os.listdir(dir_path + "/maps") if file.endswith("04.jpg")][0]

        inner_texture_node.parm("file").set(dir_path + "/" + texture_file)
    rop_output = hou.node("/stage/usd_rop1")
    rop_output.parm("lopoutput").set(dir_path + "/usd_export/" + asset_name + ".usd")
    rop_output.parm("execute").pressButton()

if __name__ == "__main__":
    hip_file = sys.argv[1]
    input_folder = sys.argv[2]

    hou.hipFile.load(hip_file)
    batch_process_usd(input_folder)
