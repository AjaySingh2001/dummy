with open('example.txt', 'w+') as file:
  
   # Write data to the file
   file.write('Hello, World!')
    
   # Move the file pointer to the beginning of the file
   file.seek(0)
    
   # Read the contents of the file
   contents = file.read()
    
   # Print the contents of the file
   print(contents)