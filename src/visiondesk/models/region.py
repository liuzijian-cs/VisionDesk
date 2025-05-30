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
VisionDesk 区域数据模型模块。
VisionDesk region data model module.

此模块定义了屏幕区域选择和捕获的数据模型。
This module defines data models for screen region selection and capture.
"""

from typing import Tuple, Optional
from pydantic import BaseModel, Field


class Region(BaseModel):
    """
    屏幕区域数据模型。
    Screen region data model.

    表示屏幕上被选择用于分析的矩形区域。
    Represents a rectangular region on screen that has been selected for analysis.
    """

    x: int = Field(description="区域左上角的 X 坐标 | X coordinate of the top-left corner of the region")
    y: int = Field(description="区域左上角的 Y 坐标 | Y coordinate of the top-left corner of the region")
    width: int = Field(gt=0, description="区域的宽度 | Width of the region")
    height: int = Field(gt=0, description="区域的高度 | Height of the region")
    name: Optional[str] = Field(default=None, description="区域的自定义名称 | Custom name for the region")

    @property
    def coordinates(self) -> Tuple[int, int, int, int]:
        """
        以元组形式返回区域坐标 (x, y, width, height)。
        Return the region coordinates as a tuple (x, y, width, height).

        返回:
            包含左上角坐标和尺寸的元组

        Returns:
            A tuple containing top-left coordinates and dimensions
        """
        return (self.x, self.y, self.width, self.height)

    @property
    def bounds(self) -> Tuple[int, int, int, int]:
        """
        以元组形式返回区域边界 (left, top, right, bottom)。
        Return the region bounds as a tuple (left, top, right, bottom).

        返回:
            包含区域边界坐标的元组

        Returns:
            A tuple containing the region boundary coordinates
        """
        return (self.x, self.y, self.x + self.width, self.y + self.height)

    def contains_point(self, x: int, y: int) -> bool:
        """
        检查给定点是否在区域内。
        Check if the given point is within the region.

        参数:
            x: 点的 X 坐标
            y: 点的 Y 坐标

        返回:
            如果点在区域内，则为 True；否则为 False

        Parameters:
            x: X coordinate of the point
            y: Y coordinate of the point

        Returns:
            True if the point is within the region, False otherwise
        """
        left, top, right, bottom = self.bounds
        return left <= x <= right and top <= y <= bottom

    def __str__(self) -> str:
        """
        返回区域的字符串表示形式。
        Return a string representation of the region.

        返回:
            区域的字符串表示

        Returns:
            String representation of the region
        """
        if self.name:
            return f"{self.name}: ({self.x}, {self.y}, {self.width} x {self.height})"
        else:
            return f"Region: ({self.x}, {self.y}, {self.width} x {self.height})"
