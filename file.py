try:
    # Input the path and encryption key
    path = input(r'Enter path of image:')
    key = int(input('Enter key for encryption of image:'))

    print('The path of file:', path)
    print('Key for encryption:', key)

    # fin= open(path, 'rb')

    # image = fin.read()
    # fin.close()

    # # Convert the image to a mutable bytearray for XOR operation
    # image = bytearray(image)

    # # Perform XOR operation on each byte
    # for index, values in enumerate(image):
    #     image[index] = values ^ key

    #     fin= open(path, 'wb')

    #     fin.write(image)
    #     fin.close()
    #     print('Encryption done...')
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()

    image = bytearray(image)

    encrypted_image = bytearray()  # Create a new bytearray for the encrypted data
    for index, value in enumerate(image):
      encrypted_image.append(value ^ key)

  # Write the encrypted data to a new file
    with open(path + '.enc', 'wb') as fout:  # Use a different filename
      fout.write(encrypted_image)

    print('Encryption done...')
    
except Exception:
    print('Error caught:', Exception.name)