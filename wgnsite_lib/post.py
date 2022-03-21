 def post(judul):
    baca = open("archetypes/default.md", "r")

    f = open(judul)

    f.write(baca)
    f.close()
    print("berhasil di buat: " + judul)
    exit()



   
