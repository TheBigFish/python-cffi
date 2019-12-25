# cffi-api-mode

cffi API 模式示例

## 编译过程

- 编译动态库
  `gcc -shared -fPIC add.c -o libadd.so`
  生成 libadd.so 文件
- cffi 编译
  `python3 build_add_module.py`
  生成 _add.cpython-35m-x86_64-linux-gnu.so 文件
- 加入当前动态库路径
  `export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH`
- 测试生成文件
  `python3 add-example.py`
  两个动态库文件都要在当前目录用到

*注意*
windows 下编译失败
