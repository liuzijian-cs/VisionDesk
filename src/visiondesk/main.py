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
VisionDesk 程序主入口点模块。
VisionDesk program main entry point module.

此模块提供应用程序的主入口函数，负责创建和启动 App 实例。
This module provides the main entry function for the application, responsible for
creating and launching the App instance.
"""

import sys
from src.visiondesk.utils import setup_logging, get_logger

def main() -> None:

    # Logger:
    setup_logging(
        default_level="INFO",
        use_emoji=True,
        use_colors=True,
        file_logging=True,
        console_logging=True
    )

    logger = get_logger(__name__)
    logger.info("🎇 Application starting... ")

if __name__ == "__main__":
    main()