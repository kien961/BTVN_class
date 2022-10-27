class Person:
  ten=''
  tuoi=0
  diachi=''
  def nhap(a):
    a.ten=str(input("Nhap ten: "))
    a.tuoi=int(input("Nhap tuoi: "))
    a.diachi=str(input("Nhap dia chi: "))
  def xuat(a):
    print("ten: ", a.ten)
    print("tuoi: ", a.tuoi)
    print("dia chi: ", a.diachi)
p1=Person()
p1.nhap()
p1.xuat()
p2=Person()
p2.nhap()
p2.xuat()