# Python Coding Challenges with PyTest

这是一个用于学习 **PyTest 测试框架** 和 **测试驱动开发 (TDD)** 的 Python 编程挑战项目。

## 项目简介

本项目包含一系列精心设计的 Python 编程练习，每个练习都配有完整的 PyTest 测试用例。通过实际编码练习，你将掌握 TDD 开发方法，提高代码质量和测试覆盖率。

## 项目结构

```
python_coding_challenges/
├── coding_solutions.py        # 编程挑战实现
├── tests/
│   └── test_solutions.py     # 测试用例
├── requirements.txt          # 项目依赖
├── .github/workflows/        # CI/CD 配置
└── README.md                 # 项目说明
```

## 编程挑战

项目包含 6 个核心编程挑战：

### 🔢 1. 列表操作：查找重复元素
- **目标**：实现一个函数，找出列表中所有出现多次的元素
- **技能点**：列表遍历、集合操作、去重

### 🔗 2. 集合运算：差集计算
- **目标**：计算两个集合的差集，返回只在第一个集合中的元素
- **技能点**：集合操作、数学运算

### 📦 3. 元组处理：元素平方
- **目标**：将元组中的每个数字元素进行平方运算
- **技能点**：元组操作、列表推导式、不可变性

### 🗂️ 4. 字典合并：键值求和
- **目标**：合并两个字典，相同键的值进行求和
- **技能点**：字典操作、键值处理、数据合并

### 📝 5. 面向对象：待办事项管理
- **目标**：实现一个简单的 ToDo 类，管理任务列表
- **技能点**：类设计、方法实现、封装性

### 🔄 6. 函数编程：列表展平
- **目标**：将嵌套列表（一层）展平为单一列表
- **技能点**：递归思维、类型检查、列表操作

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行所有测试
```bash
pytest tests/test_solutions.py -v
```

### 3. 运行特定测试
```bash
pytest tests/test_solutions.py::test_find_duplicates -v
```

### 4. 查看测试覆盖率
```bash
pytest tests/test_solutions.py --cov=coding_solutions --cov-report=html
```

## 测试结果

所有测试都应该通过：

- ✅ `test_find_duplicates` - 列表重复元素查找
- ✅ `test_difference_set` - 集合差集计算
- ✅ `test_square_tuple` - 元组元素平方
- ✅ `test_merge_dicts` - 字典合并求和
- ✅ `test_todo_class` - ToDo 类功能
- ✅ `test_flatten_list_once` - 列表展平

## 学习目标

通过完成这些编程挑战，你将学会：

- 🧠 **测试驱动开发**：先写测试，再写实现
- 📊 **PyTest 框架**：掌握测试用例编写和运行
- 🔍 **调试技能**：通过测试失败快速定位问题
- 🏗️ **代码架构**：编写可测试、可维护的代码
- 🚀 **CI/CD 实践**：自动化测试和持续集成

## 高级用法

### 参数化测试
```python
@pytest.mark.parametrize("input,expected", [
    ([1,2,2,3], [2]),
    ([], []),
    ([1,1,1,1], [1])
])
def test_find_duplicates_various_cases(input, expected):
    assert set(find_duplicates(input)) == set(expected)
```

### 异常测试
```python
def test_todo_remove_nonexistent():
    todo = ToDo()
    todo.remove_task("nonexistent")  # 应该不抛出异常
    assert todo.list_tasks() == []
```

## CI/CD 集成

项目配置了 GitHub Actions，每次推送代码时自动运行测试：

1. 进入 GitHub 仓库
2. 点击 "Actions" 标签页
3. 查看测试运行状态和结果

## 贡献指南

欢迎提交 Pull Request 来改进这个项目：

1. Fork 本仓库
2. 创建新的功能分支
3. 添加新的编程挑战和测试
4. 确保所有测试通过
5. 提交 Pull Request

## 作者

**Rhythmzd** - Python 开发者，专注于测试驱动开发和代码质量

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

---

💡 **提示**：建议按照 TDD 的方式完成每个挑战：先运行测试看到失败，然后编写最小代码让测试通过，最后重构优化。
