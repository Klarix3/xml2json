# XML to JSON

## Description
XML to JSON is a command-line tool written in Python that reads an XML file containing a flat list of employees and their managers, then converts this structure into a JSON format. This JSON output reflects the organizational structure, making it easy to understand reporting relationships.

## Installation

This tool requires Python 3. To install dependencies and set up, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/your-repo/xml-to-json-converter.git
cd xml-to-json-converter
```

## Usage

Run the program by providing an XML file containing employee data. The tool includes an interactive command interface with a `parse` command.

### Command-line Usage

```bash
python xml_to_json_app.py
```

This will launch an interactive command-line session. To parse a file, type:

```plaintext
parse <input_filename.xml> [output_filename.json]
```

### Example Commands

- `parse input_file_example.xml`  
  Converts `input_file_example.xml` to a hierarchical JSON file named `input_file_example.json`.
  
- `parse input_file_example.xml output_file_example.json`  
  Converts `input_file_example.xml` and saves it as `output_file_example.json`.

### Available Commands

- `parse <input_filename> [output_filename]`: Parse an XML file and save the output as JSON.
- `exit`: Quit the application.

## Input

An example XML input file representing employees and their managers:

```xml
<employees>
    <employee>
        <field id="email">john.doe@example.com</field>
        <field id="manager">jane.doe@example.com</field>
    </employee>
    <employee>
        <field id="email">jane.doe@example.com</field>
    </employee>
</employees>
```

The XML should contain `<employee>` tags, each with `<field>` tags for `email` and `manager`. The `manager` field can be left empty if the employee does not have a manager.

## Output

The tool generates a JSON file representing the organizational hierarchy. Here’s an example of the JSON output:

```json
{
    "employee": {
        "email": "jane.doe@example.com",
        "direct_reports": [
            {
                "employee": {
                    "email": "john.doe@example.com",
                    "direct_reports": []
                }
            }
        ]
    }
}
```

**Note**: The tool outputs an error message if the XML input file is not formatted correctly or if the specified file is not found.
