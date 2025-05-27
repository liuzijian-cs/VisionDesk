# Vision Desk

VisionDesk is an intelligent desktop assistant designed to periodically capture, analyse, and interpret the visual content displayed on your screen. By leveraging state-of-the-art multimodal AI models, it provides insightful responses based on specific screen regions selected by the user. The assistant features a non-intrusive, semi-transparent overlay window on the Windows desktop, keeping you informed in real time without distraction.

VisionDesk 是一款智能桌面助手，旨在周期性地捕获、分析并解读您屏幕上显示的视觉内容。通过利用最先进的多模态人工智能模型，它能根据用户选择的特定屏幕区域提供富有洞察力的回复。这款助手在 Windows 桌面上设有一个非侵入式、半透明的浮窗，让您在不分散注意力的情况下实时获取信息。


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
├── requirements.txt             # Python依赖列表
├── setup.py                     # 安装配置文件
├── .gitignore                   # Git忽略文件
├── .env.example                 # 环境变量示例
├── LICENSE                      # 许可证文件 Apache 2.0 License
│
├── .github/
│   ├── ISSUE_TEMPLATE
│   ├── workflows
│   │   └── ci.yml  
├── src/                         # 源代码目录
│   ├── __init__.py
│   ├── main.py                  # 程序入口
│   ├── app.py                   # 应用主类
│   │
│   ├── ui/                      # 用户界面模块
│   │   ├── __init__.py
│   │   ├── main_window.py       # 主窗口/系统托盘
│   │   ├── region_selector.py   # 区域选择器
│   │   ├── settings_dialog.py   # 设置对话框
│   │   ├── overlay_window.py    # 结果展示浮窗
│   │   └── resources/           # UI资源文件
│   │       ├── icons/           # 图标文件
│   │       └── styles/          # 样式表文件
│   │
│   ├── core/                    # 核心业务逻辑
│   │   ├── __init__.py
│   │   ├── screenshot.py        # 截图管理器
│   │   ├── ai_service.py        # AI服务封装
│   │   ├── scheduler.py         # 任务调度器
│   │   └── config_manager.py    # 配置管理器
│   │
│   ├── models/                  # 数据模型
│   │   ├── __init__.py
│   │   ├── region.py            # 区域数据模型
│   │   ├── task.py              # 任务数据模型
│   │   └── response.py          # AI响应模型
│   │
│   ├── utils/                   # 工具模块
│   │   ├── __init__.py
│   │   ├── image_utils.py       # 图像处理工具
│   │   ├── system_utils.py      # 系统相关工具
│   │   ├── logger.py            # 日志工具
│   │   └── constants.py         # 常量定义
│   │
│   └── data/                    # 数据存储
│       ├── cache/               # 图片缓存
│       ├── logs/                # 日志文件
│       └── config/              # 配置文件
│
├── tests/                       # 测试代码
│   ├── __init__.py
│   ├── test_screenshot.py
│   ├── test_ai_service.py
│   └── test_ui.py
│
├── docs/                        # 文档目录
│   ├── user_guide.md            # 用户指南
│   ├── developer_guide.md       # 开发者指南
│   └── api_reference.md         # API参考
│
├── scripts/                     # 脚本目录
│   ├── build.py                 # 构建脚本
│   └── install_deps.py          # 依赖安装脚本
│
└── dist/                        # 发布目录（构建后生成）
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.