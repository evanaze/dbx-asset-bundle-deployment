"""Apply input from the command line as variables to the Databricks environment."""

import argparse
import os
from dataclasses import dataclass

import jinja2


@dataclass
class DatabricksDeployment:
    """Class for a Databricks deployment with three environments"""

    dev_sp: str
    stage_sp: str
    prod_sp: str
    dev_host: str
    stage_host: str
    prod_host: str


def prompt_inp(reqested_input: str, retry_cnt: int = 3) -> str:
    """Prompt the user for the requested input and

    :param requested_input: The input for which to prompt the user
    :param retry_cnt: The number of retries to prompt the user for
    :raises Exception: Raise an exception if the input cannot be parsed
    """
    inp = input(f"Enter your {requested_input}: ")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Render Jinja2 templates with test_var"
    )
    parser.add_argument(
        "--test_var",
        type=str,
        required=True,
        help="The variable value to render in templates",
    )
    parser.add_argument(
        "--directory",
        type=str,
        default=".",
        help="Directory containing the templates to process",
    )
    args = parser.parse_args()

    # Create a Jinja2 environment
    env = jinja2.Environment()

    for root, dirs, files in os.walk(args.directory):
        for file_name in files:
            if file_name.endswith((".py", ".yaml")):
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, "r") as f:
                        content = f.read()
                    template = env.from_string(content)
                    rendered_content = template.render({"test_var": args.test_var})
                    with open(file_path, "w") as f:
                        f.write(rendered_content)
                except jinja2.TemplateSyntaxError as e:
                    print(f"Error rendering {file_path}: {e}")


if __name__ == "__main__":
    main()
