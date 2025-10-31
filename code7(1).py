def show_todo():
    with open('todo.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def add_todo(task):
    with open('todo.txt', 'a', encoding='utf-8') as f:
        f.write(f"[ ] {task}\n")

def del_todo(num):
    with open('todo.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open('todo.txt', 'w', encoding='utf-8') as f:
        for i, line in enumerate(lines, 1):
            if i != num:
                f.write(line)


if __name__ == "__main__":
    with open('todo.txt', 'a', encoding='utf-8') as f:
        pass
    add_todo("完成上次实验报告")
    add_todo("买牛奶")
    add_todo("跑步半小时")
    show_todo()
    add_todo("这是一个新任务")
    show_todo()
    del_todo(4)
    show_todo()
    print("任务已删除")