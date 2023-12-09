def encode_message(message):
  encoded_string = ""
  i = 0
  while (i <= len(message) - 1):
    count = 1
    ch = message[i]
    j = i
    while (j < len(message) - 1):
      if (message[j] == message[j + 1]):
        count += 1
        j += 1
      else:
        break
    encoded_string = encoded_string + ch + str(count)
    i = j + 1
  return encoded_string

message = input("Введите буквы: ")
print(encode_message(message))

# message = "AAAABBCAA"
# encoded_string = "A4B2C1A2"
