
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
num3=[];
if len(num1)<=len(num2):
    shortest=len(num1);
    longest=len(num2);
else:
    shortest=len(num2);
    longest=len(num1);
for i in range (shortest):
    num3.append(num1[i]);
    num3.append(num2[i]);
while i<longest:
    if longest==len(num2):
        num3.append(num2[i]);
    if longest==len(num1):
        num3.append(num1[i]);
    i+=1;
print(num3);
# ******************************
# Make your Code
# ******************************

# print (num3) 
