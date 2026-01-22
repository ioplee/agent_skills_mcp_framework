from loguru import logger
from typing import Optional
from agent_skill_mcp.config import settings
import os


class Logger:
    """统一日志系统"""
    
    def __init__(self):
        self._configure_logger()
    
    def _configure_logger(self):
        """配置日志系统"""
        # 清除默认配置
        logger.remove()
        
        # 控制台输出
        console_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
        logger.add(
            sink=lambda msg: print(msg, end=""),
            format=console_format,
            level=settings.log.level,
            colorize=True
        )
        
        # 文件输出
        if settings.log.file:
            # 确保日志目录存在
            log_dir = os.path.dirname(settings.log.file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir, exist_ok=True)
            
            file_format = "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}"
            logger.add(
                sink=settings.log.file,
                format=file_format,
                level=settings.log.level,
                rotation=settings.log.rotation,
                retention=settings.log.retention,
                compression="zip"
            )
    
    def get_logger(self):
        """获取日志实例"""
        return logger
    
    def debug(self, message: str, **kwargs):
        """调试级别日志"""
        logger.debug(message, **kwargs)
    
    def info(self, message: str, **kwargs):
        """信息级别日志"""
        logger.info(message, **kwargs)
    
    def warning(self, message: str, **kwargs):
        """警告级别日志"""
        logger.warning(message, **kwargs)
    
    def error(self, message: str, **kwargs):
        """错误级别日志"""
        logger.error(message, **kwargs)
    
    def critical(self, message: str, **kwargs):
        """严重级别日志"""
        logger.critical(message, **kwargs)
    
    def exception(self, message: str, **kwargs):
        """异常级别日志"""
        logger.exception(message, **kwargs)


# 创建全局日志实例
logger_instance = Logger()
logger = logger_instance.get_logger()
