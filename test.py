from PHPCaller import PHP
import json

if __name__ == "__main__":
  data = PHP.call("echo.php", "123", "456", transformer=json.loads)
  print(data)