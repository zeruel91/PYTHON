import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v': #명령 프롬프트에서 입력할 때에는 매번 
    f = open('memo.txt')#저장을 해야 변경사항이 적용됨
    memo = f.read()
    f.close()
    print(memo)
#python memo.py -a "Life is too short"
#python memo.py -v 
