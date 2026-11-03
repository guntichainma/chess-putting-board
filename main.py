
chess = []
r = ['a','b','c','d','e','f','g','h'] 
c = ['8','7','6','5','4','3','2','1']
board = [[0 for _ in range(8)] for _ in range(8)]
########

while True :
     row = []
     x = input()
     if x == 'Done'  :
          break
     pr = input()
     if  pr == 'Done'  :
          break
     pc = input()
     if  pc == 'Done' :
          break
     
   
     row.append(str(x))
     row.append(str(pr))
     row.append(str(pc))
     chess.append(row)
# print(chess)

########

for i in range(len(chess)):
    for j in range(len(r)):
            if r[j] == chess[i][1]:
                chess[i][1] = j 


for i in range(len(chess)):
    for j in range(len(c)):
            if c[j] == chess[i][2]:
                chess[i][2] = j

# print(chess)


#######


for piece in chess:
    board[piece[2]][piece[1]] = piece[0]

     
        
# for i in range(8):
#      print(board[i])
               

#######

     
for i in range(8):
     print('+---+---+---+---+---+---+---+---+')
     
     
     for j in range(8):
          if board [i][j]== 0 :
            print('| ',end='')
            if (i+j)%2 == 0 :
                print('# ',end='')
            if (i+j)%2 != 0 :
                print('. ',end='') 
          else:
               print('| ',end='')
               print(board[i][j],end=' ') 
     print('|',end=' ')
     print(8-i)
print('+---+---+---+---+---+---+---+---+')
for v in r :
     print('  '+v,end=' ')