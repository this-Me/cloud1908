# usage: for cycle
# date: 2019/11/18
# filepath: cloud1908/01.oneday/04.forcycle.py


# shell for
# for i in {1..100};do
#   echo ${i}
# done

# python for: range就是产生自然数的区间: 特点: 左闭右开区间
for i in range(100):
    print(-i)

# 1-100中所有的偶数
for n in range(1, 101):
    if n % 2 == 0:
        print(n)

# while cycle:
n = 0
while n <= 100:
    print(n)
    n += 1

