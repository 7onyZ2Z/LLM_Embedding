# load_data.py

def load_text(file_path):
    """
    从指定文件中读取文本内容。
    :param file_path: 文件路径
    :return: 文本内容字符串
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print("Finished loading.")
            return file.read()
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
        return None
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return None