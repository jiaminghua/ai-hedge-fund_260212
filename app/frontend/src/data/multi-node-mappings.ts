export interface MultiNodeDefinition {
  name: string;
  nodes: {
    componentName: string;
    offsetX: number;
    offsetY: number;
  }[];
  edges: {
    source: string;
    target: string;
  }[];
}

const multiNodeDefinition: Record<string, MultiNodeDefinition> = {
  "价值投资者": {
    name: "价值投资者",
    nodes: [
      { componentName: "股票输入", offsetX: 0, offsetY: 0 },
      { componentName: "ben_graham", offsetX: 400, offsetY: -400 },
      { componentName: "charlie_munger", offsetX: 400, offsetY: 0 },
      { componentName: "warren_buffett", offsetX: 400, offsetY: 400 },
      { componentName: "投资组合管理器", offsetX: 800, offsetY: 0 },
    ],
    edges: [
      { source: "股票输入", target: "ben_graham" },
      { source: "股票输入", target: "charlie_munger" },
      { source: "股票输入", target: "warren_buffett" },
      { source: "ben_graham", target: "投资组合管理器" },
      { source: "charlie_munger", target: "投资组合管理器" },
      { source: "warren_buffett", target: "投资组合管理器" },
    ],
  },
  "数据奇才": {
    name: "数据奇才",
    nodes: [
      { componentName: "股票输入", offsetX: 0, offsetY: 0 },
      { componentName: "technical_analyst", offsetX: 400, offsetY: -550 },
      { componentName: "fundamentals_analyst", offsetX: 400, offsetY: -200 },
      { componentName: "sentiment_analyst", offsetX: 400, offsetY: 150 },
      { componentName: "valuation_analyst", offsetX: 400, offsetY: 500 },
      { componentName: "投资组合管理器", offsetX: 800, offsetY: 0 },
    ],
    edges: [
      { source: "股票输入", target: "technical_analyst" },
      { source: "股票输入", target: "fundamentals_analyst" },
      { source: "股票输入", target: "sentiment_analyst" },
      { source: "股票输入", target: "valuation_analyst" },
      { source: "technical_analyst", target: "投资组合管理器" },
      { source: "fundamentals_analyst", target: "投资组合管理器" },
      { source: "sentiment_analyst", target: "投资组合管理器" },
      { source: "valuation_analyst", target: "投资组合管理器" },

    ],
  },
  "市场先锋": {
    name: "市场先锋",
    nodes: [
      { componentName: "股票输入", offsetX: 0, offsetY: 0 },
      { componentName: "michael_burry", offsetX: 400, offsetY: -400 },
      { componentName: "bill_ackman", offsetX: 400, offsetY: 0 },
      { componentName: "stanley_druckenmiller", offsetX: 400, offsetY: 400 },
      { componentName: "投资组合管理器", offsetX: 800, offsetY: 0 },
    ],
    edges: [
      { source: "股票输入", target: "michael_burry" },
      { source: "股票输入", target: "bill_ackman" },
      { source: "股票输入", target: "stanley_druckenmiller" },
      { source: "michael_burry", target: "投资组合管理器" },
      { source: "bill_ackman", target: "投资组合管理器" },
      { source: "stanley_druckenmiller", target: "投资组合管理器" },
    ],
  },
};

export function getMultiNodeDefinition(name: string): MultiNodeDefinition | null {
  return multiNodeDefinition[name] || null;
}

export function isMultiNodeComponent(componentName: string): boolean {
  const result = componentName in multiNodeDefinition;
  console.log('isMultiNodeComponent called with:', componentName, 'result:', result);
  return result;
} 