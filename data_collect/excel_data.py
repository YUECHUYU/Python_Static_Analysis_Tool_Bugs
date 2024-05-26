import requests
import openpyxl
from datetime import datetime
import time

# GitHub API URL
# url = "https://api.github.com/repos/python/mypy/issues"
url = "https://api.github.com/repos/microsoft/pyright/issues"

# 参数设置，获取已关闭且带有 "bug" 标签的问题
params = {"state": "closed", "labels": "bug"}

# 请求头设置，记得将 YOUR_ACCESS_TOKEN 替换为你的GitHub个人访问令牌
headers = {"Authorization": "token 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", "Accept": "applicationnd.github.v3+json"}

# 获取问题数据
issues = []

# 循环处理所有的分页
while True:
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        issues.extend(response.json())

        # 检查是否有下一页
        if 'Link' in response.headers:
            link_header = response.headers['Link']
            next_page_url = next(
                (link.split(';')[0].strip('<> ') for link in link_header.split(',') if 'rel="next"' in link), None)
            if next_page_url:
                url = next_page_url
            else:
                # 如果没有下一页，则退出循环
                break
        else:
            # 如果没有 Link 头，则退出循环
            break

    else:
        print(f"Failed to retrieve issues. Status code: {response.status_code}")
        print(response.text)
        break

    # 在每次请求后添加1秒的延迟
    time.sleep(1)

# 创建一个新的 Excel 文件
workbook = openpyxl.Workbook()
sheet = workbook.active

# 写入表头
sheet.append(["Issue Number", "Title", "Opened At", "Closed At"])

# 写入数据
for issue in issues:
    issue_number = issue['number']
    title = issue['title']
    opened_at = issue['created_at']
    closed_at = issue['closed_at'] if issue['closed_at'] else "Not Closed"

    # 将日期时间字符串转换为 Excel 支持的日期时间格式
    opened_at = datetime.strptime(opened_at, "%Y-%m-%dT%H:%M:%SZ")
    closed_at = datetime.strptime(closed_at, "%Y-%m-%dT%H:%M:%SZ") if closed_at != "Not Closed" else None

    sheet.append([issue_number, title, opened_at, closed_at])

# 保存 Excel 文件
workbook.save("pyright_bug_report_data.xlsx")

print("Data written to pyright_bug_report_data.xlsx")