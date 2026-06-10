문자변수 = """
        띄어쓰기 하고 싶을때,
        가독성 높이고 싶을때,,,
"""
num = 10 #숫자를 값으로 가지는 변수 num
count = 100
print(num + count, 문자변수)

list = ['사과','배']
# 데이터타입 확인
print(type(list))
#사칙연산자 *
print("Hi")
a = True
b = False
print(type(a))
#삼항식
age = 20
print("성인" if age >= 19 else "미성년자")

num = 1
if num > 5:
    print("5보다 크다")
    print("나는 if식에 귀속되어있음")
print("나는 위의 if 식과 상관없음")

score = 75
if score >= 90:
    print(score,"점이라서 A군요")
elif score >= 80:
    print(score,"점이라서 B군요")
elif score >= 70:
    print(score,"점이라서 C군요")
else:
    print(score,"점이라서 F군요")       

fruits = {
    "0": "사과",
    "1": "바나나",
    "2": "포도"
}
유치원 = {
    "해바라기": ["유아인","정혜인"], "장미":[], "튤립":["김태리"] 
            }
시각화 훈련 = {
    "과목": ["파이썬","깃"]
}