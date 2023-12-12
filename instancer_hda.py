import hou

def execute():
    num_assets = hou.pwd().parm('assets').eval()

    #root path
    main_root_path = hou.pwd().parent().path()

    #main subnet
    subnet = hou.node(main_root_path).createNode("subnet","instancer")
    root_path = subnet.path()

    #move target to subnet
    target_obj_merge = hou.node(root_path).createNode("object_merge")
    target_obj_merge.parm("xformtype").set(1)
    target_obj_merge.parm("objpath1").set(hou.pwd().parm("target").eval())

    #merge node
    merge_node = hou.node(root_path).createNode("merge")

    #target node operations
    scatter_node = target_obj_merge.createOutputNode("scatter")
    scatter_node.parm("relaxpoints").set(0)

    #attribute rand
    attr_rand_names = scatter_node.createOutputNode("attribrandomize")
    attr_rand_names.parm("name").set("name")
    attr_rand_names.parm("distribution").set("discrete")
    attr_rand_names.parm("valuetype").set(1)
    attr_rand_names.parm("values").set(num_assets)

    for i in range(num_assets):
        prim_name = hou.pwd().parm("asset{}".format(i+1)).eval().split("/")[-1]
        node = hou.node(root_path).createNode("object_merge", prim_name)
        node.parm("xformtype").set(1)
        node.parm("objpath1").set(hou.pwd().parm("asset{}".format(i+1)).eval())
        pack_node = node.createOutputNode("pack")
        name_node = pack_node.createOutputNode("name")
        name_node.parm("name1").set(node.name())
        merge_node.setNextInput(name_node)
        attr_rand_names.parm("strvalue{}".format(i)).set(node.name())
        node.moveToGoodPosition()

    merge_node.moveToGoodPosition()

    #copy to points
    copy_node = hou.node(root_path).createNode("copytopoints::2.0")
    copy_node.parm("useidattrib").set(1)
    copy_node.parm("idattrib").set("name")
    copy_node.setInput(0, merge_node)
    copy_node.setInput(1, attr_rand_names)
    copy_node.moveToGoodPosition()

