# 🎯 PROMPT MASTER — YOLOv8 + CrewAI + Análise de Vídeo Frame a Frame

> **Nível:** Produção · **Stack:** YOLOv8 · OpenCV · Whisper · CrewAI · LLM Multimodal  
> **Domínio:** Visão Computacional · Orquestração Multi-Agente · Análise de Cenas

---

## 🔥 PROMPT PRINCIPAL (Entrada no Sistema de Agentes)

```
SISTEMA: Analisador de Vídeo Inteligente Multi-Agente

OBJETIVO:
Analisar vídeos ou filmes frame a frame com máxima precisão, detectando,
classificando e rastreando:
  - Objetos: carros, pessoas, animais, itens genéricos
  - Acessórios: óculos, mochilas, armas, dispositivos eletrônicos
  - Características da cena: clima, iluminação, contexto urbano/natural
  - Ações: movimento, interação, comportamento humano
  - Áudio correlacionado: fala, ruído ambiente, eventos sonoros

PROCESSAMENTO (passo a passo):
  1. Extrair frames do vídeo em alta taxa (>= 30 fps)
  2. Aplicar detecção com YOLOv8 (bounding boxes + confidence score)
  3. Rastrear objetos entre frames (ID persistente via DeepSORT/ByteTrack)
  4. Classificar contexto da cena com modelo multimodal (LLM + visão)
  5. Sincronizar com análise de áudio (ASR via Whisper + eventos sonoros)
  6. Gerar enriquecimento semântico (descrição detalhada por frame)
  7. Detectar anomalias e padrões relevantes automaticamente

SAÍDA ESPERADA:
  - Overlay visual: bounding boxes + labels + IDs de rastreamento
  - Timeline estruturada em JSON (ver esquema abaixo)
  - Heatmap de movimentação por zona da cena
  - Relatório técnico detalhado por segmento de vídeo
  - Insights contextuais: intenção, risco, evento, dinâmica da cena

RESTRIÇÕES DE PRECISÃO:
  - Threshold mínimo de confiança: 0.80
  - Correção automática de falsos positivos via ensemble
  - Refinamento com múltiplos modelos quando confidence < 0.85

INTEGRAÇÕES ATIVAS:
  - YOLOv8       → detecção de objetos
  - OpenCV       → extração e pré-processamento de frames
  - Whisper      → transcrição e eventos de áudio
  - CrewAI       → orquestração multi-agente
  - DeepSORT     → rastreamento com IDs persistentes
  - LLM Vision   → análise semântica e contextual

FLUXO:
  Entrada (vídeo/stream/voz)
    → Pré-processamento (resize, denoise, sharpen)
    → Detecção YOLOv8
    → Tracking (ID único por objeto)
    → Análise semântica (LLM)
    → Correlação de áudio (Whisper)
    → Enriquecimento semântico
    → Renderização de saída (overlay + JSON + relatório)

INTERAÇÃO POR VOZ (exemplos de comandos aceitos):
  "Focar em veículos"
  "Detectar comportamento suspeito"
  "Monitorar apenas pessoas"
  "Aumentar sensibilidade"
  "Detectar objetos pequenos"
  "Destacar trajetórias"
  "Gerar relatório do segmento atual"

MODO AVANÇADO:
  - Previsão de movimento: Kalman Filter para tracking preditivo
  - Melhoria de imagem: remoção de blur + super-resolução (Real-ESRGAN)
  - Super-resolução em frames críticos (objetos < 32px)
  - Fusão multi-câmera quando disponível
```

---

## 🧠 ARQUITETURA CREWAI — MULTI-AGENTES

### Estrutura de Agentes

| # | Agente | Ferramenta Principal | Responsabilidade |
|---|--------|---------------------|-----------------|
| 1 | **Vision Agent** | YOLOv8 | Detectar objetos e gerar bounding boxes |
| 2 | **Tracking Agent** | DeepSORT / ByteTrack | Manter IDs persistentes entre frames |
| 3 | **Audio Agent** | Whisper | Transcrever fala e identificar eventos sonoros |
| 4 | **Context Agent** | LLM Multimodal | Interpretar a cena e gerar descrições semânticas |
| 5 | **Optimization Agent** | Ensemble + Heurísticas | Ajustar thresholds e reduzir falsos positivos |
| 6 | **Visualization Agent** | OpenCV + Matplotlib | Renderizar overlays, dashboards e heatmaps |

### Código de Integração CrewAI

```python
from crewai import Agent, Task, Crew

# ─── Agentes ─────────────────────────────────────────────────────────────────

vision_agent = Agent(
    role="Computer Vision Specialist",
    goal="Detect and classify all objects in each video frame with confidence >= 0.80",
    backstory="Expert in YOLOv8, trained on COCO and custom datasets.",
    tools=["YOLOv8Detector", "OpenCVProcessor"],
    verbose=True,
)

tracking_agent = Agent(
    role="Object Tracking Specialist",
    goal="Maintain persistent object IDs across frames and predict trajectories",
    backstory="Specialist in DeepSORT and ByteTrack for real-time multi-object tracking.",
    tools=["DeepSORTTracker", "KalmanPredictor"],
    verbose=True,
)

audio_agent = Agent(
    role="Audio Analyst",
    goal="Transcribe speech and detect sound events synchronized with video frames",
    backstory="Expert in Whisper ASR and audio event classification.",
    tools=["WhisperASR", "AudioEventClassifier"],
    verbose=True,
)

context_agent = Agent(
    role="Scene Context Analyst",
    goal="Generate rich semantic descriptions and detect anomalies in each scene",
    backstory="Multimodal LLM specialist with expertise in scene understanding.",
    tools=["MultimodalLLM", "AnomalyDetector"],
    verbose=True,
)

optimization_agent = Agent(
    role="Pipeline Optimization Specialist",
    goal="Reduce false positives and tune detection thresholds dynamically",
    backstory="ML engineer specialized in ensemble methods and threshold calibration.",
    tools=["EnsembleRefiner", "ConfidenceCalibrator"],
    verbose=True,
)

visualization_agent = Agent(
    role="Visualization Engineer",
    goal="Render bounding box overlays, heatmaps, and structured dashboards",
    backstory="Expert in OpenCV rendering and data visualization pipelines.",
    tools=["OverlayRenderer", "HeatmapGenerator", "ReportBuilder"],
    verbose=True,
)

# ─── Tarefas ──────────────────────────────────────────────────────────────────

detection_task = Task(
    description=(
        "Extract frames from the input video at >= 30fps. "
        "Apply YOLOv8 detection on each frame. "
        "Return bounding boxes, class labels, and confidence scores."
    ),
    agent=vision_agent,
    expected_output="List of detections per frame with bbox, label, and confidence.",
)

tracking_task = Task(
    description=(
        "Receive detections from the Vision Agent. "
        "Assign and maintain persistent IDs for each tracked object. "
        "Generate trajectory data and movement velocity estimates."
    ),
    agent=tracking_agent,
    expected_output="Tracked objects with IDs, positions, and velocity vectors.",
)

audio_task = Task(
    description=(
        "Extract audio from the input video. "
        "Transcribe speech using Whisper. "
        "Classify sound events (horn, explosion, crowd noise, etc.) "
        "and synchronize them with video timestamps."
    ),
    agent=audio_agent,
    expected_output="Timestamped transcription and sound event log.",
)

context_task = Task(
    description=(
        "Combine frame detections, tracking data, and audio events. "
        "Generate semantic scene descriptions per frame. "
        "Flag anomalies and relevant behavioral patterns."
    ),
    agent=context_agent,
    expected_output="Per-frame semantic descriptions and anomaly flags.",
)

optimization_task = Task(
    description=(
        "Review all detections and apply ensemble refinement. "
        "Remove false positives below confidence threshold. "
        "Dynamically adjust thresholds based on scene complexity."
    ),
    agent=optimization_agent,
    expected_output="Refined detection list with improved precision.",
)

visualization_task = Task(
    description=(
        "Render bounding box overlays with labels and IDs on each frame. "
        "Generate movement heatmaps. "
        "Compile structured JSON timeline and technical report."
    ),
    agent=visualization_agent,
    expected_output="Annotated video frames, heatmap image, JSON timeline, and PDF report.",
)

# ─── Crew ─────────────────────────────────────────────────────────────────────

crew = Crew(
    agents=[
        vision_agent,
        tracking_agent,
        audio_agent,
        context_agent,
        optimization_agent,
        visualization_agent,
    ],
    tasks=[
        detection_task,
        tracking_task,
        audio_task,
        context_task,
        optimization_task,
        visualization_task,
    ],
    verbose=2,
)

result = crew.kickoff(inputs={"video_path": "input/video.mp4"})
print(result)
```

---

## 🎥 PIPELINE FRAME A FRAME (NÍVEL PRODUÇÃO)

```
┌─────────────────────────────────────────────────────────────┐
│                        INPUT                                │
│         Vídeo · Câmera ao vivo · Stream WebRTC              │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   PRÉ-PROCESSAMENTO                         │
│   Redimensionamento · Remoção de ruído · Aumento de nitidez │
│              Super-resolução (Real-ESRGAN)                  │
└────────────────────────┬────────────────────────────────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
┌─────────────────────┐   ┌─────────────────────┐
│    DETECÇÃO         │   │   ANÁLISE DE ÁUDIO  │
│   YOLOv8            │   │   Whisper ASR       │
│   Bounding boxes    │   │   Eventos sonoros   │
│   Confidence score  │   │   Timestamps        │
└──────────┬──────────┘   └──────────┬──────────┘
           │                         │
           ▼                         │
┌─────────────────────┐              │
│    TRACKING          │             │
│   DeepSORT/ByteTrack │             │
│   ID único/objeto    │             │
│   Kalman prediction  │             │
└──────────┬──────────┘              │
           │                         │
           └────────────┬────────────┘
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                 ANÁLISE SEMÂNTICA (LLM)                     │
│  "carro em alta velocidade na faixa esquerda"               │
│  "pessoa carregando objeto suspeito, direção: norte"        │
│  "aglomeração detectada, risco: médio"                      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│               OTIMIZAÇÃO (ENSEMBLE)                         │
│   Remoção de falsos positivos · Calibração de thresholds    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                     SAÍDA                                   │
│  Overlay visual · JSON timeline · Heatmap · Relatório PDF   │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 SCHEMA JSON DE SAÍDA

```json
{
  "frame": 1023,
  "timestamp_ms": 34100,
  "objects": [
    {
      "id": 12,
      "type": "car",
      "confidence": 0.92,
      "bbox": { "x": 320, "y": 210, "w": 180, "h": 90 },
      "velocity": "high",
      "direction": "left-to-right",
      "trajectory": [[290, 215], [305, 213], [320, 210]]
    },
    {
      "id": 7,
      "type": "person",
      "confidence": 0.88,
      "bbox": { "x": 540, "y": 120, "w": 60, "h": 140 },
      "velocity": "slow",
      "direction": "stationary",
      "accessories": ["backpack"]
    }
  ],
  "scene": {
    "context": "urban traffic",
    "lighting": "daylight",
    "weather": "clear",
    "risk_level": "low",
    "description": "Two vehicles and one pedestrian on a busy urban intersection."
  },
  "audio": {
    "transcription": "",
    "events": ["car_horn"],
    "timestamp_ms": 34050
  },
  "anomalies": [],
  "heatmap_zone": "center-left"
}
```

---

## 🎤 COMANDOS DE VOZ (REFERÊNCIA COMPLETA)

| Comando | Ação no Pipeline |
|---------|-----------------|
| `"Focar em veículos"` | Filtra detecções para classes `car`, `truck`, `bus`, `motorcycle` |
| `"Detectar comportamento suspeito"` | Ativa módulo de anomalia comportamental |
| `"Monitorar apenas pessoas"` | Filtra para classe `person` + atributos |
| `"Aumentar sensibilidade"` | Reduz threshold para 0.65 |
| `"Detectar objetos pequenos"` | Ativa modo de detecção em alta resolução |
| `"Destacar trajetórias"` | Habilita overlay de histórico de movimento |
| `"Gerar relatório agora"` | Dispara geração imediata do relatório |
| `"Pausar análise"` | Suspende pipeline temporariamente |
| `"Retomar análise"` | Retoma pipeline do ponto pausado |
| `"Zoom em objeto [ID]"` | Super-resolução no objeto rastreado pelo ID |

---

## 🚀 MELHORIAS AVANÇADAS

| Recurso | Tecnologia | Finalidade |
|---------|-----------|-----------|
| Super-Resolução | Real-ESRGAN | Aumentar nitidez em frames críticos |
| Tracking Preditivo | Kalman Filter | Prever posição futura de objetos |
| Fusão Multi-câmera | Homografia + Calibração | Cobrir ângulos cegos |
| Edge AI | NVIDIA Jetson / Google TPU | Inferência local em tempo real |
| Streaming em Tempo Real | Kafka + WebRTC | Ingestão e entrega de baixa latência |
| Dashboard Interativo | React + Three.js | Visualização 3D de trajetórias |
| Relatórios Automáticos | LangChain + PDF | Geração narrativa de relatórios |

---

## 🎯 CASOS DE USO COBERTOS

### 🚗 Tráfego Urbano
- Contagem e classificação de veículos
- Detecção de infrações (velocidade, faixa)
- Monitoramento de congestionamento

### 🍫 Controle Industrial / Produção
- Contagem de itens na linha de produção
- Detecção de defeitos visuais
- Rastreamento de lotes

### ⚽ Análise Tática Esportiva
- Rastreamento de posicionamento de jogadores
- Análise de formação e movimentação
- Estatísticas de cobertura de campo

---

## 📁 ESTRUTURA DE PROJETO SUGERIDA

```
video_analysis/
├── agents/
│   ├── vision_agent.py
│   ├── tracking_agent.py
│   ├── audio_agent.py
│   ├── context_agent.py
│   ├── optimization_agent.py
│   └── visualization_agent.py
├── tools/
│   ├── yolo_detector.py
│   ├── deepsort_tracker.py
│   ├── whisper_asr.py
│   ├── overlay_renderer.py
│   └── heatmap_generator.py
├── pipeline/
│   ├── frame_extractor.py
│   ├── preprocessor.py
│   └── output_builder.py
├── crew_main.py          ← ponto de entrada principal
├── config.yaml           ← thresholds, modelos, paths
└── requirements.txt
```

---

## ⚙️ DEPENDÊNCIAS (requirements.txt)

```
crewai>=0.28.0
ultralytics>=8.0.0        # YOLOv8
opencv-python>=4.9.0
openai-whisper>=20231117
deep-sort-realtime>=1.3
filterpy>=1.4.5           # Kalman Filter
Pillow>=10.0.0
numpy>=1.26.0
torch>=2.1.0
langchain>=0.1.0
```

---

*Prompt criado em Abril/2026 · Stack de produção · Todos os cenários cobertos*
