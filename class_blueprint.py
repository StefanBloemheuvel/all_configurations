class ProjectHelper:
    """
    A sample utility class for your projects.
    You can customize this by adding your own methods and properties.
    """

    def __init__(self, database=None, schema=None):
        """
        Initializes the helper class.
        'project_name' is an example of a property you might set.
        'database' and 'schema' are for database connection info.
        """
        self.database = database
        self.schema = schema

    def say_hello(self):
        """
        A sample function that prints a hello message.
        """
        print(f"Hello, world! Welcome to {self.project_name}.")

    def sample_function_two(self, message="This is sample function 2."):
        """
        A second sample function that prints a custom message.
        """
        print(message)

if __name__ == "__main__":

    my_helper = ProjectHelper(
        database="prod_db",
        schema="analytics"
    )

    my_helper.say_hello()
    my_helper.sample_function_two("Have a great day!")


