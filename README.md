# GitHub Actions 自动测试实验

《开源软件设计与开发》实验二的第一部分，使用 Python 和 pytest 验证 GitHub Actions 持续集成。

## 项目文件

- `calculator.py`：加法和乘法函数。
- `test_calculator.py`：2个测试函数，覆盖4条断言。
- `.github/workflows/ci.yml`：push、pull_request 或手动运行时执行测试。

## 本地运行

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

## 实验过程

1. 提交正确实现，观察测试通过。
2. 将加法函数暂时改为乘法，提交后观察失败日志。
3. 修复加法，重新提交，确认最后一次工作流成功。

运行结果以仓库 Actions 页面实际记录为准。
