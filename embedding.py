# embedding.py

from load_data import load_text
from get_model import get_embedding
import json
import time
from tqdm import tqdm

def main():
    # 指定需要读取的文件路径
    file_path = "strategy.txt"  # 请确保文件路径正确
    output_path = "output.json"  # 保存 embedding 结果的文件路径
    api_key = "sk-F3g5KjVFEbzyRaxUiAsrRwmPTsKGu76xoE3dQEzr0dkbh2Vj"  # 替换为你的实际 API 密钥

    # 加载文本内容
    text = load_text(file_path)
    if text is None:
        print("未能加载文本内容，程序终止。")
        return

    # 假设输入是句子的列表
    strategies = text.splitlines()
    print(f"加载的策略数量: {len(strategies)}")

    # 获取每个句子的 embedding
    results = []
    for idx, strategy in enumerate(tqdm(strategies, desc="Processing Strategies", ncols=80)):
        start_time = time.time()
        embedding_result = get_embedding(strategy, api_key)
        end_time = time.time()
        processing_time = end_time - start_time

        # 更新进度条描述，显示当前策略信息
        tqdm.write(f"处理策略 {idx} 耗时: {processing_time:.2f} 秒")

        if embedding_result is not None:
            if "data" in embedding_result and len(embedding_result["data"]) > 0:
                embedding = embedding_result["data"][0].get("embedding")
                if embedding:
                    results.append({
                        "id": f"strategy_{idx}",
                        "text": strategy,
                        "embedding": embedding
                    })
                else:
                    tqdm.write(f"警告: 返回结果中缺少 'embedding' 数据: {embedding_result}")
            else:
                tqdm.write(f"警告: 返回结果中缺少 'data' 字段或数据为空: {embedding_result}")
        else:
            tqdm.write(f"警告: 未能获取策略的 embedding: {strategy}")

    # 将结果保存到文件
    try:
        with open(output_path, 'w', encoding='utf-8') as output_file:
            json.dump(results, output_file, ensure_ascii=False, indent=4)
        print(f"Embedding 结果已保存到 {output_path}")
    except Exception as e:
        print(f"保存结果时发生错误: {e}")

if __name__ == "__main__":
    main()