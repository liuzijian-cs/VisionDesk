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
VisionDesk 快捷键管理器模块。
VisionDesk shortcut manager module.

此模块负责管理全局快捷键。
This module is responsible for managing global shortcuts.
"""

import logging
import sys
from typing import Dict, Callable, Any
from PySide6.QtCore import Qt, QObject
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication


class ShortcutManager(QObject):
    """
    全局快捷键管理器。
    Global shortcut manager.

    负责注册和管理应用程序的全局快捷键。
    Responsible for registering and managing global shortcuts for the application.
    """

    def __init__(self, parent: QObject = None):
        """
        初始化快捷键管理器。
        Initialize the shortcut manager.

        参数:
            parent: 父对象

        Parameters:
            parent: Parent object
        """
        super().__init__(parent)
        self.logger = logging.getLogger(__name__)
        self.shortcuts: Dict[str, QShortcut] = {}
        self.logger.info("快捷键管理器已初始化 | Shortcut manager initialized")

    def register_shortcut(self, shortcut_id: str, key_sequence: str, callback: Callable[[], None],
                          context: Qt.ShortcutContext = Qt.ApplicationShortcut) -> bool:
        """
        注册新的快捷键。
        Register a new shortcut.

        参数:
            shortcut_id: 快捷键的唯一标识符
            key_sequence: 快捷键序列，例如 "Ctrl+Alt+S"
            callback: 快捷键被激活时调用的函数
            context: 快捷键的上下文范围

        返回:
            如果注册成功返回 True，否则返回 False

        Parameters:
            shortcut_id: Unique identifier for the shortcut
            key_sequence: Key sequence, e.g. "Ctrl+Alt+S"
            callback: Function to call when the shortcut is activated
            context: Context scope for the shortcut

        Returns:
            True if registration was successful, False otherwise
        """
        if shortcut_id in self.shortcuts:
            self.logger.warning(f"快捷键 '{shortcut_id}' 已存在 | Shortcut '{shortcut_id}' already exists")
            return False

        try:
            # 创建快捷键对象
            # Create shortcut object
            app = QApplication.instance()
            shortcut = QShortcut(QKeySequence(key_sequence), app.activeWindow())
            shortcut.setContext(context)
            shortcut.activated.connect(callback)

            # 存储快捷键引用
            # Store shortcut reference
            self.shortcuts[shortcut_id] = shortcut

            self.logger.info(f"已注册快捷键 '{shortcut_id}': {key_sequence} | Registered shortcut '{shortcut_id}': {key_sequence}")
            return True
        except Exception as e:
            self.logger.error(f"注册快捷键 '{shortcut_id}' 失败: {e} | Failed to register shortcut '{shortcut_id}': {e}")
            return False

    def unregister_shortcut(self, shortcut_id: str) -> bool:
        """
        注销已注册的快捷键。
        Unregister a registered shortcut.

        参数:
            shortcut_id: 快捷键的唯一标识符

        返回:
            如果注销成功返回 True，否则返回 False

        Parameters:
            shortcut_id: Unique identifier for the shortcut

        Returns:
            True if unregistration was successful, False otherwise
        """
        if shortcut_id not in self.shortcuts:
            self.logger.warning(f"快捷键 '{shortcut_id}' 不存在 | Shortcut '{shortcut_id}' does not exist")
            return False

        try:
            # 删除快捷键
            # Delete shortcut
            shortcut = self.shortcuts.pop(shortcut_id)
            shortcut.setEnabled(False)
            shortcut.deleteLater()

            self.logger.info(f"已注销快捷键 '{shortcut_id}' | Unregistered shortcut '{shortcut_id}'")
            return True
        except Exception as e:
            self.logger.error(f"注销快捷键 '{shortcut_id}' 失败: {e} | Failed to unregister shortcut '{shortcut_id}': {e}")
            self.shortcuts.pop(shortcut_id, None)  # 确保从字典中移除
            return False

    def is_shortcut_registered(self, shortcut_id: str) -> bool:
        """
        检查快捷键是否已注册。
        Check if a shortcut is registered.

        参数:
            shortcut_id: 快捷键的唯一标识符

        返回:
            如果快捷键已注册返回 True，否则返回 False

        Parameters:
            shortcut_id: Unique identifier for the shortcut

        Returns:
            True if the shortcut is registered, False otherwise
        """
        return shortcut_id in self.shortcuts

    def clear_all_shortcuts(self) -> None:
        """
        清除所有已注册的快捷���。
        Clear all registered shortcuts.
        """
        try:
            # 复制快捷键 ID 列表以避免在迭代过程中修改字典
            # Copy shortcut ID list to avoid modifying the dictionary during iteration
            shortcut_ids = list(self.shortcuts.keys())

            for shortcut_id in shortcut_ids:
                self.unregister_shortcut(shortcut_id)

            self.logger.info("已清除所有快捷键 | Cleared all shortcuts")
        except Exception as e:
            self.logger.error(f"清除所有快捷键时发生错误: {e} | Error occurred while clearing all shortcuts: {e}")
