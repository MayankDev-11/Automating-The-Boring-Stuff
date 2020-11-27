import img2pdf as converter

input_files =['img1.jpeg','img2.jpeg']
output_file = open("combined.pdf","wb")

output_file.write(converter.convert(input_files))
output_file.close()