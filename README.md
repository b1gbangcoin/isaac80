## 9宫格 GIF 合成工具

将 JPG 图片与 5 个 GIF 动画组合成 3×3 网格动画。

### 使用方法

**最简单：双击 `启动GIF工具` 文件**

或在终端运行：
```bash
python3 gui.py
```

### 操作步骤

1. 点击"选择"选择一张 JPG 图片
2. 输出文件名会自动生成（可修改）
3. 点击"🎬 生成 GIF"
4. 完成！

### 9宫格布局

```
GIF1  | JPG  | GIF2
------|------|------
JPG   | GIF3 | JPG
------|------|------
GIF4  | JPG  | GIF5
```

### 依赖

- Python 3
- Pillow（`pip install Pillow`）
- tkinter（通常已内置）

### 文件说明

- `启动GIF工具` - 图形界面启动器（推荐双击使用）
- `gui.py` - GUI 应用
- `ninegrid_gif.py` - 核心处理脚本
- `g1.gif ~ g5.gif` - 固定的 5 个 GIF 资源
- `test.jpg` - 示例输入图片
