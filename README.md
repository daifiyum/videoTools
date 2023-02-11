# videoTools
一个处理视频的小工具

![demo](https://s1.ax1x.com/2023/02/11/pS4AFHI.png)

### 准备环境（pipenv）

本程序采用虚拟环境

注意：提前全局安装pipenv包

```
# 下面安装命令都在虚拟环境外操作，安装包时就会自动给你创建虚拟环境

快速搭建运行环境（不包含dev环境）
pipenv install

必要所需安装
pipenv install pyside6

dev开发所需安装
pipenv install nuitka --dev
```

### 运行程序

虚拟环境外部运行

```
pipenv run python app.py
```

虚拟环境内部运行（进入虚拟环境内部）

```
pipenv shell

python app.py

# 退出虚拟环境
exit
```

### 其他

**虚拟环境修改pip源**

进入Pipfile文件内修改默认源

### 打包

**auto-py-to-exe打包**
运行 auto-py-to-exe 打开图形化打包界面进行配置打包

**nuitka打包（推荐）**

注意：需提前安装mingw64（本项目使用GCC 11.3.0）最新版

```
nuitka --mingw64 --standalone --show-memory --show-progress --nofollow-imports --plugin-enable=pyside6 --windows-disable-console --output-dir=out --windows-icon-from-ico=./app.ico --include-data-dir=./assets=./assets .\app.py
```
