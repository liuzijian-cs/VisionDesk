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
VisionDesk 应用程序主类模块。
VisionDesk application main class module.

该模块定义了 VisionDesk 应用程序的主类，负责协调所有应用程序的组件。
This module defines the main class of the VisionDesk application, responsible for
coordinating all components of the application.
"""

# import logging
# from typing import Optional
# from PySide6 import QtWidgets
#
# from visiondesk.core.config import Config
# from visiondesk.ui.components.main_window import MainWindow
# from visiondesk.utils.logger import setup_logger
#
#
# class App:
#     """
#     VisionDesk 应用程序的主类。
#     Main class for the VisionDesk application.
#
#     负责初始化并协调应用程序的各个组件，如 UI、服务和配置管理。
#     Responsible for initializing and coordinating various components of the
#     application, such as UI, services, and configuration management.
#     """
#
#     def __init__(self):
#         """
#         初始化 VisionDesk 应用程序实例。
#         Initialize the VisionDesk application instance.
#         """
#         setup_logger()
#         self.logger = logging.getLogger(__name__)
#         self.logger.info("初始化 VisionDesk 应用程序 | Initializing VisionDesk application")
#
#         self.config = Config()
#         self.qt_app: Optional[QtWidgets.QApplication] = None
#         self.main_window: Optional[MainWindow] = None
#
#     def start(self) -> None:
#         """
#         启动 VisionDesk 应用程序。
#         Start the VisionDesk application.
#
#         初始化 Qt 应用程序和主窗口，并进入应用程序的主事件循环。
#         Initializes the Qt application and main window, and enters the main event loop.
#         """
#         self.logger.info("启动 VisionDesk 应用程序 | Starting VisionDesk application")
#         self.qt_app = QtWidgets.QApplication([])
#         self.qt_app.setApplicationName("VisionDesk")
#
#         self.main_window = MainWindow(self.config)
#         self.main_window.show()
#
#         exit_code = self.qt_app.exec()
#         self.logger.info(f"应用程序退出，代码：{exit_code} | Application exited with code: {exit_code}")
#         return exit_code
#
#     def shutdown(self) -> None:
#         """
#         关闭 VisionDesk 应用程序。
#         Shut down the VisionDesk application.
#
#         执行必要的清理操作，如保存配置和关闭服务。
#         Performs necessary cleanup operations, such as saving configurations and shutting down services.
#         """
#         self.logger.info("关闭 VisionDesk 应用程序 | Shutting down VisionDesk application")
#         if self.main_window:
#             self.main_window.close()
#
#         # 保存配置，关闭服务等操作
#         # Save configuration, shut down services, etc.
#         self.config.save()
