from models import MultimodalSentimentModel
def count_parameters(model):
    params_dict = {
        'text_encoder': 0,
        'video_encoder': 0,
        'audio_encoder': 0,
        'fusion_layer': 0,
        'emotion_classifier': 0,
        'sentiment_classifier': 0}
    
    total_params = 0
    for name, param in model.named_parameters():
        if param.requires_grad:
            param_count = param.numel()
            total_params += param.numel()
            
            if 'text_encoder' in name:
                params_dict['text_encoder'] += param.numel()
            elif 'video_encoder' in name:
                params_dict['video_encoder'] += param.numel()
            elif 'audio_encoder' in name:
                params_dict['audio_encoder'] += param.numel()
            elif 'fusion_layer' in name:
                params_dict['fusion_layer'] += param.numel()
            elif 'emotion_classifier' in name:
                params_dict['emotion_classifier'] += param.numel()
            elif 'sentiment_classifier' in name:
                params_dict['sentiment_classifier'] += param.numel()
        
    return params_dict, total_params

if __name__ == "__main__":
    model = MultimodalSentimentModel()
    params_dict, total_params = count_parameters(model)
    
    print("Parameter count by component")
    for component, count in params_dict.items():
        print(f"{component:20s}: {count:,} parameters")
            
    print("\nTotal trainable parameters: {:,}".format(total_params))
    