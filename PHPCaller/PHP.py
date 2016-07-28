import subprocess

class PHP(object):
  @staticmethod
  def call(scriptPath, *args, **kwargs):
    args = list(args)
    process = subprocess.Popen(['php', scriptPath] + args, stdout=subprocess.PIPE)
    output = process.communicate()[0]
    if "transformer" in kwargs:
      return kwargs["transformer"](output)
    else:
      return output