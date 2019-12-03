import os.path
from threading import Timer

# to import the scripts from different directory
import sys
sys.path.insert(0, '/home/weijin/PycharmProjects/')
from testhowdy import compare
# from testhowdy import dataprovider

# ans = dataprovider.simpleCalculator()
# print(ans)

user = compare.match()
print(user)

#
# print("The Testing begins now")
# print(compare.id)
# print(dataprovider.simpleCalculator())
# compare.test()
# print("The ans is "  + str(ans))

# a = Timer(1.0, fileExistsMsg)
# b = Timer(4.0, noFileMsg)
#




