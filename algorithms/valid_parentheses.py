class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # Создаём словарь с парами скобок
        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            # Если текущий символ — это закрывающая скобка
            if char in mapping:
                # Извлекаем верхний элемент стека, если он не пуст, иначе назначаем переменной `top_element` значение #
                top_element = stack.pop() if stack else '#'
                # Если верхний элемент стека не соответствует правильной открывающей скобке, возвращаем False
                if mapping[char] != top_element:
                    return False
            else:
                # Если это открывающая скобка, добавляем её в стек
                stack.append(char)

        # Если после прохождения всей строки стек пуст, возвращаем True

        return not stack


valid_collection = ("()",  # True
                    "()[]{}",  # True
                    "(]",  # False
                    "([])",  # True
                    "([)]",  # False
                    "([{}])",  # True
                    "([{}]())",  # True
                    "([{}]())()",  # True
                    "([{}]())(",  # False
                    )

do = Solution()
for my_str in valid_collection:
    result = do.isValid(my_str)
    print(f"{my_str}={result}")
