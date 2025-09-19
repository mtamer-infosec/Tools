import subprocess

while True:
    try:
        command = input("> ").lower()

        if command in ("exit", "stop"):
            break

        # تنفيذ الأمر مع تجاهل أي إخراج للخطأ
        subprocess.run(command, shell=True)
    except Exception:
        # أي خطأ غير متوقع يتم تجاهله
        continue
