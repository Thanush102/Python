n=4
for i in range(0,n+1):
    spaces= " "*((n-i))
    stars = "* "*(i)
    print(spaces+stars)
for i in range(0,n+1):
    spaces= " "*((i))
    stars = "* "*(n-i)
    print(spaces+stars)


#OUTPUT
#   * 
#  * * 
# * * * 
#* * * * 
#* * * * 
# * * * 
#  * * 
#   * 
