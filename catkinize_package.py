#!/usr/bin/env python

from optparse import OptionParser

from catkinize.main import catkinize_package, prompt_changes, perform_changes
from catkinize.utils import is_valid_version

def main():
    usage = 'usage: %prog path version'
    description = '''\
catkinize backups your rosbuild build files with ".backup" extension and \
creates new build files for catkin. New files are heuristically build from \
old files and will most probably need additional manual changes before \
working with catkin.'''
    parser = OptionParser(usage=usage, description=description)
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.error("You must specify 'path' and 'version' of the package.")

    path = args[0]
    version = args[1]

    if not is_valid_version(version):
        parser.error("The version must have the format: \d.\d.\d")

    changeset = catkinize_package(path, version)
    if prompt_changes(changeset):
        perform_changes(changeset)

if __name__ == '__main__':
    main()
