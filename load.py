from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="Qwen/Qwen2.5-0.5B",
    local_dir="models/pretrained"
)

snapshot_download(
    repo_id="HuggingFaceH4/ultrachat_200k",
    repo_type="dataset",
    local_dir="datasets/sft"
)

snapshot_download(
    repo_id="HuggingFaceH4/ultrafeedback_binarized",
    repo_type="dataset",
    local_dir="datasets/dpo"
)
