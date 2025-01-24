import psutil

memory = psutil.virtual_memory()
print(f"Total Memory: {memory.total / (1024 ** 2):.2f} MB")
print(f"Used Memory: {memory.used / (1024 ** 2):.2f} MB")


