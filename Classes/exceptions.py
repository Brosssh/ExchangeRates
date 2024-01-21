class MissingColumn(Exception):
    def __init__(self, column_name :str):
        self.column_name = column_name
