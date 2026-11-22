"""Ví dụ minh họa cách ghi nhận giấy phép trong một repository học thuật."""

PROJECT = {
    "name": "BTH04 – Bản quyền nội dung số",
    "author": "Võ Thị Cẩm Ngân",
    "repository_license": "MIT",
    "studied_projects": {
        "GNU Bash": "GPL-3.0-or-later",
        "React": "MIT",
        "Apache Spark": "Apache-2.0",
    },
}

def print_license_matrix():
    for project, license_id in PROJECT["studied_projects"].items():
        print(f"{project}: {license_id}")

if __name__ == "__main__":
    print_license_matrix()
