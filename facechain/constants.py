neg_prompt = 'nsfw, paintings, sketches, (worst quality:2), (low quality:2) ' \
             'lowers, normal quality, ((monochrome)), ((grayscale)), logo, word, character'
pos_prompt_with_cloth = 'raw photo, masterpiece, chinese, simple background, wearing {}, high-class pure color background, solo, medium shot, high detail face, looking straight into the camera with shoulders parallel to the frame, slim body, photorealistic, best quality'
pos_prompt_with_style = '{} upper_body, raw photo, masterpiece, chinese, solo, medium shot, high detail face, slim body, photorealistic, best quality'


cloth_prompt = [
    {'name': 'working suit', 'prompt': 'high-class business/working suit'},  # male and female
    {'name': 'armor', 'prompt': 'silver armor'},  # male
    {'name': 'T-shirt', 'prompt': 'T-shirt'},  # male and female
    {'name': 'hanfu', 'prompt': 'beautiful traditional hanfu, upper_body'},  # female
    {'name': 'gown', 'prompt': 'an elegant evening gown'},  # female
]

styles = [
    {'name': '默认风格(default style)'},
    {'name': '凤冠霞帔(Chinese traditional gorgeous suit)',
     'model_id': 'ly261666/civitai_xiapei_lora',
     'revision': 'v1.0.0',
     'bin_file': 'xiapei.safetensors',
     'multiplier_style': 0.35,
     'add_prompt_style': 'red, hanfu, tiara, crown, '},
]


