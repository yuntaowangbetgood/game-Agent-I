from mcp.server.fastmcp import FastMCP
from bs4 import BeautifulSoup
import urllib.request
import ssl

mcp = FastMCP(name="游戏资讯助手")

@mcp.tool(
    title="获取 Steam 热销榜",
    description="获取 Steam 实时热销游戏排行榜 Top 10",
)
async def get_steam_topsellers() -> str:
    url = "https://store.steampowered.com/search/?filter=topsellers"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    
    try:
        # 创建一个完全忽略证书验证的上下文
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(req, context=context, timeout=10) as response:
            html = response.read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            
            games = soup.select('.search_result_row .title')[:10]
            result = "🔥 Steam 实时热销榜 Top 10：\n"
            for i, game in enumerate(games):
                result += f"{i+1}. {game.text.strip()}\n"
            return result
    except Exception as e:
        return f"获取排行榜失败: {str(e)}"

@mcp.tool(
    title="获取 IGN 游戏新闻",
    description="获取游戏新闻（简易版）",
)
async def get_gaming_news() -> str:
    return "📰 最新游戏资讯：\n1. 《黑神话：悟空》发布最新补丁\n2. 《GTA 6》确认明年发售\n3. 任天堂 Switch 2 爆料汇总"

if __name__ == "__main__":
    mcp.run(transport="stdio")
