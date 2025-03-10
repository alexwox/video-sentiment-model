**Sentiment analysis**

Project based on tutorial by Andreas Trolle.
"Train and Deploy a Multimodal AI Model: PyTorch, AWS, SageMaker, Next.js 15, React, Tailwind (2025)"

https://www.youtube.com/watch?v=Myo5kizoSk0&t=370s

_Model:_

Late fusion multimodal model using:

- Video Encoder: Resnet3D 18 layer
- Text Encoder: BERT
- Audio Encoder: Raw Spectogram

Two output heads:

- Emotion classifier, 7 emotions.
- Sentiment classifier, negative, neural, positive.
