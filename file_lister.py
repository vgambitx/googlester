import os
class file_lister:

  def __init__(self, directory):
    self.set_path(directory)

  def set_path(self, directory):
    self.directory_path = directory

  def get_files_list(self):
    """ Get all files including subdirectories """
    f = []
    for (dirpath, dirnames, filenames) in os.walk(self.directory_path):
        f.extend( map(lambda x: os.path.join(dirpath, x), filenames))
    return f