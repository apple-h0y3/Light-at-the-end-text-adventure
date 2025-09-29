import time
bed=time.sleep

# Print text in red
print('\033[31mWell hello there!\033[0m')

# Print text with a blue background
print('\033[44mHello World but on Blue!\033[0m')

# Print text in red with a blue background
print('\033[31m\033[44mHello World but Red on Blue!\033[0m')

print("\033[38;5;206mThis text is pink.\033[0m")
bed(3)
print("\x1b[38;5;200mThis text is pink. \033[0m")