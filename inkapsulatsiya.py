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

