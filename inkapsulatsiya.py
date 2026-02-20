# 1
# class BankHisobi:
#     def __init__(self, egasi, boshlangich_hisob):
#         self.__egasi = egasi
#         self.__boshlangich_balans = float(boshlangich_hisob)
#     def get_egasi(self):
#         return self.__egasi
#     def get_boshlangich_balans(self):
#         return self.__boshlangich_balans
#     def pul_qosh(self ,miqdor ):
#         if miqdor <=0:
#             print("Noto'g'ri miqdor!")
#         else:
#             self.__boshlangich_balans += miqdor
#     def pul_chiqar(self,miqdor):
#         if miqdor <=0:
#             print("Noto'g'ri miqdor!")
#         elif miqdor >= self.get_boshlangich_balans():
#             print("Mablag' yetarli emas!")
#         else:
#             self.__boshlangich_balans -= miqdor
#
# hisob = BankHisobi("Ali" ,500000)
# print(hisob.get_egasi())
# print(hisob.get_boshlangich_balans())
# hisob.pul_qosh(20000)
# print(hisob.get_boshlangich_balans())
# hisob.pul_chiqar(10000)
# print(hisob.get_boshlangich_balans())
# 2
#class Foydalanuvchi:
#     def __init__(self, ism,parol):
#         self.ism = ism
#         self.__parol = parol
#     def get_ism(self):
#         return self.ism
#     def get_parol(self):
#         return self.__parol
#     def parolni_tekshir(self,kiritilgan_parol):
#         if kiritilgan_parol == self.__parol:
#             return True
#         else:
#             return False
#     def parolni_ozgartir(self ,eski_parol , yangi_parol):
#         if eski_parol != self.get_parol():
#             return "Eski parol noto'g'ri!"
#         elif len(yangi_parol) < 6:
#             return "Yangi parol kamida 6 ta belgi bo'lishi kerak!"
#         else:
#             return self.get_parol() == yangi_parol
# user = Foydalanuvchi("Sardor","maxfiy123")
# print(user.get_ism())
# print(user.get_parol())
# print(user.parolni_tekshir("noto'g'ri"))
# print(user.parolni_tekshir("maxfiy123"))
# user.parolni_ozgartir("xato" , "yangi456")
# user.parolni_ozgartir("maxfiy123", "123")
# user.parolni_ozgartir("maxfiy123", "yangiParol1")
# print(user.parolni_tekshir("maxfiy123"))
# print(user.parolni_tekshir("yangiParol1"))
# 3
