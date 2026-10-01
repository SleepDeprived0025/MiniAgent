from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")
result4 = get_file_content("calculator", "main.py")
print(result4)
result1 = get_file_content("calculator", "pkg/calculator.py")
print(result1)
result2 = get_file_content("calculator", "/bin/cat")
print(result2)
result3 = get_file_content("calculator", "pkg/does_not_exist.py")
print(result3)