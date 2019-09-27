#the modules are nothing but the other python files
#the packages are basically a collection of modules

from class_support import Planet

naboo=Planet("Naboo",3000000,8,'Naboo System')
print(f'Name:{naboo.name}')
print(naboo.spin('at a very tremendous speed'))