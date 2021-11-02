
# 任务1：使用命令行登录指定的Linux环境
任务要点：ssh登录、密码输入、环境配置
步骤1：配置本地登录环境
本地是win10系统，使用的是MobaXterm这款SSH工具
步骤2：登录Linux系统
![image.png](imgs/1.png)


# 任务2：在目录下创建文件夹、删除文件夹
任务要点：创建文件夹、创建文件、删除文件、删除文件夹

步骤1：学习[Linux的目录结构](https://www.runoob.com/linux/linux-system-contents.html)
```
cd /
ls
```
![image.png](imgs/2.png)

步骤2：学习[Linux的文件和目录管理](https://www.runoob.com/linux/linux-file-content-manage.html)

常见的处理目录的命令：
```
ls（英文全拼：list files）: 列出目录及文件名

cd（英文全拼：change directory）：切换目录

pwd（英文全拼：print work directory）：显示目前的目录

mkdir（英文全拼：make directory）：创建一个新的目录

rmdir（英文全拼：remove directory）：删除一个空的目录

cp（英文全拼：copy file）: 复制文件或目录

rm（英文全拼：remove）: 删除文件或目录

mv（英文全拼：move file）: 移动文件与目录，或修改文件与目录的名称
```

步骤3：在/home/coggle目录下，新建一个以你英文昵称（中间不要有空格哦）的文件夹A在文件夹A内部创建一个以coggle命令的文件夹B
```
mkdir leigang
cd leigang
mkdir coggle
```
步骤4：在B文件夹内创建一个空txt文件
```
cd coggle
vi 1.txt
```

步骤5：删除步骤4创建的文件
```
rm 1.txt
```
步骤6：删除文件夹B，然后删除文件夹A
```
cd ../
rmdir coggle
cd ../
rmdir leigang
```

# 任务3：在目录下下载文件、阅读文件

任务要点：下载文件、移动文件、阅读文件

步骤1：在home目录下，新建一个以你英文昵称（中间不要有空格哦）的文件夹A在文件夹A内部创建一个以coggle命令的文件夹B
```
mkdir leigang
cd leigang
mkdir coggle
cd coggle
```
步骤2：使用wget命令下载https://mirror.coggle.club/dataset/affairs.txt，到文件夹Bwget教程：https://www.cnblogs.com/pretty-ru/p/10936023.html
```
wget https://mirror.coggle.club/dataset/affairs.txt
```

步骤3：使用head、cat、tail命令阅读下载的文件。阅读文件基础教程：https://www.cnblogs.com/jixp/p/10833801.html
```
head -n 10 affairs.txt   # head:只看开头几行
cat affairs.txt          # cat:由第一行开始显示文件内容
tail -n 10 affairs.txt   # tail: 只看结尾几行
```

步骤4：在命令行使用ipython进入python3环境，并使用pandas读取下载的文件。
```python
import pandas as pd
txt = pd.read_csv('affairs.txt',header=None)
print(txt)
```

# 任务4：在目录下使用vi或vim编辑文件
任务要点：vi和vim使用

步骤1：学习Nano的使用，https://blog.csdn.net/junxieshiguan/article/details/84104912
```
nano nanopyton.py
```
步骤2：学习Vim的使用，https://www.runoob.com/linux/linux-vim.html
```
vi vipython.py
```
步骤3：分别使用Nano和Vim创建py文件，并输入以下内容，并运行Python
```python
#!/usr/bin/env python3
print('Hello World!')
```

