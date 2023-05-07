# Welcome to Snake Search Project!
Hi! This project does not carry any payload. Made as the first relatively large independent project, although for the most part it is a set of functions that I implemented earlier, which I put together using a graphical interface.
# What features does this program have?

 - Search files by name
 - Searching for files by their content (next - *Deep Search*)
 - Providing information about the physical storage media on the computer, as well as a convenient presentation of this information in the form of graphs using the *matplotlb library*
 - Several types of file conversion to other formats

## Project structure
```mermaid
graph LR
A(src) --> B(modules)
A --> C(tests)
B --> D(__init__.py)
B --> E(__main__.py)
B --> F(disk_space.py)
B --> H(file_conversion.py)
B --> G(input_validation.py)
B --> J(search_engine.py)
C --> L(test_input_validation.py)
C --> K(test_search_engine.py)
C --> I(test_sort_tiles_extensions.py)
```
* *src\modules* - directory with all the necessary modules for work.
* *src\tests* - directory with tests.



# How to install and run?
*TBA*