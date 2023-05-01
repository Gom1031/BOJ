import io
import sys
import contextlib

output_buffer = io.StringIO()

# 표준 출력을 output_buffer로 리디렉션
with contextlib.redirect_stdout(output_buffer):
    try:
        print(2 ** int(input()))
    except:
        pass

# 출력 캡처
output = output_buffer.getvalue()

# 출력 길이를 확인하고 출력 초과가 발생하지 않은 경우에만 표준 출력으로 출력
if len(output) <= 4300:
    sys.stdout.write(output)
else:
    sys.stdout.write("출력 초과")
