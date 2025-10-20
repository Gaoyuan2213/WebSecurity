# merge_jsonl.py
import os

# 输入文件列表
input_files = ["out_basic.jsonl", "out_dns.jsonl"]  # M1生成的JSONL文件
output_file = "logs/detections.jsonl"  # M2默认读取路径

# 确保 logs 文件夹存在
os.makedirs("logs", exist_ok=True)

with open(output_file, "w", encoding="utf-8") as out_f:
    for fname in input_files:
        with open(fname, "r", encoding="utf-8") as in_f:
            for line in in_f:
                out_f.write(line)

print(f"Merged {len(input_files)} files into {output_file}")
