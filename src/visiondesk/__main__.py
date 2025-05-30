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
VisionDesk 命令行入口点模块。
VisionDesk command-line entry point module.

此模块提供了 VisionDesk 应用程序的命令行入口点，允许通过命令行启动应用程序。
This module provides the command-line entry point for the VisionDesk application,
allowing the app to be started from the command line.
"""

from visiondesk.main import main

if __name__ == "__main__":
    main()
