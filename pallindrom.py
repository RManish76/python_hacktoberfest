# def pallindrom(line):
#     line=list(line)
#     low = 0
#     high = len(line)-1
#     while(low<high):
#         temp=line[low]
#         line[low]=line[high]
#         line[high]=temp
#         low+=1
#         high-=1
#     line = '' . join(line)
#     return(line)
# # Driver code 
# if __name__ == '__main__' : 
	
# 	s = input()
# 	print(1) if(s==pallindrom(s)) else print(0)
s=input()
s=list(s)
temp=s.copy()
s.reverse()
print(1) if(s==temp) else print(0)