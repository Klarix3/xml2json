class HierarchyBuilder:
    def __init__(self, parsed_data):
        self.parsed_data = parsed_data
        self.employees = {}
        self.hierarchy = None
    def build_hierarchy(self):
        self._parse_employees()
        self._assign_direct_reports()
        root_employee = None
        for employee in self.employees.values():
            if not employee.get("manager"):
                root_employee = employee
                break
        if root_employee:
            self.hierarchy = self._build_employee_hierarchy(root_employee["email"])
        else:
            for email, data in self.employees.items():
                pass
        
        return self.hierarchy
    def _parse_employees(self):
        for item in self.parsed_data:
            if item["type"] == "employee":
                employee_data = {"direct_reports": []}
                for field in item["content"]:
                    if field["attributes"]["id"] == "email":
                        employee_data["email"] = field["content"]
                    elif field["attributes"]["id"] == "manager":
                        employee_data["manager"] = field["content"] if field["content"] else None
                self.employees[employee_data["email"]] = employee_data
    def _assign_direct_reports(self):
        for employee in self.employees.values():
            manager_email = employee.get("manager")
            if manager_email and manager_email in self.employees:
                self.employees[manager_email]["direct_reports"].append(employee)
            elif manager_email:
                pass
    def _build_employee_hierarchy(self, email):
        employee = self.employees[email]
        return {
            "employee": {
                "email": employee["email"],
                "direct_reports": [
                    self._build_employee_hierarchy(report["email"]) for report in employee["direct_reports"]
                ]
            }
        }