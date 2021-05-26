a=float(input("Nhập a="))

b=float(input("Nhập b="))

# Giải phương trình

if a==0:

    # xét hệ số b

    if b==0:

        print("Phương trình vô số nghiệm.")

    else:

        print("Phương trình vô nghiệm")

else:

    # Tính nghiệm phương trình

    x=-b/a

    print("Nghiệm phương trình:", a,"x+",b,"=0 là:",x)
