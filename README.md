# Vision Desk

VisionDesk is an intelligent desktop assistant designed to periodically capture, analyse, and interpret the visual content displayed on your screen. By leveraging state-of-the-art multimodal AI models, it provides insightful responses based on specific screen regions selected by the user. The assistant features a non-intrusive, semi-transparent overlay window on the Windows desktop, keeping you informed in real time without distraction.

VisionDesk 是一款智能桌面助手，旨在周期性地捕获、分析并解读您屏幕上显示的视觉内容。通过利用最先进的多模态人工智能模型，它能根据用户选择的特定屏幕区域提供富有洞察力的回复。这款助手在 Windows 桌面上设有一个非侵入式、半透明的浮窗，让您在不分散注意力的情况下实时获取信息。

# Python 开发环境
```shell
conda create -n visdesk python=3.12
conda activate visdesk
pip install PySide6 -i https://mirrors.aliyun.com/pypi/simple



```

# 技术路线

主要技术选型：
- 编程语言： Python 3.12
- GUI框架： PySide6
- 屏幕捕获： mss (高性能跨平台截图库)
- 图像处理： Pillow (PIL)
- AI集成： OpenAI Python SDK
- 异步处理： asyncio + threading
- 配置管理： configparser / JSON
- 日志系统： Python logging
- 打包工具： PyInstaller



# 项目结构
```
VisionDesk/
├── README.md                    # 项目说明文档
├── LICENSE                      # Apache 2.0 许可证
├── pyproject.toml               # 现代Python项目配置
├── requirements.txt             # 基础依赖
├── requirements-dev.txt         # 开发依赖
├── .gitignore                   # Git忽略文件
├── .env.example                 # 环境变量示例
├── .pre-commit-config.yaml      # 预提交钩子配置
│
├── .github/                     # GitHub配置
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── question.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       ├── ci.yml               # 持续集成
│       ├── release.yml          # 发布流程
│       └── docs.yml             # 文档构建
│
├── src/visiondesk/              # 源代码目录（包名）
│   ├── __init__.py
│   ├── main.py                  # 程序入口
│   ├── app.py                   # 应用主类
│   │
│   ├── ui/                      # 用户界面模块
│   │   ├── __init__.py
│   │   ├── components/          # UI组件
│   │   │   ├── __init__.py
│   │   │   ├── main_window.py   # 主窗口/系统托盘
│   │   │   ├── region_selector.py # 区域选择器
│   │   │   ├── settings_dialog.py # 设置对话框
│   │   │   └── overlay_window.py   # 结果展示浮窗
│   │   ├── themes/              # 主题系统
│   │   │   ├── __init__.py
│   │   │   ├── base_theme.py
│   │   │   ├── dark_theme.py
│   │   │   └── light_theme.py
│   │   ├── shortcuts/           # 快捷键管理
│   │   │   ├── __init__.py
│   │   │   └── shortcut_manager.py
│   │   └── resources/           # UI资源文件
│   │       ├── icons/           # 图标文件
│   │       ├── styles/          # 样式表文件
│   │       └── translations/    # 国际化文件
│   │
│   ├── core/                    # 核心业务逻辑
│   │   ├── __init__.py
│   │   ├── interfaces/          # 接口定义
│   │   │   ├── __init__.py
│   │   │   ├── ai_provider.py   # AI提供商接口
│   │   │   ├── screenshot_provider.py # 截图提供商接口
│   │   │   └── storage_provider.py    # 存储提供商接口
│   │   ├── services/            # 服务实现
│   │   │   ├── __init__.py
│   │   │   ├── screenshot_service.py  # 截图服务
│   │   │   ├── ai_service.py          # AI服务
│   │   │   ├── cache_service.py       # 缓存服务
│   │   │   ├── security_service.py    # 安全服务
│   │   │   └── privacy_service.py     # 隐私服务
│   │   ├── events/              # 事件系统
│   │   │   ├── __init__.py
│   │   │   ├── event_bus.py     # 事件总线
│   │   │   ├── event_types.py   # 事件类型定义
│   │   │   └── handlers/        # 事件处理器
│   │   │       └── __init__.py
│   │   ├── di/                  # 依赖注入
│   │   │   ├── __init__.py
│   │   │   ├── container.py     # DI容器
│   │   │   └── decorators.py    # DI装饰器
│   │   ├── scheduler.py         # 任务调度器
│   │   └── config_manager.py    # 配置管理器
│   │
│   ├── plugins/                 # 插件系统
│   │   ├── __init__.py
│   │   ├── base_plugin.py       # 插件基类
│   │   ├── plugin_manager.py    # 插件管理器
│   │   ├── ai_providers/        # AI提供商插件
│   │   │   ├── __init__.py
│   │   │   ├── openai_provider.py
│   │   │   ├── anthropic_provider.py
│   │   │   └── local_provider.py
│   │   └── extensions/          # 扩展插件
│   │       └── __init__.py
│   │
│   ├── models/                  # 数据模型
│   │   ├── __init__.py
│   │   ├── region.py            # 区域数据模型
│   │   ├── task.py              # 任务数据模型
│   │   ├── response.py          # AI响应模型
│   │   ├── config.py            # 配置模型
│   │   └── events.py            # 事件模型
│   │
│   ├── utils/                   # 工具模块
│   │   ├── __init__.py
│   │   ├── image_utils.py       # 图像处理工具
│   │   ├── system_utils.py      # 系统相关工具
│   │   ├── crypto_utils.py      # 加密工具
│   │   ├── compression_utils.py # 压缩工具
│   │   ├── logger.py            # 日志工具
│   │   ├── constants.py         # 常量定义
│   │   └── decorators.py        # 通用装饰器
│   │
│   └── storage/                 # 存储层
│       ├── __init__.py
│       ├── cache/               # 缓存实现
│       │   ├── __init__.py
│       │   ├── memory_cache.py
│       │   └── disk_cache.py
│       ├── database/            # 数据库（SQLite）
│       │   ├── __init__.py
│       │   ├── models.py
│       │   └── migrations/
│       └── file_storage/        # 文件存储
│           ├── __init__.py
│           └── local_storage.py
│
├── tests/                       # 测试代码
│   ├── __init__.py
│   ├── conftest.py              # pytest配置
│   ├── unit/                    # 单元测试
│   │   ├── __init__.py
│   │   ├── test_core/
│   │   ├── test_ui/
│   │   ├── test_plugins/
│   │   └── test_utils/
│   ├── integration/             # 集成测试
│   │   ├── __init__.py
│   │   └── test_workflows/
│   └── fixtures/                # 测试数据
│       ├── images/
│       └── configs/
│
├── docs/                        # 文档目录
│   ├── index.md                 # 文档首页
│   ├── installation.md         # 安装指南
│   ├── user_guide/              # 用户指南
│   │   ├── getting_started.md
│   │   ├── configuration.md
│   │   └── troubleshooting.md
│   ├── developer_guide/         # 开发者指南
│   │   ├── architecture.md
│   │   ├── plugin_development.md
│   │   └── contributing.md
│   ├── api_reference/           # API参考
│   │   ├── core.md
│   │   ├── plugins.md
│   │   └── utils.md
│   └── examples/                # 示例代码
│       ├── basic_usage.py
│       └── plugin_example.py
│
├── scripts/                     # 脚本目录
│   ├── build.py                 # 构建脚本
│   ├── install_deps.py          # 依赖安装脚本
│   ├── setup_dev.py             # 开发环境设置
│   └── release.py               # 发布脚本
│
├── examples/                    # 使用示例
│   ├── basic_usage.py
│   ├── custom_plugin.py
│   └── advanced_config.py
│
└── dist/                        # 发布目录（构建后生成）

```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```text
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

```