# Vision Desk

VisionDesk is an intelligent desktop assistant designed to periodically capture, analyse, and interpret the visual content displayed on your screen. By leveraging state-of-the-art multimodal AI models, it provides insightful responses based on specific screen regions selected by the user. The assistant features a non-intrusive, semi-transparent overlay window on the Windows desktop, keeping you informed in real time without distraction.

VisionDesk 是一款智能桌面助手，旨在周期性地捕获、分析并解读您屏幕上显示的视觉内容。通过利用最先进的多模态人工智能模型，它能根据用户选择的特定屏幕区域提供富有洞察力的回复。这款助手在 Windows 桌面上设有一个非侵入式、半透明的浮窗，让您在不分散注意力的情况下实时获取信息。




# 项目结构
VisionDesk
├─ .github/
│  ├─ workflows/ci.yml
│  └─ ISSUE_TEMPLATE/
├── src/
│   ├── main.py                     # 应用主入口点，启动 QApplication
│   ├── app_config.py               # 配置管理模块 (加载/保存 API Key, 区域, 频率等)
│   ├── gui/                        # GUI 相关的代码
│   │   ├── main_window.py          # 主应用窗口 (配置界面, 启动/停止按钮)
│   │   ├── region_selector.py      # 屏幕区域选择窗口
│   │   ├── overlay_window.py       # 半透明回复浮窗
│   │   └── __init__.py
│   ├── capture/                    # 屏幕截图模块
│   │   ├── screenshot.py           # 截图逻辑 (使用 mss)
│   │   ├── image_processor.py      # 图像处理 (Pillow, Base64 编码)
│   │   └── __init__.py
│   ├── llm/                        # LLM 交互模块
│   │   ├── llm_client.py        # OpenAI API 调用逻辑
│   │   └── __init__.py
│   ├── core/                       # 核心业务逻辑，协调各模块
│   │   ├── assistant_service.py    # 协调截图、LLM调用、更新浮窗的周期性服务
│   │   └── __init__.py
│   └── utils/                      # 通用工具函数 (如日志配置, 辅助函数)
│       ├── logger.py
│       └── __init__.py
├── config/
│   ├── settings.json               # 配置文件 (例如：截图区域, LLM设置, 频率)
│   └── api_keys.ini                # API Key 存储 (建议加密或从环境变量读取)
├── logs/
│   └── visiondesk.log              # 日志文件
├── assets/                         # 存放图标、图片等资源
│   └── icon.png
├── .gitignore                      # Git 忽略文件 (忽略venv, __pycache__, log文件等)
├── requirements.txt                # 项目依赖库列表
├── docs/
│   ├── 1_OverallTechnicalRoute.md
│   └── architecture.md
├── README.md
└── setup.py (Optional)             # 用于构建可分发的 Python 包


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.