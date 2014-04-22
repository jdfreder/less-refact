from __future__ import print_function

import re
import os

_get_files = lambda regex, path: [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(os.path.expanduser(path))
    for f in files if regex.match(f)]
_less_regex = re.compile(r'(@)([a-zA-Z0-9\_\-]+?)([:;\)\s,])')

def list(path='~/ipython/IPython/html', filename_regex=r'.*\.less$'):
    """List the less variables defined in a given path.

    Arguments
    ----------
    path: String
        Path to the LESS directory.  Only .less files are opened.
    OPTIONAL filename_regex: String
        Defaults to "*\.less$"
        Regular expression to use when matching file names."""
    matches = []
    for filename in _get_files(re.compile(filename_regex), path):
        with open(filename, 'r') as f:
            matches += [match[1] for match in _less_regex.findall(f.read())]
    [print(match) for match in sorted(set(matches))]

if __name__ == '__main__':
    print('This must be run with Python Fabric.')
