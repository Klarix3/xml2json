import re

class XMLParser:
    def __init__(self, xml_content):
        self.xml_content = xml_content
    
    def parse(self):
        xml = self._remove_xml_declaration(self.xml_content)
        if not xml.startswith('<') or not xml.endswith('>'):
            raise ValueError("Invalid XML format")
        return self._parse_employees(xml)
    
    def _remove_xml_declaration(self, xml):
        return re.sub(r'<\?.*?\?>', '', xml).strip()
    
    def _parse_employees(self, xml):
        # Find all <employee> elements in XML
        employee_pattern = r'<employee>(.*?)</employee>'
        employees_data = re.findall(employee_pattern, xml, re.DOTALL)
        
        employees = []
        for employee_data in employees_data:
            employee = {"type": "employee", "content": self._parse_fields(employee_data)}
            employees.append(employee)
        
        return employees
    
    def _parse_fields(self, employee_data):
        # Find all <field> elements inside <employee>
        field_pattern = r'<field\s+id="(\w+)">(.*?)</field>'
        fields = []
        
        for match in re.finditer(field_pattern, employee_data):
            field_id = match.group(1)
            field_content = match.group(2).strip() if match.group(2).strip() else None
            fields.append({"attributes": {"id": field_id}, "content": field_content})
        
        # Handle <field> elements without closing tags, e.g., <field id="manager"/>
        empty_field_pattern = r'<field\s+id="(\w+)"\s*/>'
        for match in re.finditer(empty_field_pattern, employee_data):
            field_id = match.group(1)
            fields.append({"attributes": {"id": field_id}, "content": None})
        
        return fields
