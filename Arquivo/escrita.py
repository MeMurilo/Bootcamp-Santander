arquivo = open("C:\\Users\\Murilo\\Documents\\Bootcamp Santander\\Arquivo\\text.txt", "w")
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["escrevendo", "um","novo","texto"])
arquivo.close()