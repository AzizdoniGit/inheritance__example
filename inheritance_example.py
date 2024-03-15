"𝑺𝒊𝒏𝒈𝒍𝒆 𝑰𝒏𝒉𝒆𝒓𝒊𝒕𝒂𝒏𝒄𝒆"

# class Father:
#     name = "Sasha"
#     def engineer(self):
#         return "engineer"
#
#     def mechanic(self):
#         return "engineer"
#
#     def electric(self):
#         return "engineer"
#
# class Son(Father):
#     name = "Pasha"
#
# obj1 = Son()
# print(obj1.electric())


"𝑴𝒖𝒍𝒕𝒊𝒍𝒆𝒗𝒆𝒍 𝑰𝒏𝒉𝒆𝒓𝒊𝒕𝒂𝒏𝒄𝒆"

# class GrandFather:
#     name = "Vladimir"
#
#     def engineer(self):
#         return "engineer"
#
#     def mechanic(self):
#         return "mechanic"
#
#     def electric(self):
#         return "electric"
#
#
# class Father(GrandFather):
#     name = "Vova"
#
#
# class Son(Father):
#     name = "Alexander"
#
#
# relationship1 = GrandFather()
# relationship2 = Father()
# relationship3 = Son()
#
# print(f"{relationship1.name}:", relationship1.electric())
# print(f"{relationship2.name}:", relationship2.mechanic())
# print(f"{relationship3.name}:", relationship3.engineer())


"𝑴𝒖𝒍𝒕𝒊𝒑𝒍𝒆 𝑰𝒏𝒉𝒆𝒓𝒊𝒕𝒂𝒏𝒄𝒆"


# class Father:
#     name = "Alexey"
#
#     def __init__(self):
#         self.driving = "drive"
#
#     def driving(self):
#         return self.driving
#
#
# class Mother:
#     name = "Sofia"
#
#     def __init__(self):
#         self.cooking = "cook"
#
#     def cooking(self):
#         return self.cooking
#
#
# class Son(Father, Mother):
#     name = "Elbek"
#
#     def __init__(self):
#         Father.__init__(self)
#         Mother.__init__(self)
#
#     def mixer(self):
#         print(f"{self.name} can {self.driving} and {self.cooking}")
#
#
# object = Son()
# object.mixer()


"𝑯𝒊𝒆𝒓𝒂𝒓𝒄𝒉𝒊𝒄𝒂𝒍 𝑰𝒏𝒉𝒆𝒓𝒊𝒕𝒂𝒏𝒄𝒆"

# class Calculate:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
# class Add(Calculate):
#     def __init__(self, a, b):
#         Calculate.__init__(self, a, b)
#
#     def add(self):
#         print("Addition:", self.a + self.b)
#
# # Derived Class
# class Subtract(Calculate):
#     def __init__(self, a, b):
#         Calculate.__init__(self, a, b)
#
#     def subtract(self):
#         print("Subtraction:", self.a - self.b)
#
#
# class Multiply(Calculate):
#     def __init__(self, a, b):
#         Calculate.__init__(self, a, b)
#
#     def subtract(self):
#         print("Multiply:", self.a * self.b)
#
# obj1 = Add(34, 98)
# obj2 = Subtract(45, 67)
# obj3 = Multiply(25, 4)
# obj1.add()
# obj2.subtract()
# obj3.subtract()


