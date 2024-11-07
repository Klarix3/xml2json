import unittest
from xml2json.hierarchy_builder import HierarchyBuilder

class TestHierarchyBuilder(unittest.TestCase):
    def test_build_hierarchy(self):
        parsed_data = [
            {"type": "employee", "content": [
                {"attributes": {"id": "email"}, "content": "john.doe@example.com"},
                {"attributes": {"id": "manager"}, "content": "jane.doe@example.com"}
            ]},
            {"type": "employee", "content": [
                {"attributes": {"id": "email"}, "content": "jane.doe@example.com"},
                {"attributes": {"id": "manager"}, "content": None}
            ]}
        ]
        
        hierarchy_builder = HierarchyBuilder(parsed_data)
        hierarchy = hierarchy_builder.build_hierarchy()
        
        # Check if Jane Doe is the root manager
        self.assertIn("employee", hierarchy)
        self.assertEqual(hierarchy["employee"]["email"], "jane.doe@example.com")
        
        # Check John's relationship under Jane
        self.assertEqual(len(hierarchy["employee"]["direct_reports"]), 1)
        self.assertEqual(hierarchy["employee"]["direct_reports"][0]["employee"]["email"], "john.doe@example.com")

if __name__ == '__main__':
    unittest.main()
