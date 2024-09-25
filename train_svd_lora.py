Fix AttributeError in train_svd_lora.py: add missing save_lora_weights function

Resolved an issue where StableVideoDiffusionPipeline was missing the 'save_lora_weights' function, causing an AttributeError. Added the necessary import from diffusers.loaders to enable Lora fine-tuning.
