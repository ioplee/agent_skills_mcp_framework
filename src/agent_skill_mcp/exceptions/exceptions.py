from .base import AgentSkillMCPError


class SkillError(AgentSkillMCPError):
    """技能相关异常"""
    pass


class SkillNotFoundError(SkillError):
    """技能未找到异常"""
    
    def __init__(self, skill_name: str):
        super().__init__(f"Skill '{skill_name}' not found", code=404)


class SkillValidationError(SkillError):
    """技能参数验证异常"""
    
    def __init__(self, skill_name: str, message: str):
        super().__init__(f"Skill '{skill_name}' validation error: {message}", code=400)


class SkillExecutionError(SkillError):
    """技能执行异常"""
    
    def __init__(self, skill_name: str, message: str):
        super().__init__(f"Skill '{skill_name}' execution error: {message}", code=500)


class AgentError(AgentSkillMCPError):
    """代理相关异常"""
    pass


class AgentTimeoutError(AgentError):
    """代理超时异常"""
    
    def __init__(self, message: str = "Agent operation timed out"):
        super().__init__(message, code=408)


class MCPError(AgentSkillMCPError):
    """MCP相关异常"""
    pass


class MCPConnectionError(MCPError):
    """MCP连接异常"""
    
    def __init__(self, message: str = "MCP connection error"):
        super().__init__(message, code=503)


class MCPTimeoutError(MCPError):
    """MCP超时异常"""
    
    def __init__(self, message: str = "MCP operation timed out"):
        super().__init__(message, code=408)


class MCPAuthenticationError(MCPError):
    """MCP认证异常"""
    
    def __init__(self, message: str = "MCP authentication error"):
        super().__init__(message, code=401)
