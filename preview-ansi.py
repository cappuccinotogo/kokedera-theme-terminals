#!/usr/bin/env python3
"""Show the installed terminal palette without changing its configuration."""
for row in range(2):
    for col in range(8):
        index = row * 8 + col
        print(f"\033[48;5;{index}m  {index:2}  \033[0m", end=" ")
    print()
print("\nNormal text   \033[1mBold text\033[0m   \033[3mItalic text\033[0m")
for index in range(16):
    print(f"\033[38;5;{index}mColor {index:2}: The moss garden rests in quiet light.\033[0m")
