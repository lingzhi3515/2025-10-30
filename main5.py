# main.py

print("=== 导入整个模块并使用点号语法 ===")
import code5 as tm

celsius_temp = 25
fahrenheit_temp = 77

print(f"{celsius_temp}°C = {tm.c_to_f(celsius_temp):.2f}°F")
print(f"{fahrenheit_temp}°F = {tm.f_to_c(fahrenheit_temp):.2f}°C")

print(f"\n位置实参: 25°C 转华氏度: {tm.temperature_converter(25, 'f'):.2f}°F")

print(f"关键字实参: 77°F 转摄氏度: {tm.temperature_converter(temp=77, mode='c'):.2f}°C")


print("\n=== 只导入需要使用的函数 ===")
from code5 import c_to_f, f_to_c, calculate_sum

print(f"使用导入的函数: 0°C = {c_to_f(0):.2f}°F")
print(f"使用导入的函数: 32°F = {f_to_c(32):.2f}°C")

print(f"\n可变参数函数演示:")
print(f"1+2+3 = {calculate_sum(1, 2, 3)}")
print(f"10+20+30+40 = {calculate_sum(10, 20, 30, 40)}")


print("\n=== 导入多个特定函数 ===")
from code5 import temperature_converter, create_person_profile

print("温度转换演示:")
temps_to_convert = [0, 20, 37, 100]
for temp in temps_to_convert:
    converted = temperature_converter(temp, 'f')
    print(f"{temp}°C = {converted:.2f}°F")

print(f"\n关键字参数函数演示:")
person1 = create_person_profile("张三", 25)
print(f"p1信息: {person1}")

person2 = create_person_profile("李四", 30, city="北京", job="老师")
print(f"p2信息: {person2}")

