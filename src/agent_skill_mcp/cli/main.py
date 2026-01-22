import click
from agent_skill_mcp.core import Agent
from skills.example_skill import ExampleSkill
from agent_skill_mcp.logger import logger
import asyncio


@click.group()
def cli():
    """Agent-Skill-MCP Framework CLI"""
    pass


@cli.command()
def list_skills():
    """列出所有可用技能"""
    agent = Agent("CLIAgent")
    agent.add_skill(ExampleSkill())
    
    skills = agent.get_all_skill_metadata()
    click.echo("Available skills:")
    for skill in skills:
        click.echo(f"- {skill['name']}: {skill['description']}")


@cli.command()
@click.option('--skill', required=True, help='Skill name to execute')
@click.option('--params', default='{}', help='Skill parameters as JSON string')
def execute(skill, params):
    """执行指定技能"""
    import json
    
    try:
        params_dict = json.loads(params)
    except json.JSONDecodeError:
        click.echo("Invalid JSON parameters", err=True)
        return
    
    async def run():
        agent = Agent("CLIAgent")
        agent.add_skill(ExampleSkill())
        
        try:
            result = await agent.execute_skill(skill, params_dict)
            click.echo(f"Execution result: {result}")
        except Exception as e:
            click.echo(f"Error: {e}", err=True)
    
    asyncio.run(run())


@cli.command()
def version():
    """显示框架版本"""
    from agent_skill_mcp.config import settings
    click.echo(f"Agent-Skill-MCP Framework v1.0.0")


if __name__ == '__main__':
    cli()
