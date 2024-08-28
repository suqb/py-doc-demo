import os
import shutil
import subprocess

path = '../file.txt'


#  创建文件
def create_file(filepath):
    if not os.path.exists(filepath):
        open(filepath, 'w').close()
        print(f'文件{filepath}创建成功')
    else:
        print(f'文件{filepath} 已存在')


# 删除文件
def delete_file(filepath, delete_type):
    if delete_type == 'os':
        # os模块适用于删除单个文件或空目录
        os.remove(filepath)
        os.unlink(filepath)
        # 执行系统命令删除文件、依赖于操作系统
        os.system(f'rm {filepath}')
    elif delete_type == 'shutil':
        # shutil适用于删除目录下的所有文件及其子目录
        shutil.rmtree(filepath)
    elif delete_type == 'other':
        # 外部命令
        subprocess.call(f'rm {filepath}')


# 文件读取
def read_file(filepath, read_type):
    # r：只读（默认） w：只写 a：追加 b：二进制 t：文本（默认）
    with open(filepath, 'r', encoding='utf-8') as file:
        if read_type == 'line':
            # 读取行
            for line in file:
                print(line)
        elif read_type == 'content':
            # 读取整个文件
            file_content = file.read()
            print(file_content)
        elif read_type == 'character':
            # 读取指定字节、字符，如果以打开方式为二进制则读取的是10个字节
            read = file.read(10)
            print(read)


# 文件写入
def write_file(filepath, write_type, content):
    with open(filepath, 'w', encoding='utf-8') as file:
        if write_type == 'str':
            file.write(content + '\n')
        elif write_type == 'byte':
            # 这个版本好像写不了字节数据
            file.write(content.encode('utf-8'))
        elif write_type == 'list':
            # 写入list内容不会在元素之间自动添加换行符
            file.writelines(content)


# 文件移动或重命名
def move_file(origin, target):
    # target 可以是/target_folder也可以是/target_folder/new_file.txt, 可重命名文件,需要目标文件夹存在
    shutil.move(origin, target)


# 文件复制
def copy_file(origin, target, copy_type):
    if copy_type == 'copy':
        # 和文件移动基本一致
        shutil.copy(origin, target)
    elif copy_type == 'copyfile':
        # 移动文件，并且要求目标他位置有写入权限
        shutil.copyfile(origin, target)
    elif copy_type == 'copy2':
        # 在复制数据时获取元数据中添加的访问和修改时间。复制相同的文件会导致 SameFileError 异常
        shutil.copy2(origin, target)



