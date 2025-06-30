import json
import argparse

def save_bytes_from_json(json_file, output_file):
    # 读取JSON文件
    with open(json_file, 'r') as f:
        data = json.load(f)

    # 提取bytes数组
    bytes_data = data['bytes']

    # 将bytes数据保存到文件
    with open(output_file, 'wb') as f:
        f.write(bytes(bytes_data))

def main():
    # 设置命令行参数
    parser = argparse.ArgumentParser(description='Extract bytes from JSON and save as a file.')
    parser.add_argument('input_file', help='Input JSON file name')
    
    args = parser.parse_args()

    # 生成输出文件名
    output_file = args.input_file.replace('.json', '_new.ogg')

    # 执行函数
    save_bytes_from_json(args.input_file, output_file)
    print(f'File saved as {output_file}')

if __name__ == '__main__':
    main()
