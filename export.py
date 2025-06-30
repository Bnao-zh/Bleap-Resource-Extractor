import os
import json
import UnityPy

def export_bleap_files(directory, export_dir):
    os.makedirs(export_directory, exist_ok=True)
    print("📂开始导出文件到"+export_dir+"文件夹")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith('__data'):
                file_path = os.path.join(root, file)
                print("-------------------------------------------------------")
                print("📂找到文件:"+file_path)

                env = UnityPy.load(file_path)
                for obj in env.objects:
                    if obj.type.name == "TextAsset":
                        # export asset
                        data = obj.read()
                        print(f"  📄导出谱面: {data.m_Name}.txt")
                        # path = os.path.join(export_dir, f"{data.m_Name}.txt")
                        m_name = data.m_Name
                        folder_name = m_name.rsplit('_', 1)[0]
                        file_name = m_name.rsplit('_', 1)[1] + '.txt'
                        folder_path = os.path.join(export_dir, folder_name)
                        os.makedirs(folder_path, exist_ok=True)
                        path = os.path.join(folder_path, file_name)
                        with open(path, "wb") as f:
                            f.write(data.m_Script.encode("utf-8", "surrogateescape"))
                    if obj.type.name == "MonoBehaviour":
                        if obj.serialized_type.node:
                            # save decoded data
                            tree = obj.read_typetree()
                            print(f"  🗑️临时导出MonoBehaviour: {tree['m_Name']}.json")
                            fp = os.path.join(export_dir, f"{tree['m_Name']}.json")
                            with open(fp, "wt", encoding = "utf8") as f:
                                json.dump(tree, f, ensure_ascii = False, indent = 4)
                            
                            with open(fp, 'r', encoding='utf8') as f:
                                tree = json.load(f)
                            print(f"    🎵提取音频数据: {tree['m_Name']}.opus")
                            # 提取 bytes 数组
                            bytes_data = tree['bytes']
                            # 将 bytes 数据保存到文件
                            m_name = tree['m_Name']
                            folder_name = m_name.rsplit('_', 1)[0]
                            file_name = m_name.rsplit('_', 1)[1] + '.opus'
                            folder_path = os.path.join(export_dir, folder_name)
                            os.makedirs(folder_path, exist_ok=True)
                            output_file = os.path.join(folder_path, file_name)
                            with open(output_file, 'wb') as f:
                                f.write(bytes(bytes_data))
                            # 删除临时文件
                            os.remove(fp)
                    if obj.type.name == "Texture2D":
                        # export texture
                        data = obj.read()
                        print(f"  🖼️导出图片: {data.m_Name}.png")
                        # path = os.path.join(export_dir, f"{data.m_Name}.png")
                        m_name = data.m_Name
                        folder_name = m_name.rsplit('_', 1)[0]
                        file_name = m_name.rsplit('_', 1)[1] + '.png'
                        folder_path = os.path.join(export_dir, folder_name)
                        os.makedirs(folder_path, exist_ok=True)
                        path = os.path.join(folder_path, file_name)
                        data.image.save(path)
                print("-------------------------------------------------------")
    print("🎉导出完成")


if __name__ == "__main__":
    target_directory = 'ChartPackage\\CacheFiles'
    export_directory = 'export'
    print("Bleap resource extractor v1")
    export_bleap_files(target_directory, export_directory)
