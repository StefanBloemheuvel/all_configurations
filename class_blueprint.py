class ProjectHelper:
    """
    A sample utility class for your projects.
    You can customize this by adding your own methods and properties.
    """

    def __init__(self, project_name="Default Project", database=None, schema=None):
        """
        Initializes the helper class.
        'project_name' is an example of a property you might set.
        'database' and 'schema' are for database connection info.
        """
        self.project_name = project_name
        self.database = database
        self.schema = schema
        print(
            f"ProjectHelper initialized for: {self.project_name} "
            f"(DB: {self.database}, Schema: {self.schema})"
        )

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

# This part of the script will only run if the file is executed directly
# It serves as an example of how to use the class
if __name__ == "__main__":
    # 1. Create an instance of the class
    my_helper = ProjectHelper(
        project_name="My Awesome App",
        database="prod_db",
        schema="analytics"
    )

    # 2. Call the sample functions
    my_helper.say_hello()
    my_helper.sample_function_two("Have a great day!")

    # 3. You can also create another instance
    other_helper = ProjectHelper("Another Cool Project")
    other_helper.say_hello()

