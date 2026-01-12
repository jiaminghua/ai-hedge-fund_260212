# AI 对冲基金

这是一个AI驱动的对冲基金概念验证项目。该项目的目标是探索使用AI做出交易决策的可能性。此项目仅用于**教育**目的，不打算用于实际交易或投资。

该系统由多个智能代理协同工作：

1. Aswath Damodaran 代理 - 估值院长，专注于故事、数据和严谨的估值
2. Ben Graham 代理 - 价值投资教父，只购买具有安全边际的隐藏宝石
3. Bill Ackman 代理 - 激进投资者，采取大胆立场并推动变革
4. Cathie Wood 代理 - 成长投资女王，相信创新和颠覆的力量
5. Charlie Munger 代理 - 沃伦·巴菲特的合作伙伴，只在公平价格购买出色的企业
6. Michael Burry 代理 - 大空头逆向投资者，寻找深度价值
7. Mohnish Pabrai 代理 - Dhandho 投资者，寻找低风险翻倍机会
8. Peter Lynch 代理 - 实用投资者，在日常业务中寻找"十倍股"
9. Phil Fisher 代理 - 一丝不苟的成长投资者，使用深度"闲聊"研究
10. Rakesh Jhunjhunwala 代理 - 印度的大牛
11. Stanley Druckenmiller 代理 - 宏观传奇人物，寻找具有增长潜力的不对称机会
12. Warren Buffett 代理 - 奥马哈先知，以公平价格寻找出色的公司
13. 估值代理 - 计算股票的内在价值并生成交易信号
14. 情绪代理 - 分析市场情绪并生成交易信号
15. 基本面代理 - 分析基本面数据并生成交易信号
16. 技术分析代理 - 分析技术指标并生成交易信号
17. 风险管理器 - 计算风险指标并设置仓位限制
18. 投资组合经理 - 做出最终交易决策并生成订单

<img width="1042" alt="Screenshot 2025-03-22 at 6 19 07 PM" src="https://github.com/user-attachments/assets/cbae3dcf-b571-490d-b0ad-3f0f035ac0d4" />

注意：该系统不会实际执行任何交易。

[![Twitter Follow](https://img.shields.io/twitter/follow/virattt?style=social)](https://twitter.com/virattt)

## 免责声明

该项目仅用于**教育和研究目的**。

- 不打算用于实际交易或投资
- 不提供任何投资建议或保证
- 创建者对财务损失不承担任何责任
- 投资决策请咨询财务顾问
- 过往表现不代表未来结果

使用本软件，即表示您同意仅将其用于学习目的。

## 目录
- [如何安装](#如何安装)
- [如何运行](#如何运行)
  - [⌨️ 命令行界面](#️-命令行界面)
  - [🖥️ Web 应用程序](#️-web-应用程序)
- [如何贡献](#如何贡献)
- [功能请求](#功能请求)
- [许可证](#许可证)

## 如何安装

在运行 AI 对冲基金之前，您需要安装它并设置您的 API 密钥。这些步骤对于全栈 Web 应用程序和命令行界面都是通用的。

### 1. 克隆仓库

```bash
git clone https://github.com/virattt/ai-hedge-fund.git
cd ai-hedge-fund
```

### 2. 设置 API 密钥

创建一个 `.env` 文件来存储您的 API 密钥：
```bash
# 创建 .env 文件用于存储 API 密钥（在根目录中）
cp .env.example .env
```

打开并编辑 `.env` 文件以添加您的 API 密钥：
```bash
# 用于运行 openai 托管的 LLM（gpt-4o, gpt-4o-mini 等）
OPENAI_API_KEY=your-openai-api-key

# 用于获取为对冲基金提供动力的金融数据
FINANCIAL_DATASETS_API_KEY=your-financial-datasets-api-key
```

**重要提示**：您必须至少设置一个 LLM API 密钥（例如 `OPENAI_API_KEY`、`GROQ_API_KEY`、`ANTHROPIC_API_KEY` 或 `DEEPSEEK_API_KEY`）才能使对冲基金正常工作。

**金融数据**：AAPL、GOOGL、MSFT、NVDA 和 TSLA 的数据是免费的，不需要 API 密钥。对于任何其他股票代码，您需要在 .env 文件中设置 `FINANCIAL_DATASETS_API_KEY`。

## 如何运行

### ⌨️ 命令行界面

您可以通过终端直接运行 AI 对冲基金。这种方法提供了更精细的控制，适用于自动化、脚本编写和集成目的。

<img width="992" alt="Screenshot 2025-01-06 at 5 50 17 PM" src="https://github.com/user-attachments/assets/e8ca04bf-9989-4a7d-a8b4-34e04666663b" />

#### 快速开始

1. 安装 Poetry（如果尚未安装）：
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. 安装依赖：
```bash
poetry install
```

#### 运行 AI 对冲基金
```bash
poetry run python src/main.py --ticker AAPL,MSFT,NVDA
```

您还可以指定 `--ollama` 标志来使用本地 LLM 运行 AI 对冲基金。

```bash
poetry run python src/main.py --ticker AAPL,MSFT,NVDA --ollama
```

您可以选择指定开始和结束日期，以便在特定时间段内做出决策。

```bash
poetry run python src/main.py --ticker AAPL,MSFT,NVDA --start-date 2024-01-01 --end-date 2024-03-01
```

#### 运行回测器
```bash
poetry run python src/backtester.py --ticker AAPL,MSFT,NVDA
```

**示例输出：**
<img width="941" alt="Screenshot 2025-01-06 at 5 47 52 PM" src="https://github.com/user-attachments/assets/00e794ea-8628-44e6-9a84-8f8a31ad3b47" />


注意：`--ollama`、`--start-date` 和 `--end-date` 标志也适用于回测器！

### 🖥️ Web 应用程序

运行 AI 对冲基金的新方式是通过我们的 Web 应用程序，它提供了用户友好的界面。对于喜欢可视化界面而非命令行工具的用户，建议使用此方法。

请在此处查看有关如何安装和运行 Web 应用程序的详细说明 [here](https://github.com/virattt/ai-hedge-fund/tree/main/app)。

<img width="1721" alt="Screenshot 2025-06-28 at 6 41 03 PM" src="https://github.com/user-attachments/assets/b95ab696-c9f4-416c-9ad1-51feb1f5374b" />


## 如何贡献

1. Fork 仓库
2. 创建功能分支
3. 提交您的更改
4. 推送到分支
5. 创建 Pull Request

**重要提示**：请保持您的拉取请求小而集中。这将使审查和合并变得更加容易。

## 功能请求

如果您有功能请求，请打开一个 [issue](https://github.com/virattt/ai-hedge-fund/issues) 并确保它被标记为 `enhancement`。

## 许可证

该项目采用 MIT 许可证 - 有关详细信息，请参阅 LICENSE 文件。
