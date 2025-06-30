# Bleap-Resource-Extractor
一个Bleap的资源（音频，曲绘，谱面）提取器<br>

## 安装库
使用到的库有[UnityPy](https://github.com/K0lb3/UnityPy)<br>
使用下面的命令进行安装
<pre><code>pip install unitypy</code></pre>

## ChartPackage取得方法
1：网络抓包<br>
2：MT管理器注入文件提取器后访问`/storage/提取器位置/android_data/files/package/`

## 使用
### 全部资源提取
将`export.py`放在与`ChartPackage`同一目录下<br>
然后使用下面的命令开始提取<br>
<pre><code>python3 export.py</code></pre>

### 从MonoBehaviour提取音频
将`bytes.py`放在与要提取的MonoBehaviour JSON文件同一目录下<br>
然后使用下面的命令开始提取<br>
<pre><code>python3 bytes.py [此处替换为要被提取的MonoBehaviour JSON文件名]</code></pre>
