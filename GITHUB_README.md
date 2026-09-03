# 9宫格GIF合成工具

将 JPG 图片与 5 个 GIF 动画组合成 3×3 网格动画。

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 快速开始

### Windows 用户
直接下载 [Release](https://github.com/你的账户/isaac80/releases) 中的 `9宫格GIF合成工具.exe`，双击运行即可。

### Linux/Mac 用户
```bash
# 安装依赖
pip install Pillow

# 运行
python3 gui.py
# 或双击 启动GIF工具 文件
```

## 功能介绍

将输入的 JPG 图片与 5 个 GIF 动画按以下布局组合：

```
GIF1  | JPG  | GIF2
------|------|------
JPG   | GIF3 | JPG
------|------|------
GIF4  | JPG  | GIF5
```

- **GIF 位置**：循环播放对应的 GIF 动画
- **JPG 位置**：显示输入的静态图片

## 使用方法

### 图形界面（推荐）
1. 打开应用
2. 点击"选择"按钮选择 JPG 图片
3. 输出文件名会自动生成（可修改）
4. 点击"🎬 生成 GIF"
5. 等待完成提示

### 命令行
```bash
python3 ninegrid_gif.py photo.jpg
# 输出: photo_result.gif

python3 ninegrid_gif.py photo.jpg output.gif
```

## 文件说明

| 文件 | 说明 |
|------|------|
| `启动GIF工具` | Linux/Mac 启动器（推荐双击） |
| `gui.py` | 图形界面应用 |
| `ninegrid_gif.py` | 核心处理脚本 |
| `g1.gif ~ g5.gif` | 5 个 GIF 资源文件 |
| `test.jpg` | 示例输入图片 |
| `打包为EXE.bat` | Windows 打包脚本 |

## 依赖

- Python 3.7+
- Pillow
- tkinter（通常已内置）

## 自己编译 Windows 版本

如果官方没有提供最新的 Windows 版本，你可以自己编译：

1. 安装 Python 3.8+
2. 在项目目录运行：
```bash
python -m pip install pyinstaller pillow
python -m pyinstaller --onefile --windowed --name "9宫格GIF合成工具" gui.py
```
3. 编译完成后在 `dist` 文件夹中获得 EXE 文件

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 示例

**输入：** 任意 JPG 图片（如风景照、人物照等）

**输出：** 包含 5 个动画 GIF + 输入图片的 3×3 网格动画

![Example](https://your-image-url.png)
