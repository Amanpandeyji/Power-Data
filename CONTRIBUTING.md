# Contributing to Retail Sales Data Analytics Dashboard

First off, thank you for considering contributing to this project! 🎉

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples**
* **Describe the behavior you observed and expected**
* **Include Python version, OS, and package versions**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a detailed description of the suggested enhancement**
* **Explain why this enhancement would be useful**
* **List any alternatives you've considered**

### Your First Code Contribution

Unsure where to begin? You can start by looking through these issues:

* **Beginner issues** - issues which should only require a few lines of code
* **Help wanted issues** - issues which should be a bit more involved

### Pull Requests

* Fill in the required template
* Follow the Python style guidelines
* Include appropriate test cases
* Update documentation as needed
* End all files with a newline

## Getting Started

1. **Fork the repository**
   ```bash
   # Fork via GitHub UI, then clone your fork
   git clone https://github.com/YOUR-USERNAME/sales-data-analytics-dashboard.git
   cd sales-data-analytics-dashboard
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

3. **Set up your environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Make your changes**
   - Write clean, readable code
   - Add comments where necessary
   - Follow PEP 8 style guide

5. **Test your changes**
   ```bash
   python scripts/data_cleaning.py
   python scripts/quick_analysis.py
   ```

6. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Choose your branch
   - Fill in the PR template

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Update the requirements.txt if you add new dependencies
3. Increase version numbers in relevant files
4. Your PR will be merged once you have the approval of at least one maintainer

## Style Guidelines

### Python Style Guide

* Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
* Use 4 spaces for indentation (not tabs)
* Maximum line length of 100 characters
* Use docstrings for functions and classes
* Use meaningful variable names

Example:
```python
def calculate_profit_margin(sales, profit):
    """
    Calculate profit margin percentage.
    
    Args:
        sales (float): Total sales revenue
        profit (float): Total profit
    
    Returns:
        float: Profit margin as percentage
    """
    if sales == 0:
        return 0
    return (profit / sales) * 100
```

### Documentation Style Guide

* Use Markdown for documentation
* Keep line length reasonable (80-100 characters)
* Include code examples where helpful
* Update table of contents when adding sections

### Jupyter Notebook Guidelines

* Clear all outputs before committing
* Use meaningful cell titles
* Add markdown cells to explain your analysis
* Keep cells focused and not too long

## Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

* **feat**: A new feature
* **fix**: A bug fix
* **docs**: Documentation only changes
* **style**: Changes that don't affect code meaning (formatting, etc.)
* **refactor**: Code change that neither fixes a bug nor adds a feature
* **perf**: Performance improvement
* **test**: Adding missing tests
* **chore**: Changes to build process or auxiliary tools

### Examples

```
feat(analysis): add customer segmentation analysis

Added RFM analysis for customer segmentation with visualization

Closes #123
```

```
fix(cleaning): handle edge case in date parsing

Fixed issue where invalid date formats caused script to crash

Fixes #45
```

```
docs(readme): update installation instructions

Added troubleshooting section for Windows users
```

## Project Structure

```
sales-data-analytics-dashboard/
├── data/                  # Data files (not committed if large)
├── notebooks/             # Jupyter notebooks
├── scripts/               # Python scripts
├── dashboard/             # Power BI files
├── images/                # Images and visualizations
└── tests/                 # Test files (if added)
```

## Areas for Contribution

### High Priority
- [ ] Add unit tests
- [ ] Add data validation
- [ ] Improve error handling
- [ ] Add logging functionality

### Medium Priority
- [ ] Add more visualizations
- [ ] Implement ML forecasting
- [ ] Add interactive web dashboard
- [ ] Database integration

### Low Priority
- [ ] Add more sample datasets
- [ ] Create video tutorials
- [ ] Add internationalization
- [ ] Performance optimizations

## Questions?

Feel free to open an issue with the `question` label, or reach out to the maintainers directly.

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing! 🚀
