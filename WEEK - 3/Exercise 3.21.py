n=5
for i in range(1,n+1):
    spaces= " "*(i+1)
    stars = "* "*(n-i+1)
    print(spaces+stars)

#OUTPUT
#  * * * * * 
#   * * * * 
#    * * * 
#     * * 
#      * 
