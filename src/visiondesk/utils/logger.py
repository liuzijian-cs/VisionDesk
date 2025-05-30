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
VisionDesk 日志工具模块。
VisionDesk logging utility module.

此模块提供应用程序的日志配置和管理功能。
This module provides logging configuration and management for the application.
"""

import logging
import os
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler
from typing import Optional


def setup_logger(log_level: str = "INFO", log_dir: Optional[str] = None) -> None:
    """
    设置应用程序的日志系统。
    Set up the application's logging system.

    参数:
        log_level: 日志级别 ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
        log_dir: 日志文件目录，如果为 None，则使用默认目录

    Parameters:
        log_level: Logging level ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
        log_dir: Log file directory. If None, a default directory is used
    """
    # 解析日志级别
    # Parse log level
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)

    # 配置根日志记录器
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(numeric_level)

    # 定义日志格式
    # Define log format
    log_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 添加控制台处理器
    # Add console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    root_logger.addHandler(console_handler)

    # 如果指定了日志目录，添加文件处理器
    # If log directory is specified, add file handler
    if log_dir is not None:
        log_path = Path(log_dir)
    else:
        # 使用默认位置（用户主目录下的 .visiondesk/logs 文件夹）
        # Use default location (.visiondesk/logs folder in user home directory)
        log_path = Path.home() / ".visiondesk" / "logs"

    # 确保日志目录存在
    # Ensure log directory exists
    os.makedirs(log_path, exist_ok=True)

    # 创建一个文件处理器，每个日志文件最大 5MB，保留最新的 5 个日志文件
    # Create a file handler, with max 5MB per log file, keeping the latest 5 log files
    log_file = log_path / "visiondesk.log"
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=5, encoding="utf-8"
    )
    file_handler.setFormatter(log_format)
    root_logger.addHandler(file_handler)

    # 记录初始日志消息
    # Log initial message
    root_logger.info(f"日志系统已初始化，日志级别: {log_level}, 日志文件: {log_file} | "
                   f"Logging system initialized with level: {log_level}, log file: {log_file}")
