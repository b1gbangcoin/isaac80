import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import threading
from ninegrid_gif import make_nine_grid_gif

class NineGridGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Isaac80")
        self.root.geometry("550x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        # 标题
        title_label = tk.Label(root, text="Isaac80", font=("Arial", 16, "bold"))
        title_label.pack(pady=20)

        # 输入文件选择
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10, padx=20, fill=tk.X)

        tk.Label(input_frame, text="输入 JPG 文件:", font=("Arial", 10)).pack(side=tk.LEFT)
        self.input_path = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.input_path, width=35, state=tk.DISABLED).pack(side=tk.LEFT, padx=10)
        tk.Button(input_frame, text="选择", command=self.select_input).pack(side=tk.LEFT)

        # 输出文件选择
        output_frame = tk.Frame(root)
        output_frame.pack(pady=10, padx=20, fill=tk.X)

        tk.Label(output_frame, text="输出 GIF 文件:", font=("Arial", 10)).pack(side=tk.LEFT)
        self.output_path = tk.StringVar()
        tk.Entry(output_frame, textvariable=self.output_path, width=35, state=tk.DISABLED).pack(side=tk.LEFT, padx=10)
        tk.Button(output_frame, text="选择", command=self.select_output).pack(side=tk.LEFT)

        # 预览区域
        preview_frame = tk.LabelFrame(root, text="9宫格布局", font=("Arial", 10), padx=10, pady=10)
        preview_frame.pack(pady=15, padx=20, fill=tk.BOTH, expand=True)

        preview_text = """GIF1  │ JPG  │ GIF2
──────┼──────┼──────
JPG   │ GIF3 │ JPG
──────┼──────┼──────
GIF4  │ JPG  │ GIF5"""
        tk.Label(preview_frame, text=preview_text, font=("Courier", 9), justify=tk.CENTER).pack()

        # 进度标签
        self.status_label = tk.Label(root, text="准备就绪", font=("Arial", 10, "bold"), fg="green")
        self.status_label.pack(pady=8)

        # 按钮
        button_frame = tk.Frame(root)
        button_frame.pack(pady=15)

        self.generate_btn = tk.Button(
            button_frame,
            text="🎬 生成 GIF",
            command=self.generate,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            width=18,
            height=2,
            relief=tk.RAISED,
            bd=2,
            cursor="hand2"
        )
        self.generate_btn.pack(side=tk.LEFT, padx=8)

        tk.Button(
            button_frame,
            text="❌ 退出",
            command=root.quit,
            bg="#f44336",
            fg="white",
            font=("Arial", 12, "bold"),
            width=18,
            height=2,
            relief=tk.RAISED,
            bd=2,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=8)

    def select_input(self):
        file_path = filedialog.askopenfilename(
            title="选择输入 JPG 文件",
            filetypes=[("JPEG 文件", "*.jpg"), ("JPEG 文件", "*.jpeg"), ("所有文件", "*.*")],
            initialdir=self.script_dir
        )
        if file_path:
            self.input_path.set(file_path)
            if not self.output_path.get():
                default_output = os.path.splitext(file_path)[0] + "_result.gif"
                self.output_path.set(default_output)

    def select_output(self):
        file_path = filedialog.asksaveasfilename(
            title="选择输出 GIF 文件",
            filetypes=[("GIF 文件", "*.gif"), ("所有文件", "*.*")],
            initialdir=self.script_dir,
            defaultextension=".gif"
        )
        if file_path:
            self.output_path.set(file_path)

    def generate(self):
        input_file = self.input_path.get()
        output_file = self.output_path.get()

        if not input_file:
            messagebox.showerror("错误", "请选择输入 JPG 文件")
            return

        if not output_file:
            messagebox.showerror("错误", "请选择输出 GIF 文件")
            return

        if not os.path.exists(input_file):
            messagebox.showerror("错误", f"输入文件不存在: {input_file}")
            return

        gif_files = [
            os.path.join(self.script_dir, "g1.gif"),
            os.path.join(self.script_dir, "g2.gif"),
            os.path.join(self.script_dir, "g3.gif"),
            os.path.join(self.script_dir, "g4.gif"),
            os.path.join(self.script_dir, "g5.gif")
        ]

        for g in gif_files:
            if not os.path.exists(g):
                messagebox.showerror("错误", f"找不到 GIF 文件: {g}")
                return

        self.generate_btn.config(state=tk.DISABLED)
        self.status_label.config(text="处理中...", fg="blue")

        thread = threading.Thread(target=self._generate_thread, args=(gif_files, input_file, output_file))
        thread.start()

    def _generate_thread(self, gif_files, input_file, output_file):
        try:
            make_nine_grid_gif(gif_files, input_file, output_file, cell_size=200)
            self.root.after(0, lambda: self._on_success(output_file))
        except Exception as e:
            self.root.after(0, lambda: self._on_error(str(e)))

    def _on_success(self, output_file):
        self.generate_btn.config(state=tk.NORMAL)
        self.status_label.config(text="✓ 生成成功!", fg="green")
        messagebox.showinfo("成功", f"GIF 已生成:\n{output_file}")

    def _on_error(self, error):
        self.generate_btn.config(state=tk.NORMAL)
        self.status_label.config(text="✗ 生成失败", fg="red")
        messagebox.showerror("错误", f"生成失败:\n{error}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = NineGridGUI(root)
    root.mainloop()
