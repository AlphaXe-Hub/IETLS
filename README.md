# IETLS word list windows notification
# 雅思单词列表窗口通知
Getting started
Installing Windows-Toasts
The latest version of Windows-Toasts requires Python 3.9 or later, and supports Windows 10 and 11.

It can be installed using pip:

启动安装Windows - Toasts最新版本的Windows - Toasts需要Python 3.9或更晚，并且支持Windows 10和11。它可以用pip安装：

``` cmd
$ python -m pip install windows-toasts
```
![image](https://github.com/user-attachments/assets/60834a43-343c-4a00-907f-d86244d1f5b7)

package
打包脚本
```python
pip install pyinstaller

 pyinstaller  --clean --console --hidden-import=winrt.windows.foundation.collections --hidden-import=winrt.windows.ui.notifications --icon=logo.ico --add-data="word.txt;." IETLS.py
```
We can Customize the word list in `word.txt`
在 `word.txt` 可自定义单词表