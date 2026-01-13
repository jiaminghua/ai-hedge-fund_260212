"""Constants and utilities related to analysts configuration."""

from src.agents import portfolio_manager
from src.agents.aswath_damodaran import aswath_damodaran_agent
from src.agents.ben_graham import ben_graham_agent
from src.agents.bill_ackman import bill_ackman_agent
from src.agents.cathie_wood import cathie_wood_agent
from src.agents.charlie_munger import charlie_munger_agent
from src.agents.fundamentals import fundamentals_analyst_agent
from src.agents.michael_burry import michael_burry_agent
from src.agents.phil_fisher import phil_fisher_agent
from src.agents.peter_lynch import peter_lynch_agent
from src.agents.sentiment import sentiment_analyst_agent
from src.agents.stanley_druckenmiller import stanley_druckenmiller_agent
from src.agents.technicals import technical_analyst_agent
from src.agents.valuation import valuation_analyst_agent
from src.agents.warren_buffett import warren_buffett_agent
from src.agents.rakesh_jhunjhunwala import rakesh_jhunjhunwala_agent
from src.agents.mohnish_pabrai import mohnish_pabrai_agent
from src.agents.news_sentiment import news_sentiment_agent
from src.agents.growth_agent import growth_analyst_agent

# Define analyst configuration - single source of truth
ANALYST_CONFIG = {
    "aswath_damodaran": {
        "display_name": "阿斯瓦斯·达莫达兰",
        "description": "估值学院长",
        "investing_style": "专注于内在价值和财务指标，通过严谨的估值分析评估投资机会。",
        "agent_func": aswath_damodaran_agent,
        "type": "analyst",
        "order": 0,
    },
    "ben_graham": {
        "display_name": "本杰明·格雷厄姆",
        "description": "价值投资之父",
        "investing_style": "强调安全边际，通过系统性价值分析投资于基本面强劲的被低估公司。",
        "agent_func": ben_graham_agent,
        "type": "analyst",
        "order": 1,
    },
    "bill_ackman": {
        "display_name": "比尔·阿克曼",
        "description": "激进投资者",
        "investing_style": "通过战略激进主义和逆向投资立场，寻求影响管理层并释放价值。",
        "agent_func": bill_ackman_agent,
        "type": "analyst",
        "order": 2,
    },
    "cathie_wood": {
        "display_name": "凯西·伍德",
        "description": "成长投资女王",
        "investing_style": "专注于颠覆性创新和成长，投资于引领技术进步和市场颠覆的公司。",
        "agent_func": cathie_wood_agent,
        "type": "analyst",
        "order": 3,
    },
    "charlie_munger": {
        "display_name": "查理·芒格",
        "description": "理性思考者",
        "investing_style": "倡导价值投资，专注于优质企业和长期增长，通过理性决策。",
        "agent_func": charlie_munger_agent,
        "type": "analyst",
        "order": 4,
    },
    "michael_burry": {
        "display_name": "迈克尔·伯里",
        "description": "大空头逆向投资者",
        "investing_style": "进行逆向押注，经常做空被高估的市场，并通过深入基本面分析投资于被低估的资产。",
        "agent_func": michael_burry_agent,
        "type": "analyst",
        "order": 5,
    },
    "mohnish_pabrai": {
        "display_name": "莫尼什·帕伯莱",
        "description": "Dhandho投资者",
        "investing_style": "专注于价值投资和长期增长，通过基本面分析和安全边际。",
        "agent_func": mohnish_pabrai_agent,
        "type": "analyst",
        "order": 6,
    },
    "peter_lynch": {
        "display_name": "彼得·林奇",
        "description": "10倍股投资者",
        "investing_style": "投资于业务模式易于理解且具有强劲增长潜力的公司，使用'买你所知道'的策略。",
        "agent_func": peter_lynch_agent,
        "type": "analyst",
        "order": 6,
    },
    "phil_fisher": {
        "display_name": "菲尔·费舍尔",
        "description": "闲聊投资者",
        "investing_style": "强调投资于管理强大和产品创新的公司，通过闲聊研究专注于长期增长。",
        "agent_func": phil_fisher_agent,
        "type": "analyst",
        "order": 7,
    },
    "rakesh_jhunjhunwala": {
        "display_name": "拉凯什·朱恩贾拉",
        "description": "印度大牛市",
        "investing_style": "利用宏观经济洞察投资于高增长行业，特别是新兴市场和国内机会。",
        "agent_func": rakesh_jhunjhunwala_agent,
        "type": "analyst",
        "order": 8,
    },
    "stanley_druckenmiller": {
        "display_name": "斯坦利·德鲁肯米勒",
        "description": "宏观投资者",
        "investing_style": "专注于宏观经济趋势，通过自上而下分析对货币、商品和利率进行大额押注。",
        "agent_func": stanley_druckenmiller_agent,
        "type": "analyst",
        "order": 9,
    },
    "warren_buffett": {
        "display_name": "沃伦·巴菲特",
        "description": "奥马哈先知",
        "investing_style": "通过价值投资和长期持有，寻求具有强劲基本面和竞争优势的公司。",
        "agent_func": warren_buffett_agent,
        "type": "analyst",
        "order": 10,
    },
    "technical_analyst": {
        "display_name": "技术分析师",
        "description": "图表模式专家",
        "investing_style": "专注于图表模式和市场趋势，经常使用技术指标和价格行为分析做出投资决策。",
        "agent_func": technical_analyst_agent,
        "type": "analyst",
        "order": 11,
    },
    "fundamentals_analyst": {
        "display_name": "基本面分析师",
        "description": "财务报表专家",
        "investing_style": "深入研究财务报表和经济指标，通过基本面分析评估公司的内在价值。",
        "agent_func": fundamentals_analyst_agent,
        "type": "analyst",
        "order": 12,
    },
    "growth_analyst": {
        "display_name": "成长分析师",
        "description": "成长专家",
        "investing_style": "分析增长趋势和估值，通过增长分析识别增长机会。",
        "agent_func": growth_analyst_agent,
        "type": "analyst",
        "order": 13,
    },
    "news_sentiment_analyst": {
        "display_name": "新闻情绪分析师",
        "description": "新闻情绪专家",
        "investing_style": "分析新闻情绪以预测市场走势，并通过新闻分析识别机会。",
        "agent_func": news_sentiment_agent,
        "type": "analyst",
        "order": 14,
    },
    "sentiment_analyst": {
        "display_name": "市场情绪分析师",
        "description": "市场情绪专家",
        "investing_style": "衡量市场情绪和投资者行为，通过行为分析预测市场走势并识别机会。",
        "agent_func": sentiment_analyst_agent,
        "type": "analyst",
        "order": 15,
    },
    "valuation_analyst": {
        "display_name": "估值分析师",
        "description": "公司估值专家",
        "investing_style": "专注于确定公司的公允价值，使用各种估值模型和财务指标进行投资决策。",
        "agent_func": valuation_analyst_agent,
        "type": "analyst",
        "order": 16,
    },
}

# Derive ANALYST_ORDER from ANALYST_CONFIG for backwards compatibility
ANALYST_ORDER = [(config["display_name"], key) for key, config in sorted(ANALYST_CONFIG.items(), key=lambda x: x[1]["order"])]


def get_analyst_nodes():
    """Get the mapping of analyst keys to their (node_name, agent_func) tuples."""
    return {key: (f"{key}_agent", config["agent_func"]) for key, config in ANALYST_CONFIG.items()}


def get_agents_list():
    """Get the list of agents for API responses."""
    return [
        {
            "key": key,
            "display_name": config["display_name"],
            "description": config["description"],
            "investing_style": config["investing_style"],
            "order": config["order"]
        }
        for key, config in sorted(ANALYST_CONFIG.items(), key=lambda x: x[1]["order"])
    ]
