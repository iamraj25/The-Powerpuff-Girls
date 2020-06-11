''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    N = int(input())
    ingredient = [int(x) for x in input().split()]
    totalingredient = [int(x) for x in input().split()]
    lis = []
    for i in range(N):
        lis.append(totalingredient[i]//ingredient[i])
    print(min(lis))


main()

