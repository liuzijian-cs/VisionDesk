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
VisionDesk 应用设置模型模块。
VisionDesk application settings model module.

此模块定义了应用程序的所有设置项。
This module defines all settings for the application.
"""

# from typing import Dict, List, Optional
# from pydantic import BaseModel, Field
#
# from visiondesk.models.region import Region
#
#
# class AISettings(BaseModel):
#     """
#     AI 相关设置。
#     AI-related settings.
#     """
#
#     provider: str = Field(
#         default="openai",
#         description="AI 提供商名称 | AI provider name"
#     )
#
#     model_name: str = Field(
#         default="gpt-4o",
#         description="要使���的 AI 模型名称 | Name of the AI model to use"
#     )
#
#     api_key: Optional[str] = Field(
#         default=None,
#         description="API 密钥 | API key"
#     )
#
#     temperature: float = Field(
#         default=0.7,
#         ge=0.0,
#         le=2.0,
#         description="模型温度参数，控制随机性 | Model temperature parameter, controls randomness"
#     )
#
#     max_tokens: int = Field(
#         default=500,
#         ge=50,
#         le=4000,
#         description="回复的最大令牌数 | Maximum number of tokens in the response"
#     )
#
#
# class UISettings(BaseModel):
#     """
#     用户界面相关设置。
#     User interface related settings.
#     """
#
#     theme: str = Field(
#         default="system",
#         description="应用程序主题 (system, light, dark) | Application theme (system, light, dark)"
#     )
#
#     font_size: int = Field(
#         default=10,
#         ge=8,
#         le=18,
#         description="UI 字体大小 | UI font size"
#     )
#
#     overlay_opacity: float = Field(
#         default=0.85,
#         ge=0.1,
#         le=1.0,
#         description="浮窗透明度 | Overlay window opacity"
#     )
#
#     language: str = Field(
#         default="zh_CN",
#         description="应用程序语言 | Application language"
#     )
#
#
# class CaptureSettings(BaseModel):
#     """
#     屏幕捕获相关设置。
#     Screen capture related settings.
#     """
#
#     interval_seconds: int = Field(
#         default=5,
#         ge=1,
#         le=3600,
#         description="屏幕捕获间隔（秒） | Screen capture interval (seconds)"
#     )
#
#     auto_capture: bool = Field(
#         default=False,
#         description="是否启用自动捕获 | Whether to enable automatic capture"
#     )
#
#     capture_quality: int = Field(
#         default=85,
#         ge=1,
#         le=100,
#         description="JPEG 图像质量 | JPEG image quality"
#     )
#
#
# class Settings(BaseModel):
#     """
#     应用程序总体设置。
#     Overall application settings.
#     """
#
#     ai: AISettings = Field(default_factory=AISettings)
#     ui: UISettings = Field(default_factory=UISettings)
#     capture: CaptureSettings = Field(default_factory=CaptureSettings)
#
#     saved_regions: Dict[str, Region] = Field(
#         default_factory=dict,
#         description="保存的屏幕区域 | Saved screen regions"
#     )
#
#     startup_with_system: bool = Field(
#         default=False,
#         description="是否在系统启动时自动启动应用 | Whether to start the application automatically with the system"
#     )
#
#     update_check: bool = Field(
#         default=True,
#         description="是否自动检查更新 | Whether to automatically check for updates"
#     )
