weight = input("몸무게를 입력하세요[kg]:")
weight = float(weight)
height = input("당신의 키는[m]: ")
height = float(height)
bmi = weight / height ** 2

print ("당신의 체질량지수는", bmi)