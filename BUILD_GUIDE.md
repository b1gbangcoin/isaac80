# Windows 版本编译指南

如果你想自己编译 Windows 版本的 EXE，请按以下步骤操作：

## 前置要求

- Windows 操作系统
- Python 3.8 或更高版本（https://www.python.org/）
- 网络连接

## 编译步骤

### 1. 下载项目
```bash
git clone https://github.com/b1gbangcoin/isaac80.git
cd isaac80
```

### 2. 运行编译脚本
在项目文件夹中，双击 `build.bat` 文件。

或者在命令行运行：
```bash
build.bat
```

### 3. 等待编译完成
编译过程会：
- 安装依赖库（Pillow, PyInstaller）
- 编译 Python 代码成 EXE
- 生成可执行文件

编译可能需要 1-3 分钟。

### 4. 获取 EXE 文件
编译完成后，可执行文件位置：
```
isaac80/dist/Isaac80.exe
```

## 常见问题

**Q: 说找不到 Python**
A: 需要安装 Python 并添加到 PATH。可以重新安装 Python，勾选 "Add Python to PATH"。

**Q: 编译很慢**
A: 首次编译会下载所有依赖，属于正常现象。之后会快一些。

**Q: 编译失败**
A: 检查错误信息，可能是：
- Python 版本过低
- 网络连接问题
- 磁盘空间不足

## 直接使用 EXE

编译完成后，可以：
1. 把 `Isaac80.exe` 复制到任何位置
2. 直接双击运行
3. 无需 Python 环境

## 分享

编译好的 EXE 可以分享给其他 Windows 用户，他们无需安装任何环境即可使用。
