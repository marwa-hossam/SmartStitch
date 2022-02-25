class WorkDirectory:
  """Model for holding Working Directory Information"""
  def __init__(self, input, output, subprocess):
    self.input_path = input
    self.output_path = output
    self.subprocess_path = subprocess
    self.input_files = []
    self.output_files = []
  
  # This dictates how it will look in the log file.
  def __repr__(self):
    stringRep = "\'input_path=" + str(self.input_path)
    if (self.input_files):
      stringRep += ", input_files:" + str(len(self.input_files))
    stringRep += ", output_path:" + str(self.output_path)
    if (self.output_files):
      stringRep += ", output_files:" + str(len(self.output_files))
    stringRep += ", subprocess_path=" + str(self.subprocess_path)
    stringRep += "\'"
    return stringRep