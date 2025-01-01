def read_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")
        return read_input(prompt)

def main():
    print("Geometri Hesap Makinesine Hoşgeldiniz")
    print("Yüzey alanını hesaplamak istiyorsanız 1'e")
    print("Hacmi hesaplamak istiyorsanız 2'ye basın")

    choice = read_input("Seçiminiz: ")

    if choice == 1:
        print("Hangi geometrik şeklin yüzey alanını hesaplamak istiyorsanız tuşlayın")
        print("1=) KÜP")
        print("2=) SİLİNDİR")
        print("3=) KONİ")
        print("4=) KÜRE")
        print("5=) YARIM KÜRE")
        print("6=) DİKDÖRTGEN PRİZMA")
        print("7=) ÜÇGEN PRİZMA")

        shape = read_input("Seçiminiz: ")

        if shape == 1:
            side = read_input("KÜPÜN KENAR UZUNLUĞUNU GİRİNİZ: ")
            area = 6 * (side ** 2)
            print(f"KÜPÜN ALANI: {area}")
        elif shape == 2:
            radius = read_input("SİLİNDİRİN YARIÇAPINI GİRİNİZ: ")
            height = read_input("SİLİNDİRİN YÜKSEKLİĞİNİ GİRİNİZ: ")
            pi = 3.14
            area = 2 * pi * (radius ** 2) + 2 * pi * radius * height
            print(f"SİLİNDİRİN ALANI: {area}")
        elif shape == 3:
            radius = read_input("KONİNİN YARIÇAPINI GİRİNİZ: ")
            slant_height = read_input("KONİNİN EĞİK YÜKSEKLİĞİNİ GİRİNİZ: ")
            pi = 3.14
            area = pi * (radius ** 2) + pi * slant_height * radius
            print(f"KONİNİN ALANI: {area}")
        elif shape == 4:
            radius = read_input("KÜRENİN YARIÇAPINI GİRİNİZ: ")
            area = 4 * 3.14 * (radius ** 2)
            print(f"KÜRENİN ALANI: {area}")
        elif shape == 5:
            radius = read_input("YARIM KÜRENİN YARIÇAPINI GİRİNİZ: ")
            area = 3 * 3.14 * (radius ** 2)
            print(f"YARIM KÜRENİN ALANI: {area}")
        elif shape == 6:
            height = read_input("DİKDÖRTGEN PRİZMANIN YÜKSEKLİĞİNİ GİRİNİZ: ")
            length = read_input("DİKDÖRTGEN PRİZMANIN UZUNLUĞUNU GİRİNİZ: ")
            width = read_input("DİKDÖRTGEN PRİZMANIN GENİŞLİĞİNİ GİRİNİZ: ")
            area = 2 * (length * height + height * width + width * length)
            print(f"DİKDÖRTGEN PRİZMANIN ALANI: {area}")
        elif shape == 7:
            base_height = read_input("TABAN YÜKSEKLİĞİNİ GİRİNİZ: ")
            base_length = read_input("TABAN UZUNLUĞUNU GİRİNİZ: ")
            base_area = (base_height * base_length) / 2
            prism_height = read_input("ÜÇGEN PRİZMANIN YÜKSEKLİĞİNİ GİRİNİZ: ")
            area = 2 * base_area + (prism_height * (base_length * 3))
            print(f"ÜÇGEN PRİZMANIN ALANI: {area}")
        else:
            print("Lütfen geçerli bir sayı giriniz")

    elif choice == 2:
        print("Hangi geometrik şeklin hacmini hesaplamak istiyorsanız tuşlayın")
        print("1=) KÜP")
        print("2=) SİLİNDİR")
        print("3=) KONİ")
        print("4=) KÜRE")
        print("5=) YARIM KÜRE")
        print("6=) DİKDÖRTGEN PRİZMA")
        print("7=) ÜÇGEN PRİZMA")

        shape = read_input("Seçiminiz: ")

        if shape == 1:
            side = read_input("KÜPÜN KENAR UZUNLUĞUNU GİRİNİZ: ")
            volume = side ** 3
            print(f"KÜPÜN HACMİ: {volume}")
        elif shape == 2:
            radius = read_input("SİLİNDİRİN YARIÇAPINI GİRİNİZ: ")
            height = read_input("SİLİNDİRİN YÜKSEKLİĞİNİ GİRİNİZ: ")
            pi = 3.14
            volume = pi * height * (radius ** 2)
            print(f"SİLİNDİRİN HACMİ: {volume}")
        elif shape == 3:
            radius = read_input("KONİNİN YARIÇAPINI GİRİNİZ: ")
            height = read_input("KONİNİN YÜKSEKLİĞİNİ GİRİNİZ: ")
            pi = 3.14
            volume = (pi * height * (radius ** 2)) / 3
            print(f"KONİNİN HACMİ: {volume}")
        elif shape == 4:
            radius = read_input("KÜRENİN YARIÇAPINI GİRİNİZ: ")
            volume = (4 / 3) * 3.14 * (radius ** 3)
            print(f"KÜRENİN HACMİ: {volume}")
        elif shape == 5:
            radius = read_input("YARIM KÜRENİN YARIÇAPINI GİRİNİZ: ")
            volume = (2 / 3) * 3.14 * (radius ** 3)
            print(f"YARIM KÜRENİN HACMİ: {volume}")
        elif shape == 6:
            height = read_input("DİKDÖRTGEN PRİZMANIN YÜKSEKLİĞİNİ GİRİNİZ: ")
            length = read_input("DİKDÖRTGEN PRİZMANIN UZUNLUĞUNU GİRİNİZ: ")
            width = read_input("DİKDÖRTGEN PRİZMANIN GENİŞLİĞİNİ GİRİNİZ: ")
            volume = length * width * height
            print(f"DİKDÖRTGEN PRİZMANIN HACMİ: {volume}")
        elif shape == 7:
            base_height = read_input("TABAN YÜKSEKLİĞİNİ GİRİNİZ: ")
            base_length = read_input("TABAN UZUNLUĞUNU GİRİNİZ: ")
            base_area = (base_height * base_length) / 2
            prism_height = read_input("ÜÇGEN PRİZMANIN YÜKSEKLİĞİNİ GİRİNİZ: ")
            volume = base_area * prism_height
            print(f"ÜÇGEN PRİZMANIN HACMİ: {volume}")
        else:
            print("Lütfen geçerli bir sayı giriniz")
    else:
        print("Lütfen geçerli bir sayı giriniz")

if __name__ == "__main__":
    main()
