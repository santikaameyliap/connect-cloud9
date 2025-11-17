# list
# Sebuah tipe data yang bisa menyimpan banyak niali
myList = ["Jeruk", "Anggur", "Apel", 50000]
print(type(myList))
print(myList)
print(myList[1])
myList[0] = "Jeruk Bali" # Reassignment, overriding
print(myList)

# Tuple
# Data type yang mirip dengan list, namun bersifat immutable (Tidak bisa dirubah)

myTuple = ("Jeruk Mandarin", "Anggur", "Apel", 50000)
print(myTuple)
print(myTuple[1])
# myTuple[0] = "Jeruk Bali" # Reassignment, overriding
# print(myTuple)

# Dictionary
# Menyimpan nilai berupa pasangan key-value, Bersifat mutable/bisa diganti. Indeks (key) bisa diganti.
"""
String: Paling umum digunakan karena bersifat deskriptif.
Angka: Baik integer maupun float.
Tuple: Karena tuple tidak dapat diubah, ia bisa digunakan sebagai key. 
Tipe data yang tidak bisa digunakan sebagai key 
List: Karena list dapat diubah (mutable), tidak bisa dijadikan key.
Dictionary: Sama seperti list, dictionary tidak dapat diubah, sehingga tidak bisa menjadi key.
"""
import json

myDictionary = {
    "buah1": "Jeruk",
    "buah2": "Anggur",
    "buah3": "Apel",
    "harga": 50000
}
print(type(myDictionary))
print(myDictionary)
print(myDictionary["buah2"])
myDictionary["buah1"] = "Jeruk Bali"
print(myDictionary)


# print biar rapi (istilahnya "pretty")
print(json.dumps(myDictionary, indent=4))


####################
## CHALLENGE TIME ##
####################

# 1. MIsalkan saya punya list myProgrammingLang = ["Python", "Shell", "Javascript", "PHP", "Golang", "C++"].
# Bagaimana cara memanggil golang dan C++ hanya dengan menggunakan satu pasang square bracket.
myProgrammingLang = ["Python", "Shell", "Javascript", "PHP", "Golang", "C++"]
print(myProgrammingLang[4:6]) # cara start:stop
print(myProgrammingLang[-2:])
print(myProgrammingLang[4:])
print(myProgrammingLang[-2])
print(myProgrammingLang[2:4],myProgrammingLang[5])

# 2. Misalkan saya punya complex nested dictionary:
myComplexDict = {
    "name": "santika ameylia",
    "alamat": {
        "provinsi": "Jawa Timur",
        "kecamatan": "Kawedanan",
        "desa": "Sumberdodol",
        "RT": "01",
        "RW": "02",
    },
    "siblings": ["Tama", "Dewi", "Carmen"]
}

# Bagaimana cara untuk memunculkan: Nama santika ameylia, alamat: Sumberdodol, Kawedanan RT 01, RW 02. Saudara: Tama, Dewi, Carmen

