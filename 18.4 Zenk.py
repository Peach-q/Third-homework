def bracket_check(text):
   left_br = text.count("(")
   right_br = text.count(")")
   if left_br == right_br:
       return "YES"
   else:
       return "NO"

print(bracket_check((input("Введите строку:\n"))))