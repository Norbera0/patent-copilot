#!/usr/bin/env python3
"""
Patent Copilot - A Patent Search Agent
Helps users search for similar patents based on their invention descriptions.
"""

import os
import json
from typing import List, Dict, Any
from dotenv import load_dotenv
from serpapi import Client
from langchain.agents import Tool, AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage

# Load environment variables
load_dotenv()

class PatentSearchTool:
    """Custom tool for searching patents using SerpAPI Google Patents API"""
    
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_API_KEY")
        if not self.api_key:
            raise ValueError("SERPAPI_API_KEY not found in environment variables")
        self.client = Client(api_key=self.api_key)
    
    def search_patents(self, query: str) -> str:
        """
        Search for patents using SerpAPI Google Patents API
        
        Args:
            query (str): Search query for patents
            
        Returns:
            str: Formatted patent search results
        """
        try:
            params = {
                "engine": "google_patents",
                "q": query,
                "num": 10  # Limit to top 10 results
            }
            
            results = self.client.search(params)
            
            if "error" in results:
                return f"Error in patent search: {results['error']}"
            
            patents = results.get("organic_results", [])
            
            if not patents:
                return f"No patents found for query: '{query}'"
            
            formatted_results = []
            formatted_results.append(f"Patent Search Results for: '{query}'")
            formatted_results.append("=" * 50)
            
            for i, patent in enumerate(patents, 1):
                title = patent.get("title", "No title available")
                snippet = patent.get("snippet", "No description available")
                patent_id = patent.get("patent_id", "No patent ID")
                inventor = patent.get("inventor", "Unknown inventor")
                assignee = patent.get("assignee", "Unknown assignee")
                publication_date = patent.get("publication_date", "Unknown date")
                
                formatted_results.append(f"\n{i}. {title}")
                formatted_results.append(f"   Patent ID: {patent_id}")
                formatted_results.append(f"   Inventor: {inventor}")
                formatted_results.append(f"   Assignee: {assignee}")
                formatted_results.append(f"   Publication Date: {publication_date}")
                formatted_results.append(f"   Description: {snippet}")
                formatted_results.append("-" * 40)
            
            return "\n".join(formatted_results)
            
        except Exception as e:
            return f"Error occurred during patent search: {str(e)}"

class PatentAnalysisAgent:
    """LangChain agent for patent analysis and search orchestration"""
    
    def __init__(self):
        # Initialize Gemini
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not gemini_api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=gemini_api_key,
            temperature=0.3
        )
        
        # Initialize patent search tool
        self.patent_tool = PatentSearchTool()
        
        # Create tools
        self.tools = [
            Tool(
                name="patent_search",
                description="Search for patents using a query. Input should be a clear, specific search query about an invention or technology.",
                func=self.patent_tool.search_patents
            )
        ]
        
        # Create agent prompt
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a patent research expert helping users find similar patents for their inventions.

Your task is to:
1. Analyze the user's invention description
2. Extract key technical concepts, keywords, and terminology
3. Generate 2-3 different search strategies:
   - One broad conceptual search
   - One specific technical terms search  
   - One alternative description/approach search
4. Execute these searches using the patent_search tool
5. Analyze the results and provide a comprehensive summary

For each search strategy, explain why you chose those specific terms and what aspect of the invention you're targeting.

After searching, provide:
- Summary of most relevant patents found
- Assessment of potential novelty gaps
- Recommendations for further research
- Suggestions for patent application strategy

Be thorough but concise in your analysis."""),
            ("user", "{input}"),
            ("assistant", "{agent_scratchpad}")
        ])
        
        # Create agent
        self.agent = create_openai_functions_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=self.prompt
        )
        
        # Create agent executor
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            max_iterations=10
        )
    
    def analyze_invention(self, invention_description: str) -> str:
        """
        Analyze an invention and search for similar patents
        
        Args:
            invention_description (str): User's description of their invention
            
        Returns:
            str: Comprehensive analysis and search results
        """
        try:
            result = self.agent_executor.invoke({
                "input": f"""Please analyze this invention and search for similar patents:

Invention Description: {invention_description}

Please follow these steps:
1. Extract key technical concepts and keywords
2. Generate and execute 2-3 different search strategies
3. Analyze the results and provide a comprehensive summary
4. Provide recommendations for patent strategy"""
            })
            
            return result["output"]
            
        except Exception as e:
            return f"Error during patent analysis: {str(e)}"

def print_welcome():
    """Print welcome message and instructions"""
    print("=" * 60)
    print("    🔍 PATENT COPILOT - Patent Search Agent 🔍")
    print("=" * 60)
    print("\nWelcome! I'll help you search for patents similar to your invention.")
    print("\nHow to use:")
    print("• Describe your invention in detail")
    print("• Include key technical features and functionality")
    print("• Be specific about what makes it unique")
    print("\nExample: 'A smart water bottle that tracks hydration levels")
    print("using sensors and sends reminders to a mobile app'")
    print("\n" + "-" * 60)

def get_user_input() -> str:
    """Get invention description from user"""
    print("\n📝 Please describe your invention:")
    print("(Press Enter twice when finished)")
    
    lines = []
    empty_lines = 0
    
    while empty_lines < 2:
        line = input()
        if line.strip() == "":
            empty_lines += 1
        else:
            empty_lines = 0
        lines.append(line)
    
    # Remove trailing empty lines
    while lines and lines[-1].strip() == "":
        lines.pop()
    
    description = "\n".join(lines).strip()
    
    if not description:
        print("❌ Please provide a description of your invention.")
        return get_user_input()
    
    return description

def main():
    """Main application entry point"""
    try:
        # Print welcome message
        print_welcome()
        
        # Check environment variables
        if not os.getenv("GEMINI_API_KEY"):
            print("❌ Error: GEMINI_API_KEY not found in environment variables")
            print("Please create a .env file with your API keys:")
            print("GEMINI_API_KEY=your_gemini_api_key")
            print("SERPAPI_API_KEY=your_serpapi_key")
            return
        
        if not os.getenv("SERPAPI_API_KEY"):
            print("❌ Error: SERPAPI_API_KEY not found in environment variables")
            print("Please create a .env file with your API keys:")
            print("GEMINI_API_KEY=your_gemini_api_key")
            print("SERPAPI_API_KEY=your_serpapi_key")
            return
        
        # Initialize patent analysis agent
        print("🤖 Initializing Patent Analysis Agent...")
        agent = PatentAnalysisAgent()
        print("✅ Agent ready!")
        
        # Get user input
        invention_description = get_user_input()
        
        print(f"\n🔍 Analyzing invention and searching for similar patents...")
        print("This may take a moment...\n")
        
        # Analyze invention and get results
        result = agent.analyze_invention(invention_description)
        
        print("\n📊 Analysis Results:")
        print("=" * 60)
        print(result)
        print("\n" + "=" * 60)
        
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 