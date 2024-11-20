# Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
def cek_kelulusan (nilai):
    if nilai > 60:
        return 'Lulus'
    else:
        return 'gagal'
    
nilai_anda = 80
status = cek_kelulusan (nilai_anda)
print(f"nilai: {nilai_anda}, status: {status}")

nilai_anda2 = 60
status2 = cek_kelulusan (nilai_anda2)
print(f"nilai: {nilai_anda2}, status: {status2}")