# Copyright 2025 刘子健_LiuZijian
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
VisionDesk 的日志配置和工具模块。
Logging configuration and utilities for VisionDesk.

此模块提供集中式的日志设置，包括文件轮转、控制台输出以及开发和生产环境的不同日志级别。
This module provides a centralised logging setup with file rotation,
console output, and different log levels for development and production.

可用函数列表 (Available Functions):

基础日志功能 (Basic Logging):
    - get_logger(name: str) -> logging.Logger
        获取日志记录器实例 / Get a logger instance
    - setup_logging(**kwargs) -> None
        配置日志系统 / Configure the logging system

步骤日志 (Step Logging):
    - log_step_start(logger, message)
        记录步骤开始 / Log step start
    - log_step_complete(logger, message)
        记录步骤完成 / Log step completion
    - log_phase_complete(logger, message)
        记录阶段完成 / Log phase completion

操作日志 (Operation Logging):
    - log_init(logger, message)
        记录初始化操作 / Log initialization
    - log_config(logger, message)
        记录配置操作 / Log configuration
    - log_network(logger, message)
        记录网络操作 / Log network operation
    - log_ai(logger, message)
        记录AI操作 / Log AI operation
    - log_screenshot(logger, message)
        记录截图操作 / Log screenshot operation

使用示例 (Usage Example):
    logger = get_logger(__name__)
    setup_logging(default_level="DEBUG", use_emoji=True)
    log_init(logger, "Starting application")
"""

import logging
import logging.handlers
import sys
from typing import Optional, Dict, Any
from datetime import datetime

from .constants import LOGS_DIR

# Create logs directory if it doesn't exist
LOGS_DIR.mkdir(parents=True, exist_ok=True)


class LogEmoji:
    """
    Emoji constants for different log contexts.
    不同日志上下文的表情符号常量。
    """
    # Status emojis / 状态表情
    STEP_START = "🐾"  # Starting a step / 开始执行步骤
    STEP_PROGRESS = "🐾"  # In progress / 进行中
    STEP_COMPLETE = "✅"  # Step completed / 步骤完成
    PHASE_COMPLETE = "🫡"  # Phase completed / 阶段完成

    # Result emojis / 结果表情
    SUCCESS = "🫡"  # Success / 成功
    WARNING = "⚠️"  # Warning / 警告
    ERROR = "❌"  # Error / 错误
    CRITICAL = "🚨"  # Critical / 严重错误

    # Action emojis / 动作表情
    INIT = "🚀"  # Initialisation / 初始化
    CONFIG = "⚙️"  # Configuration / 配置
    SAVE = "💾"  # Saving / 保存
    LOAD = "📂"  # Loading / 加载
    NETWORK = "🌐"  # Network operation / 网络操作
    AI = "✨"  # AI operation / AI操作
    SCREENSHOT = "📸"  # Screenshot / 截图

    # System emojis / 系统表情
    START = "🎇"  # Application start / 应用启动
    STOP = "🛑"  # Application stop / 应用停止
    RESTART = "🔄"  # Restart / 重启

    @classmethod
    def get_level_emoji(cls, level: str) -> str:
        """
        Get emoji for log level.
        获取日志级别对应的表情。
        """
        level_map = {
            'DEBUG': '🔍',
            'INFO': 'ℹ️',
            'WARNING': cls.WARNING,
            'ERROR': cls.ERROR,
            'CRITICAL': cls.CRITICAL
        }
        return level_map.get(level.upper(), '')


class VisionDeskFormatter(logging.Formatter):
    """
    Custom formatter for VisionDesk with timestamp and optional emojis.
    VisionDesk 的自定义格式化器，包含时间戳和可选的表情符号。
    """

    def __init__(
            self,
            fmt: Optional[str] = None,
            datefmt: Optional[str] = None,
            use_emoji: bool = True,
            use_colors: bool = False
    ):
        """
        Initialise the formatter.
        初始化格式化器。

        Args:
            fmt: Format string / 格式字符串
            datefmt: Date format string / 日期格式字符串
            use_emoji: Whether to include emojis / 是否包含表情符号
            use_colors: Whether to use ANSI colors / 是否使用 ANSI 颜色
        """
        if fmt is None:
            fmt = '[%(asctime)s] %(emoji)s [%(name)s] %(levelname)s: %(message)s'
        if datefmt is None:
            datefmt = '%Y-%m-%d %H:%M:%S'

        super().__init__(fmt, datefmt)
        self.use_emoji = use_emoji
        self.use_colors = use_colors

        # ANSI colour codes / ANSI 颜色代码
        self.COLORS = {
            'DEBUG': '\033[36m',  # Cyan / 青色
            'INFO': '\033[32m',  # Green / 绿色
            'WARNING': '\033[33m',  # Yellow / 黄色
            'ERROR': '\033[31m',  # Red / 红色
            'CRITICAL': '\033[35m',  # Magenta / 洋红色
        }
        self.RESET = '\033[0m'

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record.
        格式化日志记录。
        """
        # Add emoji attribute / 添加表情属性
        if self.use_emoji and hasattr(record, 'emoji'):
            record.emoji = record.emoji
        elif self.use_emoji:
            record.emoji = LogEmoji.get_level_emoji(record.levelname)
        else:
            record.emoji = ''

        # Apply colors if enabled / 如果启用则应用颜色
        original_levelname = record.levelname
        if self.use_colors and record.levelname in self.COLORS:
            record.levelname = f"{self.COLORS[record.levelname]}{record.levelname}{self.RESET}"

        # Format the message / 格式化消息
        result = super().format(record)

        # Reset levelname for other handlers / 为其他处理器重置级别名
        record.levelname = original_levelname

        return result


class VisionDeskLogger:
    """
    Main logger class for VisionDesk application.
    VisionDesk 应用的主日志类。
    """

    _instances: Dict[str, logging.Logger] = {}
    _default_level: str = "INFO"
    _file_logging_enabled: bool = True
    _console_logging_enabled: bool = True

    @classmethod
    def setup_logging(
            cls,
            default_level: str = "INFO",
            file_logging: bool = True,
            console_logging: bool = True,
            use_emoji: bool = True,
            use_colors: bool = False,
            log_file_prefix: str = "visiondesk"
    ) -> None:
        """
        Set up global logging configuration.
        设置全局日志配置。

        Args:
            default_level: Default logging level / 默认日志级别
            file_logging: Enable file logging / 启用文件日志
            console_logging: Enable console logging / 启用控制台日志
            use_emoji: Use emojis in logs / 在日志中使用表情
            use_colors: Use colors in console / 在控制台使用颜色
            log_file_prefix: Log file name prefix / 日志文件名前缀
        """
        cls._default_level = default_level.upper()
        cls._file_logging_enabled = file_logging
        cls._console_logging_enabled = console_logging

        # Create root logger configuration / 创建根日志配置
        root_logger = logging.getLogger()
        root_logger.setLevel(getattr(logging, cls._default_level, logging.INFO))

        # Clear existing handlers / 清除现有处理器
        root_logger.handlers.clear()

        # File handler with rotation / 带轮转的文件处理器
        if file_logging:
            log_file = LOGS_DIR / f"{log_file_prefix}_{datetime.now().strftime('%Y%m%d')}.log"
            file_handler = logging.handlers.RotatingFileHandler(
                log_file,
                maxBytes=10 * 1024 * 1024,  # 10MB
                backupCount=10,  # 最大轮转数 10 个文件
                encoding='utf-8'
            )
            file_formatter = VisionDeskFormatter(
                fmt='[%(asctime)s] [%(name)s] %(levelname)s: %(message)s',
                use_emoji=False,  # No emojis in file logs / 文件日志中不使用表情
                use_colors=False
            )
            file_handler.setFormatter(file_formatter)
            file_handler.setLevel(logging.DEBUG)  # Always log everything to file / 总是记录所有内容到文件
            root_logger.addHandler(file_handler)

        # Console handler / 控制台处理器
        if console_logging:
            console_handler = logging.StreamHandler(sys.stdout)
            console_formatter = VisionDeskFormatter(
                use_emoji=use_emoji,
                use_colors=use_colors
            )
            console_handler.setFormatter(console_formatter)
            console_handler.setLevel(getattr(logging, cls._default_level, logging.INFO))
            root_logger.addHandler(console_handler)

    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        """
        Get or create a logger instance.
        获取或创建日志实例。

        Args:
            name: Logger name (usually __name__) / 日志名称（通常是 __name__）

        Returns:
            Logger instance / 日志实例
        """
        if name not in cls._instances:
            logger = logging.getLogger(name)
            cls._instances[name] = logger
        return cls._instances[name]

    @classmethod
    def log_step(cls, logger: logging.Logger, message: str, emoji: str = LogEmoji.STEP_START) -> None:
        """
        Log a step with emoji.
        使用表情记录步骤。

        Args:
            logger: Logger instance / 日志实例
            message: Log message / 日志消息
            emoji: Emoji to use / 要使用的表情
        """
        record = logger.makeRecord(
            logger.name, logging.INFO, "(custom)", 0,
            message, (), None
        )
        record.emoji = emoji
        logger.handle(record)


# Convenience functions / 便捷函数
def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance with the default configuration.
    使用默认配置获取日志实例。

    Args:
        name: Logger name (usually __name__) / 日志名称（通常是 __name__）

    Returns:
        Logger instance / 日志实例
    """
    return VisionDeskLogger.get_logger(name)


def setup_logging(**kwargs) -> None:
    """
    Set up logging with custom configuration.
    使用自定义配置设置日志。
    """
    VisionDeskLogger.setup_logging(**kwargs)


# Helper functions for logging with emojis / 带表情的日志辅助函数
def log_step_start(logger: logging.Logger, message: str) -> None:
    """Log the start of a step. / 记录步骤开始。"""
    VisionDeskLogger.log_step(logger, message, LogEmoji.STEP_START)


def log_step_complete(logger: logging.Logger, message: str) -> None:
    """Log the completion of a step. / 记录步骤完成。"""
    VisionDeskLogger.log_step(logger, message, LogEmoji.STEP_COMPLETE)


def log_phase_complete(logger: logging.Logger, message: str) -> None:
    """Log the completion of a phase. / 记录阶段完成。"""
    VisionDeskLogger.log_step(logger, message, LogEmoji.PHASE_COMPLETE)


def log_init(logger: logging.Logger, message: str) -> None:
    """Log initialisation. / 记录初始化。"""
    VisionDeskLogger.log_step(logger, message, LogEmoji.INIT)


def log_config(logger: logging.Logger, message: str) -> None:
    """Log configuration. / 记录配置。"""
    VisionDeskLogger.log_step(logger, message, LogEmoji.CONFIG)


def log_network(logger: logging.Logger, message: str) -> None:
    """Log network operation. / 记录网络操作。"""
    VisionDeskLogger.log_step(logger, message, LogEmoji.NETWORK)


def log_ai(logger: logging.Logger, message: str) -> None:
    """Log AI operation. / 记录 AI 操作。"""
    VisionDeskLogger.log_step(logger, message, LogEmoji.AI)


def log_screenshot(logger: logging.Logger, message: str) -> None:
    """Log screenshot operation. / 记录截图操作。"""
    VisionDeskLogger.log_step(logger, message, LogEmoji.SCREENSHOT)


# Initialise with default settings when module is imported / 导入模块时使用默认设置初始化
VisionDeskLogger.setup_logging()
# --- Example Usage / 使用示例 ---
if __name__ == "__main__":
    import time
    import os
    # Clean up old log files for a fresh test / 清理旧日志文件以进行全新测试
    for f in LOGS_DIR.glob("visiondesk_*.log*"):
        try:
            os.remove(f)
        except OSError as e:
            print(f"Error removing file {f}: {e}")
    print(f"Cleaned up old logs in {LOGS_DIR}\n")
    print("--- Test 1: Console with emojis and colors, File with no emojis/colors ---")
    print("--- 测试 1: 控制台带表情和颜色，文件不带表情/颜色 ---")
    setup_logging(
        default_level="DEBUG",
        use_emoji=True,
        use_colors=True,
        file_logging=True,
        console_logging=True
    )
    logger1 = get_logger(__name__)
    logger1.debug("This is a standard DEBUG message. / 这是标准 DEBUG 消息。")
    logger1.info("This is a standard INFO message. / 这是标准 INFO 消息。")
    logger1.warning("This is a standard WARNING message. / 这是标准 WARNING 消息。")
    logger1.error("This is a standard ERROR message. / 这是标准 ERROR 消息。")
    logger1.critical("This is a standard CRITICAL message. / 这是标准 CRITICAL 消息。")
    log_init(logger1, "Application initialisation started. / 应用程序初始化开始。")
    log_config(logger1, "Loading configuration settings. / 加载配置设置。")
    log_step_start(logger1, "Beginning complex calculation. / 开始复杂计算。")
    log_network(logger1, "Sending data to remote server. / 发送数据到远程服务器。")
    log_ai(logger1, "Processing image with AI model. / 使用 AI 模型处理图像。")
    log_screenshot(logger1, "Captured screen for analysis. / 捕获屏幕进行分析。")
    log_step_complete(logger1, "Complex calculation finished. / 复杂计算完成。")
    log_phase_complete(logger1, "All core modules successfully loaded and ready. / 所有核心模块成功加载并准备就绪。")
    print("\n--- Console Output (expect emojis and colors): ---")
    print("--- 控制台输出（期望有表情和颜色）：---")
    print("    (You should see colors and emojis like 🐞, ℹ️, ⚠️, ❌, 🚨 for standard logs,")
    print("     and 🚀, ⚙️, 🙌, 🌐, 🧠, 📸, ✅, 🫡 for custom step logs.)")
    print("    (您应该看到标准日志有颜色和表情符号，如 🐞, ℹ️, ⚠️, ❌, 🚨，")
    print("     自定义步骤日志有 🚀, ⚙️, 🙌, 🌐, 🧠, 📸, ✅, 🫡。)\n")
    # Give some time for file writes to complete / 给文件写入留出一些时间
    time.sleep(0.5)
    # Read and print file content to verify no emojis/colors / 读取并打印文件内容以验证没有表情符号/颜色
    log_file_path = LOGS_DIR / f"visiondesk_{datetime.now().strftime('%Y%m%d')}.log"
    print(f"\n--- File Output from: {log_file_path} (expect no emojis/colors): ---")
    print(f"--- 文件输出自: {log_file_path} (期望无表情符号/颜色): ---")
    try:
        with open(log_file_path, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Log file not found at {log_file_path}. Please check if file_logging was enabled and path is correct.")
    except Exception as e:
        print(f"Error reading log file: {e}")
    # --- Test 2: Console only, no emojis, no colors, no file logging ---
    # To re-setup logging, we need to explicitly force re-initialization,
    # as setup_logging is designed to be called once, but for testing, we override this.
    # 为了重新设置日志，我们需要明确强制重新初始化，
    # 因为 setup_logging 被设计为只调用一次，但为了测试，我们覆盖了这一点。
    print("\n\n--- Test 2: Console only, no emojis, no colors, no file logging ---")
    print("--- 测试 2: 仅控制台，无表情符号，无颜色，无文件日志 ---")
    setup_logging( # This call will force re-initialization due to different settings
        default_level="INFO",
        use_emoji=True,
        use_colors=True,
        file_logging=False,
        console_logging=True
    )
    logger2 = get_logger("MyModule") # Get a different named logger
    logger2.info("This is an INFO message without emojis or colors. / 这是没有表情或颜色的 INFO 消息。")
    logger2.warning("This is a WARNING message without emojis or colors. / 这是没有表情或颜色的 WARNING 消息。")
    # Custom step logs should also not have emojis if use_emoji is False in setup_logging
    # 如果 setup_logging 中 use_emoji 为 False，则自定义步骤日志也不应有表情符号
    log_step_start(logger2, "Starting a process without emojis. / 开始一个没有表情符号的进程。")
    log_step_complete(logger2, "Process completed without emojis. / 进程完成，无表情符号。")
    print("\n--- Console Output (expect no emojis/colors): ---")
    print("--- 控制台输出（期望无表情/颜色）：---")
    print("    (You should see plain text without any special characters or colors.)")
    print("    (您应该看到纯文本，没有任何特殊字符或颜色。)\n")