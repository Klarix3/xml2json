import unittest
from xml2json.parser import XMLParser

class TestXMLParser(unittest.TestCase):
    def test_parse_employees(self):
        xml_content = '''
        <?xml version="1.0"?>
        <employees>
            <employee>
                <field id="email">john.doe@example.com</field>
                <field id="manager">jane.doe@example.com</field>
            </employee>
            <employee>
                <field id="email">jane.doe@example.com</field>
            </employee>
        </employees>
        '''
        parser = XMLParser(xml_content)
        parsed_data = parser.parse()
        
        # Check if it parsed the correct number of employees
        self.assertEqual(len(parsed_data), 2)
        
        # Check the content of the first employee
        self.assertEqual(parsed_data[0]["content"][0]["content"], "john.doe@example.com")
        self.assertEqual(parsed_data[0]["content"][1]["content"], "jane.doe@example.com")
        
        # Check that the second employee has no manager
        self.assertIsNone(parsed_data[1]["content"][1]["content"])

    def test_parse_empty_field(self):
        xml_content = '''
        <employees>
            <employee>
                <field id="email">alice@example.com</field>
                <field id="manager"/>
            </employee>
        </employees>
        '''
        parser = XMLParser(xml_content)
        parsed_data = parser.parse()
        
        self.assertEqual(parsed_data[0]["content"][0]["content"], "alice@example.com")
        self.assertIsNone(parsed_data[0]["content"][1]["content"])

if __name__ == '__main__':
    unittest.main()
