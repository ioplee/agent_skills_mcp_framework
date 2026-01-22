import asyncio
from agent_skill_mcp.core import Agent
from agent_skill_mcp.mcp import OpenAIMCP
from skills.example_skill import ExampleSkill
from agent_skill_mcp.logger import logger
from agent_skill_mcp.exceptions import SkillNotFoundError, SkillExecutionError


async def main():
    """示例代理主函数"""
    logger.info("Starting example agent...")
    
    try:
        # 创建代理
        agent = Agent("EnterpriseAgent")
        logger.info(f"Created agent: {agent.get_name()}")
        
        # 添加技能
        example_skill = ExampleSkill()
        agent.add_skill(example_skill)
        logger.info(f"Added skill: {example_skill.name}")
        
        # 查看技能元数据
        skill_metadata = agent.get_all_skill_metadata()
        logger.info(f"Skill metadata: {skill_metadata}")
        
        # 执行技能
        logger.info("Executing example skill...")
        result = await agent.execute_skill("example", {"content": "Hello from Enterprise Framework!"})
        logger.info(f"Skill execution result: {result}")
        
        # 尝试执行不存在的技能
        try:
            logger.info("Trying to execute non-existent skill...")
            await agent.execute_skill("non_existent", {})
        except SkillNotFoundError as e:
            logger.warning(f"Expected error: {e}")
        
        # 尝试执行技能时传入无效参数
        try:
            logger.info("Trying to execute skill with invalid params...")
            await agent.execute_skill("example", {"content": 123})  # 无效参数类型
        except SkillExecutionError as e:
            logger.warning(f"Expected error: {e}")
        
        # 初始化MCP（注意：需要在.env文件中设置OPENAI_API_KEY）
        logger.info("Initializing MCP...")
        mcp = OpenAIMCP()
        
        # 使用MCP生成文本
        logger.info("Generating text with MCP...")
        generated_text = await mcp.generate("Write a short poem about AI in 2026")
        logger.info(f"Generated text: {generated_text}")
        
        # 使用MCP进行对话
        logger.info("Chatting with MCP...")
        messages = [
            {"role": "system", "content": "You are a helpful enterprise assistant."},
            {"role": "user", "content": "What are the key benefits of using an agent-skill-mcp framework?"}
        ]
        chat_response = await mcp.chat(messages)
        logger.info(f"Chat response: {chat_response}")
        
        # 使用MCP生成嵌入
        logger.info("Generating embedding with MCP...")
        embedding = await mcp.embed("Enterprise AI framework with agent-skill-mcp architecture")
        logger.info(f"Embedding generated successfully, length: {len(embedding)}")
        
        # 关闭MCP
        mcp.close()
        logger.info("MCP closed successfully")
        
        # 关闭代理
        agent.shutdown()
        logger.info("Agent shutdown successfully")
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
