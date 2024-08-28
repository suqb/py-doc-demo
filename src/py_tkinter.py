# python gui
import tkinter as tk


def button_click():
    value = entry.get()
    label.config({'text': value})


# 创建主窗口
root = tk.Tk()
root.title('Tkinter Application')
root.geometry('1200x600')

# 创建标签
label = tk.Label(root, text='Hello Tkinter!')
label.config({'bg': 'red'})
label.pack()

# 创建按钮并且绑定事件监听器
button = tk.Button(root, text='Button', command=button_click)
button.config({'bg': 'green'})
button.pack()

# 文本输入框
entry = tk.Entry(root)
entry.pack()

# 文本区
text = tk.Text(root)
text.pack()

# 进入事件循环
root.mainloop()
