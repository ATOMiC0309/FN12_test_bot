# named tuple
#
# class Employee:
#     def __init__(self, id, name, lastname, age, email):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email
#
# employees = [
#     (1, 'Toxir', 'Toxirov', 20, 'jaldjkla@email.com'),
#     (2, 'Sobir', 'Sobirov', 25, 'sdfsdcsc@email.com')
# ]
# for employee in employees:
#     em = Employee(*employee)
#     print(em.id, em.name, em.lastname, em.age, em.email)


# -----------------------------------------------------------------------------------------------

# from collections import namedtuple
#
# Employee = namedtuple('Employee', 'id name lastname age email')
#
# employees = [
#     (1, 'Toxir', 'Toxirov', 20, 'jaldjkla@email.com'),
#     (2, 'Sobir', 'Sobirov', 25, 'sdfsdcsc@email.com')
# ]
#
# for employee in employees:
#     em = Employee(*employee)
#     print(em.id, em.name, em.lastname, em.age, em.email)

# -----------------------------------------------------------------------------------------------
# from collections import namedtuple
# Cars = namedtuple('Cars', 'id model color speed price')
#
# cars = [
#     (1, 'Tarcker Turbo', "Orange", 260, 16000),
#     (2, 'Cobalt', "Gray", 260, 11000),
#     (3, 'Malibu', "White", 280, 22000),
# ]
#
# for car in cars:
#     c = Cars(*car)
#     print(c.id, c.model.center(18, ' '), c.color.center(10, ' '), c.speed, c.price)







































