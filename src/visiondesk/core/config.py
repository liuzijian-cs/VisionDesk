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
VisionDesk 配置管理模块。
VisionDesk configuration management module.

此模块负责管理应用程序的配置设置，包括加载、保存和访问配置项。
This module is responsible for managing application configuration settings,
including loading, saving, and accessing configuration items.
"""

import json
import os
import logging
from pathlib import Path
from typing import Dict, Any, Optional

from visiondesk.models.settings import Settings


class Config:
    """
    应用程序配置管理类。
    Application configuration management class.

    负责处理应用程序设置的加载、保存和访问。
    Responsible for handling the loading, saving, and accessing of application settings.
    """

    def __init__(self, config_path: Optional[str] = None):
        """
        初始化配置管理器。
        Initialize the configuration manager.

        参数:
            config_path: 配置文件的路径。如果未提供，则使用默认路径。

        Parameters:
            config_path: Path to the configuration file. If not provided, a default path is used.
        """
        self.logger = logging.getLogger(__name__)

        if config_path is None:
            # 使用默认配置路径（用户主目录下的.visiondesk文件夹）
            # Use default config path (in .visiondesk folder in user's home directory)
            home_dir = Path.home()
            self.config_dir = home_dir / ".visiondesk"
            self.config_file = self.config_dir / "config.json"
        else:
            self.config_file = Path(config_path)
            self.config_dir = self.config_file.parent

        # 确保配置目录存在
        # Ensure the configuration directory exists
        os.makedirs(self.config_dir, exist_ok=True)

        # 初始化设置
        # Initialize settings
        self.settings = Settings()

        # 加载配置（如果存在）
        # Load configuration (if exists)
        self.load()

    def load(self) -> None:
        """
        从配置文件加载设置。
        Load settings from the configuration file.
        """
        if not self.config_file.exists():
            self.logger.info(f"配置文件不存在，使用默认设置 | Configuration file does not exist, using default settings")
            return

        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config_data = json.load(f)

            # 将加载的数据应用到设置对象
            # Apply loaded data to settings object
            self.settings = Settings.model_validate(config_data)
            self.logger.info(f"已从 {self.config_file} 加载配置 | Configuration loaded from {self.config_file}")
        except Exception as e:
            self.logger.error(f"加载配置时出错: {e} | Error loading configuration: {e}")

    def save(self) -> None:
        """
        将当前设置保存到配置文件。
        Save current settings to the configuration file.
        """
        try:
            # 将设置序列化为JSON
            # Serialize settings to JSON
            config_data = self.settings.model_dump(mode='json')

            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, indent=2, ensure_ascii=False)

            self.logger.info(f"已将配置保存至 {self.config_file} | Configuration saved to {self.config_file}")
        except Exception as e:
            self.logger.error(f"保存配置时出错: {e} | Error saving configuration: {e}")

    def get(self, section: str, key: str, default: Any = None) -> Any:
        """
        获取配置值。
        Get a configuration value.

        参数:
            section: 配置部分名称
            key: 配置键名
            default: 如果键不存在，则返回的默认值

        返回:
            配置值或默认值

        Parameters:
            section: Configuration section name
            key: Configuration key name
            default: Default value to return if the key doesn't exist

        Returns:
            Configuration value or default value
        """
        try:
            section_data = getattr(self.settings, section, {})
            return getattr(section_data, key, default)
        except AttributeError:
            return default

    def set(self, section: str, key: str, value: Any) -> None:
        """
        设置配置值。
        Set a configuration value.

        参数:
            section: 配置部分名称
            key: 配置键名
            value: 要设置的值

        Parameters:
            section: Configuration section name
            key: Configuration key name
            value: Value to set
        """
        try:
            section_data = getattr(self.settings, section)
            setattr(section_data, key, value)
        except AttributeError:
            self.logger.error(f"无法设置配置 {section}.{key}: 部分或键不存在 | Cannot set configuration {section}.{key}: section or key does not exist")
