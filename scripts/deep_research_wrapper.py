#!/usr/bin/env python3
"""
企业深度调研框架生成器
Enterprise Deep Research Framework Generator

生成结构化的企业调研框架和搜索问题清单，供 AI 智能体通过 web-search 工具完成实际调研。
Generates a structured research framework and search queries for AI agents
to conduct actual research via web-search tools.

输入：公司名称、国家
输出：结构化调研框架（Markdown / JSON）
"""

import argparse
import json
import sys
from typing import Dict, List


class CompanyResearcher:
    """企业调研框架生成器"""

    def __init__(self, company_name: str, country: str = "中国"):
        self.company_name = company_name
        self.country = country

    def research_company(self) -> Dict:
        """
        生成企业调研框架

        Returns:
            Dict: 包含调研框架和搜索问题清单的字典
        """
        print(f"[调研] 正在生成 {self.company_name} 的调研框架...")
        return self._generate_company_framework()

    def _generate_company_framework(self) -> Dict:
        """
        生成企业调研框架

        Returns:
            Dict: 企业调研框架
        """
        company_info = {
            "company_name": self.company_name,
            "country": self.country,
            "research_status": "框架已生成，待智能体通过 web-search 深度调研",
            "company_overview": {
                "introduction": f"{self.company_name} 是一家位于{self.country}的企业，具体介绍需通过深度调研获取。",
                "established_year": "待调研",
                "team_size": "待调研"
            },
            "business_info": {
                "main_business": "待深度调研主营业务",
                "business_model": "待调研",
                "core_services": ["待调研"]
            },
            "products": {
                "core_products": ["待调研"],
                "product_features": "待调研"
            },
            "tags": {
                "industry_tags": ["待调研"],
                "business_tags": ["待调研"],
                "market_position": "待调研"
            },
            "customers": {
                "main_customers": ["待调研"],
                "customer_segments": "待调研"
            },
            "research_queries": self._generate_research_queries(),
            "industry_research_queries": self._generate_industry_queries()
        }

        return company_info

    def _generate_research_queries(self) -> List[str]:
        """
        生成企业调研搜索问题清单（供智能体 web-search 使用）

        Returns:
            List[str]: 调研问题列表
        """
        return [
            f"{self.company_name} 公司介绍 成立时间 发展历程",
            f"{self.company_name} 主营业务 核心业务 服务范围",
            f"{self.company_name} 代表产品 核心产品 主要服务",
            f"{self.company_name} 行业分类 业务标签 所属行业",
            f"{self.company_name} 客户群体 主要客户 服务对象",
            f"{self.company_name} 团队规模 员工人数 组织架构",
            f"{self.company_name} 竞争优势 核心竞争力 业务特点",
            f"{self.company_name} 财务状况 营收规模（如有公开信息）"
        ]

    def _generate_industry_queries(self) -> List[Dict[str, str]]:
        """
        生成行业调研搜索问题（痛点 + 案例）

        Returns:
            List[Dict]: 行业调研问题列表，含搜索目的说明
        """
        return [
            {
                "purpose": "行业共性痛点",
                "query": f"{self.company_name} 所在行业 痛点 挑战 2024 2025",
                "collect": "行业普遍痛点、典型表现、量化数据"
            },
            {
                "purpose": "行业AI应用案例（通用）",
                "query": f"{self.company_name} 所在行业 AI应用 智能化 案例",
                "collect": "至少3个标杆企业案例：企业背景、应用场景、技术方案、实施效果"
            },
            {
                "purpose": "行业AI应用案例（细分）",
                "query": f"{self.company_name} 核心业务 AI LLM 实践",
                "collect": "细分业务领域的AI实践案例和关键成功因素"
            }
        ]

    def format_output(self, company_info: Dict, format_type: str = "markdown") -> str:
        """
        格式化输出

        Args:
            company_info: 公司信息字典
            format_type: 输出格式（markdown/json）

        Returns:
            str: 格式化输出
        """
        if format_type == "json":
            return json.dumps(company_info, ensure_ascii=False, indent=2)
        else:
            return self._format_markdown(company_info)

    def _format_markdown(self, company_info: Dict) -> str:
        """
        格式化为Markdown

        Args:
            company_info: 公司信息字典

        Returns:
            str: Markdown格式
        """
        md = f"# {company_info['company_name']} 企业调研框架\n\n"
        md += f"**调研状态**: {company_info.get('research_status', '未知')}\n\n"
        md += f"**国家/地区**: {company_info['country']}\n\n"

        # 公司概览
        md += "## 公司概览\n\n"
        overview = company_info.get('company_overview', {})
        md += f"- **公司介绍**: {overview.get('introduction', '待调研')}\n"
        md += f"- **成立年份**: {overview.get('established_year', '待调研')}\n"
        md += f"- **团队规模**: {overview.get('team_size', '待调研')}\n\n"

        # 业务信息
        md += "## 业务信息\n\n"
        business = company_info.get('business_info', {})
        md += f"- **主营业务**: {business.get('main_business', '待调研')}\n"
        md += f"- **业务模式**: {business.get('business_model', '待调研')}\n\n"

        core_services = business.get('core_services', [])
        if core_services and core_services != ["待调研"]:
            md += "**核心服务**:\n"
            for i, service in enumerate(core_services, 1):
                md += f"{i}. {service}\n"
            md += "\n"

        # 产品信息
        md += "## 产品/服务\n\n"
        products = company_info.get('products', {})
        core_products = products.get('core_products', [])
        if core_products and core_products != ["待调研"]:
            md += "**代表产品**:\n"
            for i, product in enumerate(core_products, 1):
                md += f"{i}. {product}\n"
            md += "\n"

        # 标签
        md += "## 行业/业务标签\n\n"
        tags = company_info.get('tags', {})
        industry_tags = tags.get('industry_tags', [])
        business_tags = tags.get('business_tags', [])

        if industry_tags and industry_tags != ["待调研"]:
            md += f"- **行业**: {', '.join(industry_tags)}\n"
        if business_tags and business_tags != ["待调研"]:
            md += f"- **业务**: {', '.join(business_tags)}\n"

        # 企业调研查询
        if "research_queries" in company_info:
            md += "\n## 待调研问题清单（企业信息）\n\n"
            md += "以下问题需要智能体通过 **web-search** 工具深度调研：\n\n"
            queries = company_info["research_queries"]
            for i, query in enumerate(queries, 1):
                md += f"{i}. `{query}`\n"

        # 行业调研查询
        if "industry_research_queries" in company_info:
            md += "\n## 待调研问题清单（行业信息）\n\n"
            for item in company_info["industry_research_queries"]:
                md += f"### {item['purpose']}\n"
                md += f"- **搜索关键词**: `{item['query']}`\n"
                md += f"- **收集内容**: {item['collect']}\n\n"

        return md


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='企业深度调研框架生成器 - 生成调研框架供智能体 web-search 使用'
    )
    parser.add_argument('--company-name', required=True, help='公司名称')
    parser.add_argument('--country', default='中国', help='国家/地区（默认：中国）')
    parser.add_argument('--format', choices=['markdown', 'json'], default='markdown',
                       help='输出格式（默认：markdown）')

    args = parser.parse_args()

    try:
        researcher = CompanyResearcher(
            company_name=args.company_name,
            country=args.country
        )

        company_info = researcher.research_company()
        output = researcher.format_output(company_info, args.format)
        print(output)

        return 0

    except Exception as e:
        print(f"[错误] {str(e)}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
