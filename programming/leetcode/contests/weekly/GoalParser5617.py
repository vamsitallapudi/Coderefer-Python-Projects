class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")


print(Solution().interpret("G()()()()(al)"))
