#input string
name = input("Masukkan nama lengkap anda: ")

#input integer
age = int(input("Masukkan umur anda: "))

#input float
height = float(input("Masukkan tinggi anda dalam cm: "))

#input boolean
bool_python_input = input("Apakah anda suka python? (iya/tidak): ")
bool_python = bool_python_input.lower() == "iya"

#simpan jawaban dan label ke dalam list
answers = [name, age, height, bool_python]
labels  = ["Nama", "Umur", "Tinggi", "Suka python"]





##Tampilkan tipe data dari setiap jawaban
#print("/nTipe data dari setiap jawaban")
#for i in range (len(answer)):
#     print (f"{labels[i]}  :  {type(answer[i])}")

#tampilkan hasil tanpa menggunakan perulangan
print("/n===== Output Data =====")
print(f"{labels[0]} : {answers[0]}")
print(f"{labels[1]} : {answers[1]}")
print(f"{labels[2]} : {answers[2]}")
print(f"{labels[3]} : {answers[3]}")


#tampilkan tipe data dari setiap jawaban
print("/nTipe data dari setiap jawaban:")
print(f"{labels[0]} : {answers[0]}")
print(f"{labels[1]} : {answers[1]}") 
print(f"{labels[2]} : {answers[2]}")
print(f"{labels[3]} : {answers[3]}")