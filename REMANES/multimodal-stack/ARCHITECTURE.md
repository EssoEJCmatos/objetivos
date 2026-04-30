# 🏗️ ARCHITECTURE — Multimodal Video Analysis Stack

> **Stack:** YOLOv8 · OpenCV · Whisper · CrewAI · LLM Multimodal  
> **Domínio:** Visão Computacional · Orquestração Multi-Agente · Análise de Cenas

---

## 🧠 Visão Geral

Sistema de análise de vídeo inteligente baseado em múltiplos agentes especializados, orquestrados pelo CrewAI. O pipeline processa vídeo frame a frame combinando detecção de objetos, rastreamento, análise semântica e correlação de áudio.

---

## 🤖 Agentes

| # | Agente | Ferramenta Principal | Responsabilidade |
|---|--------|---------------------|-----------------|
| 1 | **Vision Agent** | YOLOv8 | Detectar objetos e gerar bounding boxes |
| 2 | **Tracking Agent** | DeepSORT / ByteTrack | Manter IDs persistentes entre frames |
| 3 | **Audio Agent** | Whisper | Transcrever fala e identificar eventos sonoros |
| 4 | **Context Agent** | LLM Multimodal | Interpretar a cena e gerar descrições semânticas |
| 5 | **Optimization Agent** | Ensemble + Heurísticas | Ajustar thresholds e reduzir falsos positivos |
| 6 | **Visualization Agent** | OpenCV + Matplotlib | Renderizar overlays, dashboards e heatmaps |

---

## 🔄 Pipeline Frame a Frame

```
┌─────────────────────────────────────────────────────────────┐
│                        INPUT                                │
│         Vídeo · Câmera ao vivo · Stream WebRTC              │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   PRÉ-PROCESSAMENTO                         │
│   Redimensionamento · Remoção de ruído · Nitidez            │
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
│  Fusão de detecções, tracking e eventos de áudio            │
│  Geração de descrições semânticas por frame                 │
│  Detecção de anomalias e padrões comportamentais            │
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

## 📊 Schema JSON de Saída

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

## 🎤 Ações Disponíveis (Comandos de Voz e Interface)

| Ação | Comando | Efeito no Pipeline |
|------|---------|-------------------|
| Focar em veículos | `"Focar em veículos"` | Filtra classes `car`, `truck`, `bus`, `motorcycle` |
| Detectar comportamento suspeito | `"Detectar comportamento suspeito"` | Ativa módulo de anomalia comportamental |
| Monitorar pessoas | `"Monitorar apenas pessoas"` | Filtra para classe `person` + atributos |
| Aumentar sensibilidade | `"Aumentar sensibilidade"` | Reduz threshold para 0.65 |
| Detectar objetos pequenos | `"Detectar objetos pequenos"` | Ativa modo de alta resolução |
| Destacar trajetórias | `"Destacar trajetórias"` | Habilita overlay de histórico de movimento |
| Gerar relatório | `"Gerar relatório agora"` | Dispara geração imediata do relatório |
| Pausar análise | `"Pausar análise"` | Suspende pipeline temporariamente |
| Retomar análise | `"Retomar análise"` | Retoma pipeline do ponto pausado |

---

## 📁 Estrutura de Projeto

```
multimodal-stack/
├── ARCHITECTURE.md          ← este arquivo
├── player.html              ← interface web do player
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
├── crew_main.py
├── config.yaml
└── requirements.txt
```

---

## ⚙️ Dependências

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

## 🚀 Melhorias Avançadas

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

*Arquitetura definida em Abril/2026 · Stack de produção · Todos os cenários cobertos*
