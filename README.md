# il-pusht-k8s

## Goal

## Results

## Architecture

## Learning-scale vs industry-scale

## Setup

Tested on Apple Silicon (M3 Pro, macOS). Needs Python 3.12 and ffmpeg.

```bash
git clone git@github.com:rehmanazeem/il-pusht-k8s.git && cd il-pusht-k8s
conda create -n il-pusht -c conda-forge python=3.12 ffmpeg
conda activate il-pusht
make setup        # pip install -r requirements.lock -e .
```

Check:

```bash
python -c "import torch; print(torch.backends.mps.is_available())"   # True on Apple Silicon
lerobot-eval --help
```

### Reference checkpoint

`lerobot/diffusion_pusht` uses the old checkpoint format, which LeRobot 0.6.1 cannot load.
Migrate it once with the workaround script:

```bash
python scripts/migrate_pusht_ckpt.py --pretrained-path lerobot/diffusion_pusht \
  --output-dir outputs/models/diffusion_pusht
```

### Known warnings

Harmless: a duplicate `libavdevice` warning (`opencv-python` and `av` both bundle it) and a
torchcodec `libavutil` warning (falls back to pyav).
