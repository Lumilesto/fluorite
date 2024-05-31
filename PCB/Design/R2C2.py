import numpy as np
E48 = [1.00,1.05,1.10,
       1.15,1.21,1.27,
       1.33,1.40,1.47,
       1.54,1.62,1.69,
       1.78,1.87,1.96,
       2.05,2.15,2.26,
       2.37,2.49,2.61,
       2.74,2.87,3.01,
       3.16,3.32,3.48,
       3.65,3.83,4.02,
       4.22,4.42,4.64,
       4.87,5.11,5.36,
       5.62,5.90,6.19,
       6.49,6.81,7.15,
       7.50,7.87,8.25,
       8.66,9.09,9.53]

error = 1e9
Res = [0,0,0,0]
count = 0
full = 48**4*6**4
percent = full*0.01
refreshpoint = 0
for r1 in E48:
    for e1 in range(0,6):
        R1 = r1 * 10**e1
        for r2 in E48:
            for e2 in range(0,6):
                R2 = r2 * 10**e2
                for c1 in E48:
                    for e3 in range(-9,-3):
                        C1 = c1 * 10**e3
                        for c2 in E48:
                            for e4 in range(-9,-3):
                                C2 = c2 * 10**e4
                                count = count + 1
                                err1 = abs(1-0.5*(1+(2*np.pi*10*R1*C1)**2)**0.5*(1+(2*np.pi*10*R2*C2)**2)**0.5)
                                if(err1<error):
                                    error = err1
                                    Res[0]=R1
                                    Res[1]=R2
                                    Res[2]=C1
                                    Res[3]=C2
#                                print(f'{R1} {R2} {C1} {C2}')
#                                print(err1)
                                if(count-refreshpoint>percent):
                                    refreshpoint = count
                                    ppp = count/full*100
                                    print(f'{ppp}%')
print("R1    R2    C1    C2    error")
print(f'{Res}    {error}')
#

