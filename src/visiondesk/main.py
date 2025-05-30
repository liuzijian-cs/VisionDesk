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

# import sys
# import logging
# from visiondesk.app import App
# from visiondesk.utils.logger import setup_logger
#
#
# def main() -> int:
#     """
#     VisionDesk 应用程序的主入口函数。
#     Main entry function for the VisionDesk application.
#
#     返回:
#         int: 应用程序的退出代码。0 表示成功退出。
#     Returns:
#         int: The application exit code. 0 indicates successful exit.
#     """
#     # 设置日志系统
#     # Set up logging system
#     setup_logger()
#     logger = logging.getLogger(__name__)
#
#     try:
#         logger.info("VisionDesk 应用程序启动 | VisionDesk application starting")
#         app = App()
#         return app.start()
#     except Exception as e:
#         logger.exception(f"应用程序发生未处理的异常: {e} | Unhandled exception in application: {e}")
#         return 1
#     finally:
#         logger.info("应用程序退出 | Application exited")
#
#
# if __name__ == "__main__":
#     sys.exit(main())
