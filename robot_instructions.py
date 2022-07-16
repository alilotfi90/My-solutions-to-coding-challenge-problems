def isRobotBounded(instructions):
        x , y , dx , dy = 0 , 0 , 0 , 1
        for i in range(len(instructions)):
            #print(instructions[i])
            if instructions[i]=='G':
                x , y=x+dx , y+dy
            elif instructions[i]=='L':
                dy , dx=dx , -dy
            else:
                dy , dx=-dx , dy
        return (x,y)==(0,0) or dy!=1
def main():
    instructions="GLGLGLLL"
    print(isRobotBounded(instructions))
if __name__ == "__main__":
  main()