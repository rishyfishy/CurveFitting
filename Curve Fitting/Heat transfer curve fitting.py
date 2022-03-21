import fittingFunctions
import csv
import matplotlib.pyplot as plt
import math

Re=[60,120,300,600]
Nu=[4.824,8.184,18.27,30.492]
Bu=[]

a,b=fittingFunctions.powerLawFit(Re,Nu)
Pr=0.243
print (a,b)
m=a
C=b-math.log(Pr)/3
print("m = {}".format(m))
print("C = {}".format(C))

plt.figure(1)
plt.plot(Re,Nu)
plt.plot(Re,[b*Rei**a for Rei in Re])
plt.show()
# x_data = []
# y_data_t1 = []
# y_data_t2 = []
# y_data_t3 = []
# y_data_t4 = []
# with open("Q2.csv") as data:
#     csvReader = csv.reader(data,delimiter = ",")

#     i=0
#     for row in csvReader:
#         # print(row)
#         if i>0:
#             x_data.append(float(row[0]))
#             y_data_t1.append(float(row[1]))
#             y_data_t2.append(float(row[2]))
#             y_data_t3.append(float(row[3]))
#             y_data_t4.append(float(row[4]))
        
#         i+=1

# a1,b1=fittingFunctions.exponentialFit(x_data,y_data_t1)
# a2,b2=fittingFunctions.exponentialFit(x_data,y_data_t2)
# a3,b3=fittingFunctions.exponentialFit(x_data,y_data_t3)
# a4,b4=fittingFunctions.exponentialFit(x_data,y_data_t4)

# print(a1,b1,a2,b2,a3,b3,a4,b4)

# plt.figure(1)
# plt.plot(x_data,y_data_t1)
# plt.plot(x_data,[b1*math.exp(a1*xi) for xi in x_data])
# plt.figure(2)
# plt.plot(x_data,y_data_t2)
# plt.plot(x_data,[b2*math.exp(a2*xi) for xi in x_data])
# plt.figure(3)
# plt.plot(x_data,y_data_t3)
# plt.plot(x_data,[b3*math.exp(a3*xi) for xi in x_data])
# plt.figure(4)
# plt.plot(x_data,y_data_t4)
# plt.plot(x_data,[b4*math.exp(a4*xi) for xi in x_data])
# plt.show()
# plt.xlabel("x")
# plt.ylabel("y")

