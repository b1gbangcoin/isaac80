# Isaac80 - 九宫格 GIF 合成工具

一个强大而简单的工具，可以将任意 JPG/PNG 图片与 5 个 GIF 动画组合成高质量的 3×3 网格动画。

![Release](https://img.shields.io/badge/version-v1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey)

## ✨ 特性

- **简单易用** - 直观的图形化界面，一键生成动画
- **灵活组合** - 支持任意 JPG/PNG 图片与 5 个 GIF 组合
- **高性能** - 快速处理，生成高质量 GIF 动画
- **跨平台** - 完全支持 Windows、Linux、Mac
- **开源免费** - MIT 许可证，完全开源

## 🚀 快速开始

### Windows 用户（推荐）

1. 从 [Release](https://github.com/b1gbangcoin/isaac80/releases) 下载 `Isaac80.exe`
2. 双击运行
3. 选择图片 → 生成 GIF

### Linux/Mac 用户

```bash
git clone https://github.com/b1gbangcoin/isaac80.git
cd isaac80
pip install Pillow
python3 gui.py
```

## 📖 使用指南

### 图形界面

1. **启动应用**
   - 双击 `Isaac80.exe`（Windows）
   - 运行 `python3 gui.py`（Linux/Mac）

2. **选择图片**
   - 点击"选择"按钮
   - 选择任意 JPG 或 PNG 文件

3. **生成 GIF**
   - 点击"🎬 生成 GIF"
   - 等待处理完成

### 命令行

```bash
# 自动生成输出名
python3 ninegrid_gif.py photo.jpg

# 指定输出文件名
python3 ninegrid_gif.py photo.jpg output.gif
```

## 🎬 9宫格布局

```
GIF1  | JPG  | GIF2
------|------|------
JPG   | GIF3 | JPG
------|------|------
GIF4  | JPG  | GIF5
```

- **GIF 位置**：循环播放对应的 GIF 动画
- **JPG 位置**：显示输入的静态图片
- **总尺寸**：600×600 像素

## 📋 技术规格

| 项目 | 规格 |
|------|------|
| 输出格式 | GIF 动画 |
| 单元格大小 | 200×200 像素 |
| 总尺寸 | 600×600 像素 |
| 帧率 | 100ms/帧 |
| 循环方式 | 无限循环 |

## 📦 文件说明

| 文件 | 说明 |
|------|------|
| `Isaac80.exe` | Windows 可执行文件 |
| `gui.py` | 图形界面源代码 |
| `ninegrid_gif.py` | 核心 GIF 合成引擎 |
| `g1.gif ~ g5.gif` | 5 个 GIF 动画资源 |
| `build.bat` | Windows 编译脚本 |
| `BUILD_GUIDE.md` | 详细编译指南 |

## 💻 系统要求

**Windows 版本（EXE）**
- Windows 7 或更高版本
- 30 MB 磁盘空间
- 无需额外依赖

**源代码版本**
- Python 3.7+
- Pillow 库
- tkinter（通常已内置）

## ❓ 常见问题

**Q: 能否修改中心的 GIF？**
A: 可以。替换 `g1.gif ~ g5.gif` 文件即可。

**Q: 输出文件太大？**
A: 可以压缩输入图片或减少 GIF 帧数。

**Q: 支持其他格式吗？**
A: 支持所有 PIL 支持的格式（JPG、PNG、BMP 等）。

**Q: 怎样自己编译 EXE？**
A: 参考 `BUILD_GUIDE.md` 文件的详细说明。

## 📝 许可证

MIT License - 可自由使用、修改和分发

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📚 更新日志

**v1.0.0 (2026-09-03)**
- 首个正式版本
- 完整的 GUI 界面
- Windows EXE 预编译版本
- 跨平台支持
- 详细文档

## 🔗 链接

- [GitHub 仓库](https://github.com/b1gbangcoin/isaac80)
- [Release 下载](https://github.com/b1gbangcoin/isaac80/releases)
- [问题反馈](https://github.com/b1gbangcoin/isaac80/issues)

---

Made with ❤️ by b1gbangcoin
