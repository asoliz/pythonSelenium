# pythonSelenium
 Python Selenium framework - testing on CURA Healthcare Service

To run pytest
https://docs.pytest.org/en/7.1.x/how-to/usage.html

Specifying which tests to run:
Pytest supports several ways to run and select tests from the command-line.

--Run tests in a module

pytest test_mod.py

--Run tests in a directory

pytest testing/

--Run tests by keyword expressions

pytest -k "MyClass and not method"

This will run tests which contain names that match the given string expression (case-insensitive), which can include Python operators that use filenames, class names and function names as variables. The example above will run TestMyClass.test_something but not TestMyClass.test_method_simple.


Command-line Flags (add at the end)
For reporting:
-v, --verbose         increase verbosity.

Running based on keywords
-k <keyword>