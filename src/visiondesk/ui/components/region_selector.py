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
VisionDesk 区域选择器模块。
VisionDesk region selector module.

此模块提供屏幕区域选择功能。
This module provides screen region selection functionality.
"""

# import logging
# from typing import Optional, Tuple, Callable
#
# from PySide6.QtCore import Qt, QRect, QPoint, Signal, QObject
# from PySide6.QtGui import QColor, QPainter, QPen, QBrush, QMouseEvent, QKeyEvent
# from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QDialog
#
# from visiondesk.models.region import Region
#
#
# class RegionSelectorOverlay(QWidget):
#     """
#     屏幕区域选择覆盖层。
#     Screen region selection overlay.
#
#     允许用户通过拖动鼠标在屏幕上选择矩形区域。
#     Allows users to select a rectangular region on screen by dragging the mouse.
#     """
#
#     region_selected = Signal(Region)
#     selection_canceled = Signal()
#
#     def __init__(self, parent: Optional[QWidget] = None):
#         """
#         初始化区域选择覆盖层。
#         Initialize the region selection overlay.
#
#         参数:
#             parent: 父窗口小部件
#
#         Parameters:
#             parent: Parent widget
#         """
#         super().__init__(parent)
#
#         self.logger = logging.getLogger(__name__)
#         self.logger.info("初始化区域选择器覆盖层 | Initializing region selector overlay")
#
#         self.start_point = QPoint()
#         self.end_point = QPoint()
#         self.is_selecting = False
#
#         # 设置窗口属性
#         # Set window properties
#         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
#         self.setAttribute(Qt.WA_TranslucentBackground)
#         self.setMouseTracking(True)
#
#         # 设置覆盖整个屏幕
#         # Set to cover the entire screen
#         screen_geometry = QApplication.primaryScreen().geometry()
#         self.setGeometry(screen_geometry)
#
#         self.logger.debug(f"区域选择覆盖层覆盖屏幕: {screen_geometry.width()}x{screen_geometry.height()} | "
#                         f"Region selection overlay covering screen: {screen_geometry.width()}x{screen_geometry.height()}")
#
#     def paintEvent(self, event) -> None:
#         """
#         绘制覆盖层和选择区域。
#         Draw the overlay and selection area.
#         """
#         painter = QPainter(self)
#
#         # 设置半透明背景
#         # Set semi-transparent background
#         painter.fillRect(self.rect(), QColor(0, 0, 0, 100))
#
#         # 如果正在选择，绘制选择框
#         # If selecting, draw selection box
#         if self.is_selecting:
#             selected_rect = QRect(self.start_point, self.end_point).normalized()
#
#             # 绘制选中区域（将其从背景中"挖出"，使其更透明）
#             # Draw selected area (make it more transparent by "cutting out" from the background)
#             painter.setCompositionMode(QPainter.CompositionMode_Clear)
#             painter.fillRect(selected_rect, Qt.transparent)
#
#             # 绘制选择框边框
#             # Draw selection box border
#             painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
#             painter.setPen(QPen(QColor(0, 120, 215), 2, Qt.SolidLine))
#             painter.drawRect(selected_rect)
#
#             # 绘制尺寸信息
#             # Draw dimension information
#             text = f"{selected_rect.width()} x {selected_rect.height()}"
#             painter.setPen(QPen(QColor(255, 255, 255), 1))
#             text_rect = painter.fontMetrics().boundingRect(text)
#
#             # 确保文本位于选择框内部或附近但始终可见
#             # Ensure text is inside or near the selection box but always visible
#             if selected_rect.width() > text_rect.width() + 10 and selected_rect.height() > text_rect.height() + 5:
#                 # 在选择框内部绘制文本
#                 # Draw text inside the selection box
#                 text_x = selected_rect.x() + 5
#                 text_y = selected_rect.y() + text_rect.height() + 5
#             else:
#                 # 在选择框上方绘制文本
#                 # Draw text above the selection box
#                 text_x = selected_rect.x()
#                 text_y = selected_rect.y() - 5
#
#             # 绘制文本背景以提高可读性
#             # Draw text background to improve readability
#             bg_rect = QRect(text_x - 2, text_y - text_rect.height() - 2, text_rect.width() + 4, text_rect.height() + 4)
#             painter.fillRect(bg_rect, QColor(0, 0, 0, 180))
#
#             # 绘制文本
#             # Draw text
#             painter.drawText(text_x, text_y, text)
#
#     def mousePressEvent(self, event: QMouseEvent) -> None:
#         """
#         处理鼠标按下事件，开始选择区域。
#         Handle mouse press event, start region selection.
#
#         参数:
#             event: 鼠标事件对象
#
#         Parameters:
#             event: Mouse event object
#         """
#         if event.button() == Qt.LeftButton:
#             self.is_selecting = True
#             self.start_point = event.pos()
#             self.end_point = self.start_point
#             self.logger.debug(f"开始选择区域，起点: ({self.start_point.x()}, {self.start_point.y()}) | "
#                             f"Started region selection, start point: ({self.start_point.x()}, {self.start_point.y()})")
#             self.update()
#
#     def mouseMoveEvent(self, event: QMouseEvent) -> None:
#         """
#         处理鼠标移动事件，更新选择区域。
#         Handle mouse move event, update selection area.
#
#         参数:
#             event: 鼠标事件对象
#
#         Parameters:
#             event: Mouse event object
#         """
#         if self.is_selecting:
#             self.end_point = event.pos()
#             self.update()
#
#     def mouseReleaseEvent(self, event: QMouseEvent) -> None:
#         """
#         处理鼠标释放事件，完成区域选择。
#         Handle mouse release event, complete region selection.
#
#         参数:
#             event: 鼠标事件对象
#
#         Parameters:
#             event: Mouse event object
#         """
#         if event.button() == Qt.LeftButton and self.is_selecting:
#             self.is_selecting = False
#             selected_rect = QRect(self.start_point, self.end_point).normalized()
#
#             # 如果选择的区域太小，则视为无效选择
#             # If the selected area is too small, consider it an invalid selection
#             if selected_rect.width() < 10 or selected_rect.height() < 10:
#                 self.logger.debug("选择的区域太小，忽略 | Selected region too small, ignoring")
#                 self.close()
#                 self.selection_canceled.emit()
#                 return
#
#             # 创建区域对象并发出信号
#             # Create region object and emit signal
#             region = Region(
#                 x=selected_rect.x(),
#                 y=selected_rect.y(),
#                 width=selected_rect.width(),
#                 height=selected_rect.height()
#             )
#             self.logger.info(f"已选择区域: {region} | Selected region: {region}")
#             self.region_selected.emit(region)
#             self.close()
#
#     def keyPressEvent(self, event: QKeyEvent) -> None:
#         """
#         处理键盘按下事件，允许用户取消选择。
#         Handle key press event, allows user to cancel selection.
#
#         参数:
#             event: 键盘事件对象
#
#         Parameters:
#             event: Key event object
#         """
#         # 如果按下 Esc 键，取消选择
#         # If Esc key is pressed, cancel selection
#         if event.key() == Qt.Key_Escape:
#             self.logger.info("用户取消了区域选择 | User canceled region selection")
#             self.close()
#             self.selection_canceled.emit()
#         else:
#             super().keyPressEvent(event)
#
#
# class RegionSelector(QObject):
#     """
#     区域选择器管理类。
#     Region selector manager class.
#
#     管理屏幕区域选择过程。
#     Manages the screen region selection process.
#     """
#
#     def __init__(self, parent: Optional[QObject] = None):
#         """
#         初始化区域选择器。
#         Initialize the region selector.
#
#         参数:
#             parent: 父对象
#
#         Parameters:
#             parent: Parent object
#         """
#         super().__init__(parent)
#         self.logger = logging.getLogger(__name__)
#         self.overlay: Optional[RegionSelectorOverlay] = None
#
#     def select_region(self, callback: Callable[[Optional[Region]], None]) -> None:
#         """
#         启动区域选择过程。
#         Start the region selection process.
#
#         参数:
#             callback: 选择完成后的回调函数，接收已选区域或 None（如果取消）
#
#         Parameters:
#             callback: Callback function after selection completes, receives selected region or None (if canceled)
#         """
#         self.logger.info("启动区域选择过程 | Starting region selection process")
#
#         # 创建并显示覆盖层
#         # Create and show overlay
#         self.overlay = RegionSelectorOverlay()
#         self.overlay.region_selected.connect(lambda region: callback(region))
#         self.overlay.selection_canceled.connect(lambda: callback(None))
#         self.overlay.show()
#
#     def cancel_selection(self) -> None:
#         """
#         取消当前的区域选择过程。
#         Cancel the current region selection process.
#         """
#         if self.overlay and self.overlay.isVisible():
#             self.logger.info("取消区域选择过程 | Canceling region selection process")
#             self.overlay.close()
#             self.overlay = None
