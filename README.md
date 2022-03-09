# 卡牌切牌脚本

通过获取技能位置的颜色 rgb 进行切牌判断

rgb 匹配：[蓝](https://rgb-matcher.vercel.app/?r=0-205&g=0-208&b=60-255) [红](https://rgb-matcher.vercel.app/?r=79-255&g=0-54&b=0-59) [黄](https://rgb-matcher.vercel.app/?r=66-255&g=57-255&b=0-68)

## 使用

[Github Releases](https://github.com/edtam/lol-card-master/releases) 下载 exe 文件运行

## 自行修改与构建

```bash
# 安装环境
pip install pipenv
cd project
pipenv install
pipenv run py card-master.py

# 构建
pipenv run pyinstaller -F card-master.py
```
