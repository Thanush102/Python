n=int(input("Enter n value:"))
spaces = ' '
star = '*'
print(spaces*n+star)

for i in range(n-1,0,-1):
    print(spaces*(i)+star+spaces*(2*(n-i)-1)+star)
for j in range(2,n):
    print(spaces*(j)+star+(spaces*(2*(n-j)-1))+star)
print(spaces*n+star)

#OUTPUT
#Enter n value:6
#      *
#     * *
#    *   *
#   *     *
#  *       *
# *         *
#  *       *
#   *     *
#    *   *
#     * *
#      *
