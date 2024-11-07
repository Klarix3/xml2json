import unittest
from xml2json.formatter import JSONFormatter

class TestJSONFormatter(unittest.TestCase):
    def test_format(self):
        hierarchy = {
            "employee": {
                "email": "jane.doe@example.com",
                "direct_reports": [
                    {"employee": {
                        "email": "john.doe@example.com",
                        "direct_reports": []
                    }}
                ]
            }
        }
        
        formatter = JSONFormatter(hierarchy)
        json_output = formatter.format()
        
        expected_output = (
            '{\n'
            '    "employee": {\n'
            '        "email": "jane.doe@example.com",\n'
            '        "direct_reports": [\n'
            '            {\n'
            '                "employee": {\n'
            '                    "email": "john.doe@example.com",\n'
            '                    "direct_reports": []\n'
            '                }\n'
            '            }\n'
            '        ]\n'
            '    }\n'
            '}'
        )
        
        # Test that the formatted JSON matches the expected output
        self.assertEqual(json_output.replace(" ", ""), expected_output.replace(" ", ""))

if __name__ == '__main__':
    unittest.main()
