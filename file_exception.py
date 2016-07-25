# Dinh nghia mot ham o day.
def temp_convert(var):
   try:
      return int(var)
   except ValueError, Argument:
      print "Tham so khong chua cac so\n", Argument

# Goi ham tren.
temp_convert("xyz");
