import yaml
import json
import sys
from employee import Employee

with open("employees.yaml","r") as file:
    employees = yaml.safe_load(file)

with open("line_managers.yaml","r") as line_file:
    managers = yaml.safe_load(line_file)

manager_dict = {managers[manager]["department"]: managers[manager]["name"] for manager in managers}

for employee in employees:
    e = employees[employee]
    emp = Employee()
    emp.full_name = e["name"]
    e["email"] = emp.email
    if e["role"] != "Line Manager":
        e["Line Manager"] = manager_dict[e["department"]]

with open("user_data.json","w") as data_file:
    json.dump(employees, data_file, indent=4)

print("Process Done!")
