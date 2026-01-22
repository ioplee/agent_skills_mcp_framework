class AgentSkillMCPError(Exception):
    """框架基础异常类"""
    
    def __init__(self, message: str, code: int = 500, details: dict = None):
        self.message = message
        self.code = code
        self.details = details or {}
        super().__init__(self.message)
    
    def to_dict(self):
        """转换为字典"""
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "code": self.code,
            "details": self.details
        }
