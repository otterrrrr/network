N = input()
for i in range(int(N)):
    str1, str2, str3, str4 = map(str, input().split(' ') )
    #print (str1, str2, str3, str4)
    STR = str1 + str2 + str3 +str4
    count = 1
    result = 0
    for j in range(len(STR)-1, -1, -1):
        #print(STR[j])
        if count % 2 == 1:
            result = result + int(STR[j])
        else:
            even = int(STR[j])*2
            sum = even//10 + even%10
            result = result + sum
        count = count + 1
    
    if result % 10 == 0:
        print('Valid')
    else:
        print('Invalid')
    