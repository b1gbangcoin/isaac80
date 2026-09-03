# Isaac80 - 九宫格 GIF 合成工具

一个强大而简单的工具，可以将任意 JPG/PNG 图片与 5 个 GIF 动画组合成高质量的 3×3 网格动画。

## 特性

✨ **简单易用**
- 直观的图形化界面
- 一键生成动画
- 无需编程知识

🎬 **灵活组合**
- 支持任意 JPG/PNG 作为中心图片
- 5 个可自定义的 GIF 动画位置
- 自动适配不同大小的输入

⚡ **高性能**
- 快速处理，即时反馈
- 生成高质量 GIF 动画
- 支持无限循环播放

🔧 **跨平台**
- Windows / Linux / Mac 完全支持
- 无需安装依赖（Windows EXE 版本）
- 开源免费

## 快速开始

### Windows 用户（推荐）
1. 从 [Release](https://github.com/b1gbangcoin/isaac80/releases) 下载 `Isaac80.exe`
2. 双击运行
3. 选择图片 → 点击"生成 GIF" → 完成

### Linux/Mac 用户
```bash
git clone https://github.com/b1gbangcoin/isaac80.git
cd isaac80
pip install Pillow
python3 gui.py
```

## 使用指南

### 图形界面操作

1. **启动应用**
   - Windows：双击 `Isaac80.exe`
   - Linux/Mac：运行 `python3 gui.py`

2. **选择图片**
   - 点击第一个"选择"按钮
   - 选择任意 JPG 或 PNG 文件

3. **设置输出文件**
   - 输出文件名会自动生成
   - 可点击第二个"选择"修改输出位置

4. **生成 GIF**
   - 点击"🎬 生成 GIF"按钮
   - 等待处理完成

5. **查看结果**
   - 输出 GIF 文件保存到指定位置
   - 可用任何图片查看器打开

### 命令行操作

```bash
# 简单模式（自动生成输出名）
python3 ninegrid_gif.py photo.jpg

# 指定输出文件名
python3 ninegrid_gif.py photo.jpg my_animation.gif
```

## 9宫格布局说明

程序使用以下布局组合图片：

```
GIF1  | JPG  | GIF2
------|------|------
JPG   | GIF3 | JPG
------|------|------
GIF4  | JPG  | GIF5
```

**各部分说明：**
- **GIF 位置**（角落 + 中心）：循环播放对应的 GIF 动画
- **JPG 位置**（十字方向）：显示输入的静态图片
- **总尺寸**：600×600 像素（5 个单元格，每个 200×200）
- **动画帧率**：100ms 每帧
- **循环方式**：无限循环

## 技术规格

| 项目 | 规格 |
|------|------|
| 输出格式 | GIF 动画 |
| 单元格大小 | 200×200 像素 |
| 总尺寸 | 600×600 像素 |
| 帧率 | 100ms/帧 |
| 色彩深度 | RGBA |
| 循环方式 | 无限循环 |

## 文件说明

| 文件 | 说明 |
|------|------|
| `Isaac80.exe` | Windows 可执行文件（推荐使用） |
| `gui.py` | 图形界面源代码 |
| `ninegrid_gif.py` | 核心 GIF 合成引擎 |
| `g1.gif ~ g5.gif` | 5 个预设 GIF 动画资源 |
| `build.bat` | Windows EXE 编译脚本 |
| `BUILD_GUIDE.md` | 详细编译指南 |
| `启动GIF工具` | Linux/Mac 启动脚本 |

## 系统要求

**Windows 版本（EXE）**
- Windows 7 或更高版本
- 30 MB 磁盘空间
- 无需额外依赖

**源代码版本**
- Python 3.7+
- Pillow 库
- tkinter（通常已内置）

## 常见问题

**Q: 能否修改中心的 GIF 动画？**
A: 可以。替换 `g1.gif ~ g5.gif` 文件即可，只需保持相同的文件名。

**Q: 输出的 GIF 文件太大？**
A: 输出大小取决于输入图片质量和 GIF 帧数。可以：
- 压缩输入图片
- 使用在线 GIF 压缩工具
- 减少 GIF 帧数

**Q: 能否改变输出尺寸？**
A: 可以。编辑源代码中的 `cell_size=200` 参数，改为其他数值即可。

**Q: 支持其他图片格式吗？**
A: 支持所有 PIL 支持的格式，包括 JPG、PNG、BMP、TIFF 等。

**Q: 能否自定义单元格排列？**
A: 可以。编辑 `ninegrid_gif.py` 中的 `pos_map` 参数即可。

## 示例

### 输入
- 一张风景照或人物照：`photo.jpg`
- 5 个 GIF 动画：`g1.gif ~ g5.gif`

### 输出
- 包含组合效果的 GIF 动画：`photo_result.gif`

## 许可证

MIT License - 可自由使用、修改和分发

## 贡献

欢迎提交 Issue 和 Pull Request！

## 更新日志

**v1.0.0 (2026-09-03)**
- 首个正式版本
- 完整的图形界面
- Windows EXE 预编译版本
- 跨平台支持
- 详细文档和编译指南

## 相关链接

- GitHub 仓库：https://github.com/b1gbangcoin/isaac80
- 问题反馈：https://github.com/b1gbangcoin/isaac80/issues
- Release 下载：https://github.com/b1gbangcoin/isaac80/releases
