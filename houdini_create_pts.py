import hou
import csv


node = hou.pwd()
geo = node.geometry()

csv_file_path = "csv/path"

with open(csv_file_path, "r") as file:
    reader = csv.reader(file)

    next(reader, None)

    for row in reader:
        point_id, x ,y ,z = row

        x, y, z = float(x), float(y), float(z)

        pt = geo.createPoint()
        pt.setPosition(hou.Vector3(x,y,z))
