import base64

def encode_files(input_file, output_file):
  try:
    with open(input_file, 'r', encoding='utf-8') as file:
      content = file.read()
    encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    with open(output_file, 'w', encoding='utf-8') as file:
      file.write(encoded_content)
    print(f"Encoded content saved to {output_file}")
  except Exception as e:
    print(f"An error occurred: {e}")

def decode_files(input_file, output_file):
  try:
    with open(input_file, 'r', encoding='utf-8') as file:
      encoded_content = file.read()
    decoded_content = base64.b64decode(encoded_content.encode('utf-8')).decode('utf-8')
    with open(output_file, 'w', encoding='utf-8') as file:
      file.write(decoded_content)
    print(f"Decoded content saved to {output_file}")
  except Exception as e:
    print(f"An error occurred: {e}")

print("1 - Encode")
print("2 - Decode")
choice = input("Choose: ")
if int(choice) == 1:
  input_file = "encode_input.txt"
  output_file = "encode_output.txt"
  encode(input_file, output_file)
elif int(choice) == 2:
  input_file = "decode_input.txt"
  output_file = "decode_output.txt"
  decode(input_file, output_file)
