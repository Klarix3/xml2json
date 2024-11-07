import cmd
from xml2json.parser import XMLParser
from xml2json.hierarchy_builder import HierarchyBuilder
from xml2json.formatter import JSONFormatter
class XMLToJSONApp(cmd.Cmd):
    intro = "Welcome! Type 'parse <filename> [output_filename]' to start or 'exit' to quit."
    prompt = "(xmltojson) "
    def do_parse(self, args):
        try:
            args = args.split()
            filename = args[0]
            output_filename = args[1] if len(args) > 1 else filename.rsplit('.', 1)[0] + '.json'
            with open(filename, 'r', encoding="utf-8") as file:
                xml_content = file.read()
            parser = XMLParser(xml_content)
            parsed_data = parser.parse()
            hierarchy_builder = HierarchyBuilder(parsed_data)
            hierarchy = hierarchy_builder.build_hierarchy()
            formatter = JSONFormatter(hierarchy)
            json_output = formatter.format()
            with open(output_filename, 'w', encoding="utf-8") as json_file:
                json_file.write(json_output)
        except FileNotFoundError:
            print(f"File {filename} does not exist.")
        except ValueError as e:
            print(f"XML format error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    def do_exit(self, arg):
        return True
    def emptyline(self):
        pass