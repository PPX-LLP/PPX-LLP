# This is a simple notebook
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import random
import datetime
import calendar

class IconManager:
    def __init__(self, folder_path):
        self.all_images = self._load_images(folder_path)
        self.available_images = []
        self.used_images = []
        self.current_round = 0
        self.reset_images()

    def _load_images(self, folder_path):
        """加载指定文件夹中的所有图片"""
        supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
        try:
            return [
                os.path.join(folder_path, f)
                for f in os.listdir(folder_path)
                if f.lower().endswith(supported_formats)
            ]
        except Exception as e:
            messagebox.showerror("错误", f"无法加载图片: {str(e)}")
            return []

    def reset_images(self):
        """重置图片池"""
        if not self.all_images:
            return
        
        self.available_images = random.sample(self.all_images, len(self.all_images))
        self.used_images = []
        self.current_round += 1

    def get_next_icon(self, size=(32, 32)):
        """获取下一个图标"""
        if not self.available_images:
            self.reset_images()
        
        if not self.available_images:
            return None  # 无可用图片时返回空

        img_path = self.available_images.pop()
        self.used_images.append(img_path)
        
        try:
            img = Image.open(img_path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"无法加载图片 {img_path}: {str(e)}")
            return self.get_next_icon(size)  # 自动尝试下一个图片

# 初始化图标管理器（替换为你的图片路径）
icon_manager = IconManager(r"C:\Users\27411\Pictures\螈")

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        # 初始化界面
        self.setup_ui()
        self.setup_bindings()

    def setup_ui(self):
        # 创建带图标的Treeview
        self.tree = ttk.Treeview(
            self.root,
            columns=('task', 'time'),
            show='tree headings',
            height=15
        )
        
        # 配置列
        self.tree.column('#0', width=50, anchor='center')  # 图标列
        self.tree.heading('#0', text='图标')
        self.tree.column('task', width=200, anchor='w')
        self.tree.heading('task', text='任务内容')
        self.tree.column('time', width=150, anchor='center')
        self.tree.heading('time', text='时间')
        
        # 其他界面组件保持不变...
        
    def add_task(self):
        # ...原有验证逻辑...
        
        # 获取图标
        icon = icon_manager.get_next_icon()
        
        # 插入带图标的数据
        if icon:
            self.tree.insert(
                '',
                'end',
                image=icon,
                values=(task, time_str)
            )
        else:
            self.tree.insert(
                '',
                'end',
                values=(task, time_str)
            )
        
        # ...后续逻辑...

# 使用示例
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
