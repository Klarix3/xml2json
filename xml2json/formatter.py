class JSONFormatter:
    def __init__(self, data, indent=4):
        self.data = data
        self.indent = indent
    def format(self):
        return self._format_value(self.data, 1)
    def _format_value(self, value, level):
        indent_space = ' ' * (level * self.indent)
        if isinstance(value, dict):
            items = [f'\n{indent_space}{self._format_key(k)}: {self._format_value(v, level + 1)}' for k, v in value.items()]
            return '{' + ','.join(items) + '\n' + (' ' * ((level - 1) * self.indent)) + '}'
        elif isinstance(value, list):
            items = [self._format_value(v, level) for v in value]
            return '[' + ', '.join(items) + ']'
        else:
            return f'"{value}"'
    def _format_key(self, key):
        return f'"{key}"'