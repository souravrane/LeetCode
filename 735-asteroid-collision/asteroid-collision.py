class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()
        for num in asteroids:
            stack.append(num)
            while len(stack) > 1:
                if stack[-1] * stack[-2] > 0: break
                if stack[-1] > 0 and stack[-2] < 0: break
                a1, a2 = stack.pop(), stack.pop()
                if abs(a1) > abs(a2): stack.append(a1)
                elif abs(a2) > abs(a1): stack.append(a2)
        return stack
        