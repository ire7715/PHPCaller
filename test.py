from PHPCaller import PHP

if __name__ == "__main__":
  print PHP.call("echo.php", "123", "456")