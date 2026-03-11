# Security Policy

## Supported Versions

We currently support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of this project seriously. If you discover a security vulnerability, please follow these steps:

### Where to Report

Please **DO NOT** create a public GitHub issue for security vulnerabilities.

Instead, please report security vulnerabilities by emailing:
- **Email**: [your.email@example.com]
- **Subject**: [SECURITY] Brief description of the vulnerability

### What to Include

When reporting a vulnerability, please include:

1. **Description**: A clear description of the vulnerability
2. **Impact**: What kind of impact could this vulnerability have?
3. **Reproduction Steps**: Detailed steps to reproduce the vulnerability
4. **Affected Versions**: Which versions of the project are affected?
5. **Suggested Fix**: If you have suggestions on how to fix the vulnerability
6. **Your Contact Information**: So we can follow up with questions

### Response Timeline

- **Acknowledgment**: Within 48 hours of your report
- **Initial Assessment**: Within 7 days
- **Fix Timeline**: Depending on severity:
  - Critical: Within 7 days
  - High: Within 14 days
  - Medium: Within 30 days
  - Low: Within 90 days

### Disclosure Policy

- We will work with you to understand and validate the vulnerability
- We will work on a fix and prepare a security advisory
- We will coordinate a disclosure timeline with you
- We will publicly acknowledge your responsible disclosure (unless you prefer to remain anonymous)

## Security Best Practices

### For Users

1. **Keep Dependencies Updated**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Use Virtual Environments**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Validate Input Data**
   - Always validate CSV files before processing
   - Be cautious with data from untrusted sources

4. **Protect Sensitive Data**
   - Never commit sensitive data to version control
   - Use `.gitignore` to exclude data files if they contain sensitive information
   - Be careful when sharing Power BI dashboards

### For Contributors

1. **Code Review**: All code changes require review before merging
2. **Dependency Management**: Keep dependencies up to date and minimal
3. **No Secrets in Code**: Never commit API keys, passwords, or other secrets
4. **Input Validation**: Always validate and sanitize input data
5. **Error Handling**: Implement proper error handling to prevent information leakage

## Known Security Considerations

### Data Privacy
- This project processes retail sales data
- Ensure compliance with data protection regulations (GDPR, CCPA, etc.)
- Anonymize or pseudonymize personal data when appropriate

### Dependencies
- We use third-party Python packages (pandas, numpy, etc.)
- We recommend regularly updating dependencies
- Check for known vulnerabilities in dependencies using tools like `safety`:
  ```bash
  pip install safety
  safety check -r requirements.txt
  ```

### Power BI Files
- `.pbix` files may contain embedded data
- Review data before sharing dashboards publicly
- Use Power BI's data protection features when necessary

## Security Tools

### Recommended Tools for Checking Security

```bash
# Install security tools
pip install safety bandit

# Check for known vulnerabilities in dependencies
safety check -r requirements.txt

# Check Python code for security issues
bandit -r scripts/
```

## Update Process

When a security vulnerability is fixed:

1. We will release a patched version
2. Update the CHANGELOG.md with security fix details
3. Publish a security advisory on GitHub
4. Notify users through GitHub releases and discussions

## Acknowledgments

We appreciate the security research community and will acknowledge researchers who responsibly disclose vulnerabilities (with their permission).

## Questions?

If you have questions about this security policy, please open a discussion on GitHub or contact the maintainers.

---

Thank you for helping keep this project and its users safe! 🔒
