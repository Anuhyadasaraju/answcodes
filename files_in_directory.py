# ------------------------------------------------------------------------
#
# Python program to list all files in a directory in Python.
#
# AUTHOR  : Anuhya Dasaraju
# VERSION  DATE             AUTHOR           CHANGES
# -------  ----             -------          -------
# 1.0      29th Mar, 2024   Anuhya Dasaraju  Initial version
#
# ------------------------------------------------------------------------

import os

def list_files(directory):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a regular file (not a directory)
        if os.path.isfile(os.path.join(directory, filename)):
            print(filename)

# Example usage
directory_path = '/Users/anuhya/test' # Specify the directory path here
list_files(directory_path)