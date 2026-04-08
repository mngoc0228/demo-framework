# init dự án từ đầu với uv
```
- uv init | option chọn python version "uv init --python 3.12"
```

# khởi tạo môi trường ảo .venv với uv
```
- uv venv --python 3.12
- source .venv\Scripts\activate
```

# cài đặt package(gói) ví dụ như pytest, selenium, ...
```
- uv add pytest selenium
```

# để chạy file python với uv
```
- uv run main.py || uv run example.py
```