# This is an input class. Do not edit.

def defy_ast(stack, ast):
    print("stack and astroids are", stack, ast)
    while len(stack) != 0 and stack[-1] > 0 and ast < 0:
        if abs(ast) > abs(stack[-1]):
            stack.pop()
        elif abs(ast) == abs(stack[-1]):
            stack.pop()
            return
        else:
            return
    stack.append(ast)
    return


def collidingAsteroids(asteroids):
    print(asteroids)
    stack = []
    while len(asteroids) != 0:
        ast = asteroids.pop(0)
        defy_ast(stack, ast)
        print("output of stack is", stack)

    return stack
