#convert the messy phone number into a clean number fprmat with one digit
#"+49 (176) 123-4567" to 00491761234567

phone = "+49 (176) 123-4567"
print(phone.replace("+", "00")
      .replace("(", "")
      .replace(")", "")
      .replace(" ", "")
      .replace("-", ""))