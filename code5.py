def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

def temperature_converter(temp, mode='f'):
    if mode == 'f':
        return c_to_f(temp)
    elif mode == 'c':
        return f_to_c(temp)
    else:
        raise ValueError("单位参数必须是 'f' 或 'c'")
    
def batch_temperature_converter_inplace(temps, mode='f'):
    
    for i in range(len(temps)):
        temps[i] = temperature_converter(temps[i], mode)


celsius_temp = 25
fahrenheit_temp = 77
    
print(f"{celsius_temp}°C = {c_to_f(celsius_temp):.2f}°F")
print(f"{fahrenheit_temp}°F = {f_to_c(fahrenheit_temp):.2f}°C")
    
print(f"\n=== 通用转换函数演示 ===")
print(f"25°C 转华氏度: {temperature_converter(25, 'f'):.2f}°F")
print(f"77°F 转摄氏度: {temperature_converter(77, 'c'):.2f}°C")
    
print(f"\n=== 批量转换演示（不修改原始列表）===")
original_temps = [0, 20, 37, 100]
print(f"原始温度列表: {original_temps}°C")
print(f"\n=== 避免原始列表被修改的方法 ===")
print("copy()方法复制列表，再改变复制后的列表:")
original_list = [0, 20, 37, 100]
temp_list = original_list.copy()
batch_temperature_converter_inplace(temp_list, 'f')
print(f"原始列表: {original_list}°C")
print(f"转换后列表: {[f'{temp:.2f}°F' for temp in temp_list]}")
print(f"原始列表保持不变: {original_temps}°C")
    
print(f"\n=== 批量转换演示（修改原始列表）===")
print(f"修改前列表: {original_temps}°C")
batch_temperature_converter_inplace(original_temps, 'f')
print(f"修改后列表: {[f'{temp:.2f}°F' for temp in original_temps]}")
    
def calculate_sum(*numbers):
    return sum(numbers)

print(f"1+2+3 = {calculate_sum(1, 2, 3)}")
print(f"10+20+30+40 = {calculate_sum(10, 20, 30, 40)}")
print(f"单个数字5 = {calculate_sum(5)}")
print(f"空参数 = {calculate_sum()}")

def create_person_profile(name, age, **additional_info):
    profile = {
        'name': name,
        'age': age
    }
    
    profile.update(additional_info)
    return profile

person1 = create_person_profile("张三", 25)
print(f"p1信息: {person1}")

# 包含额外信息
person2 = create_person_profile("李四", 30, city="北京", job="老师")
print(f"p2信息: {person2}")
