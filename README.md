# Vision Desk

VisionDesk is an intelligent desktop assistant designed to periodically capture, analyse, and interpret the visual content displayed on your screen. By leveraging state-of-the-art multimodal AI models, it provides insightful responses based on specific screen regions selected by the user. The assistant features a non-intrusive, semi-transparent overlay window on the Windows desktop, keeping you informed in real time without distraction.

VisionDesk 是一款智能桌面助手，旨在周期性地捕获、分析并解读您屏幕上显示的视觉内容。通过利用最先进的多模态人工智能模型，它能根据用户选择的特定屏幕区域提供富有洞察力的回复。这款助手在 Windows 桌面上设有一个非侵入式、半透明的浮窗，让您在不分散注意力的情况下实时获取信息。

## Python 开发环境
```shell
conda create -n visdesk python=3.12
conda activate visdesk
pip install -e ".[dev]"  # 安装所有开发依赖
```

## 技术选型

- 编程语言： Python 3.12
- GUI框架： PySide6
- 屏幕捕获： mss (高性能跨平台截图库)
- 图像处理： Pillow (PIL)
- AI集成： OpenAI Python SDK
- 异步处理： asyncio + threading
- 配置管理： pydantic
- 日志系统： Python logging
- 打包工具： PyInstaller

## 代码质量控制
- ruff: 代码风格检查和静态分析
- black: 代码格式化
- mypy: 类型检查
- pytest: 单元测试和集成测试

## 优化后的项目结构
```
VisionDesk/
├── README.md                                  # 项目说明文档
├── LICENSE                                    # Apache 2.0 许可证
├── pyproject.toml                             # 现代Python项目配置
├── .gitignore                                 # Git忽略文件
├── .env.example                               # 环境变量示例
├── .pre-commit-config.yaml                    # 预提交钩子配置
│
├── .github/                                   # GitHub配置
│   ├── ISSUE_TEMPLATE/                        # Issue模板
│   │   ├── bug_report.md                      # Bug报告模板
│   │   ├── feature_request.md                 # 功能请求模板
│   │   └── question.md                        # 问题模板
│   ├── PULL_REQUEST_TEMPLATE.md               # Pull Request模板
│   └── workflows/                             # GitHub Actions 工作流程
│       ├── ci.yml                             # 持续集成
│       ├── release.yml                        # 发布流程
│       └── docs.yml                           # 文档构建
│
├── src/                                       # 源代码根目录
│   └── visiondesk/                            # 源代码主包
│       ├── __init__.py                        # 包初始化
│       ├── __main__.py                        # 命令行入口点
│       ├── main.py                            # 程序主入口点
│       ├── app.py                             # 应用主类
│       │
│       ├── ui/                                # 用户界面模块
│       │   ├── __init__.py                    # 包初始化
│       │   ├── components/                    # UI组件
│       │   │   ├── __init__.py                # 包初始化
│       │   │   ├── main_window.py             # 主窗口
│       │   │   ├── region_selector.py         # 区域选择器
│       │   │   └── overlay_window.py          # 结果展示浮窗
│       │   ├── shortcuts/                     # 快捷键管理
│       │   │   ├── __init__.py                # 包初始化
│       │   │   └── shortcut_manager.py        # 快捷键管理器
│       │   └── resources/                     # UI资源文件 (非代码)
│       │       ├── icons/                     # 图标文件
│       │       ├── styles/                    # 样式表文件
│       │       └── translations/              # 国际化文件
│       │
│       ├── core/                              # 核心业务逻辑
│       │   ├── __init__.py                    # 包初始化
│       │   ├── services/                      # 服务实现
│       │   │   ├── __init__.py                # 包初始化
│       │   │   ├── screenshot_service.py      # 屏幕截图服务
│       │   │   └── ai_service.py              # AI服务
│       │   └── config.py                      # 配置管理
│       │
│       ├── ai/                                # AI集成
│       │   ├── __init__.py                    # 包初始化
│       │   ├── providers/                     # AI提供商
│       │   │   ├── __init__.py                # 包初始化
│       │   │   ├── base.py                    # 提供商基类
│       │   │   └── openai.py                  # OpenAI提供商
│       │   └── models/                        # AI模型抽象
│       │       ├── __init__.py                # 包初始化
│       │       └── vision_model.py            # 视觉模型
│       │
│       ├── models/                            # 数据模型 (Pydantic等)
│       │   ├── __init__.py                    # 包初始化
│       │   ├── region.py                      # 区域数据模型
│       │   └── settings.py                    # 应用设置模型
│       │
│       └── utils/                             # 工具函数
│           ├── __init__.py                    # 包初始化
│           ├── image_utils.py                 # 图像处理工具
│           ├── logger.py                      # 日志工具
│           ├── constants.py                   # 常量定义
│           └── decorators.py                  # 通用装饰器
│
├── tests/                                     # 测试代码
│   ├── __init__.py                            # 包初始化
│   ├── conftest.py                            # pytest配置
│   ├── unit/                                  # 单元测试
│   │   └── __init__.py                        # 包初始化
│   └── integration/                           # 集成测试
│       └── __init__.py                        # 包初始化
│
└── docs/                                      # 文档目录
    └── 1_OverallTechnicalRoute.md             # 技术路线概述
```

# Copyright 2025 刘子健_LiuZijian
#
# This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
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

# GenAI Declaration:
- ChatGPT, Claude, Gemini and other AI tools were used to assist in writing code, documentation, and project structure.

