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
VisionDesk 工具函数模块。
VisionDesk utility functions module.

此模块包含应用程序中使用的各种工具函数和助手类。
This module contains various utility functions and helper classes used throughout the application.
"""

from .logger import (
    setup_logging,
    get_logger,
    log_step_start,
    log_step_complete,
    log_phase_complete,
    log_init,
    log_config,
    log_network,
    log_ai,
    log_screenshot,
)

__all__ = [
    # 日志设置和获取函数
    "setup_logging",
    "get_logger",

    # 步骤日志函数
    "log_step_start",
    "log_step_complete",
    "log_phase_complete",

    # 操作特定日志函数
    "log_init",
    "log_config",
    "log_network",
    "log_ai",
    "log_screenshot",
]
