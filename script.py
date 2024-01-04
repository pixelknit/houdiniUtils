import hou
import sys

hip_file = sys.argv[1]
input_file = sys.argv[2]

hou.hipFile.load(hip_file)

file_node = hou.node("/obj/geo1/file1")
file_node.parm("file").set(input_file)

name_node = hou.node("/obj/geo1/set_name")
name_node.parm("name").set(input_file)

export_node = hou.node("/obj/geo1/filecache1")
export_node.parm("file").set(input_file + "remeshed.bgeo.sc")
export_node.parm("execute").pressButton()

