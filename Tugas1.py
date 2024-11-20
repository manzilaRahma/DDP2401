# Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
print('## Nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    fahrenheit=(celcius*9/5)+32 #Mengkonversi suhu dari celcius ke fahreneit
    return fahrenheit # Mengembalikan nilai fahrenheit

suhu_celcius1 = 0
suhu_celcius2 = 100
suhu_fahrenheit1 = celcius_ke_fahrenheit(suhu_celcius1)
suhu_fahrenheit2 = celcius_ke_fahrenheit(suhu_celcius2)
print('suhu celcius', suhu_celcius1, 'sama dengan', suhu_fahrenheit1)
print('suhu celcius', suhu_celcius2, 'sama dengan', suhu_fahrenheit2)