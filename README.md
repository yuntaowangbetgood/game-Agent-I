# game-Agent-I
基于开源 MCP 框架和大模型 API（DeepSeek），搭建的一个能用自然语言对话的智能小助手。你只要打字让它查东西，它就会自动去网上抓取 Steam 最新的热销游戏榜单并告诉你
基础版 其它功能正在更新（自动定时抓取游戏销量及相关新闻）
## 🚀 运行演示
<img width="1096" height="537" alt="image" src="https://github.com/user-attachments/assets/0e74d899-7cc2-4328-bbc8-a4ca7703a3d1" />
# 🎮 全球游戏动态监控 Agent (Game Monitor Agent)

基于开源 MCP 框架与大模型 API（DeepSeek）构建的轻量级智能助手。用户通过自然语言对话，即可让 AI 自动调用本地工具抓取 Steam 实时热销榜单，并生成结构化报告。

## ✨ 项目功能
- **大模型驱动**：接入 DeepSeek API，实现自然语言意图识别。
- **工具自动调用**：利用 MCP 协议，让 AI 自主决定何时使用外部工具。
- **实时数据抓取**：成功解决网络证书拦截，精准爬取 Steam 商店热销 Top 10 数据。

## 🛠️ 技术栈
- Python 3.15
- Model Context Protocol (MCP)
- DeepSeek API / Anthropic SDK
- BeautifulSoup / urllib

## 💻 如何运行
1. 克隆仓库并安装依赖：
   ```bash
   pip install -r requirements.txt
  2 配置环境变量：
复制 .env.example 为 .env，并填入你自己的 API Key。
3 python client.py
