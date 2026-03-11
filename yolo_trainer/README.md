# YOLO Trainer

A standalone PyQt5 application for training custom YOLO object detection models for the DB3K turret tracking system.

## Features

- **Dataset Management**: Validate and prepare YOLO-format datasets
- **Training Configuration**: Customize epochs, batch size, image size, and device
- **Real-time Monitoring**: Live progress updates and training logs
- **Model Export**: Save trained models for use in the main application
- **Integration**: Seamlessly connect with the turret app's YOLO detection system

## Requirements

### Python Dependencies
```
PyQt5>=5.15.0
ultralytics>=8.0.0
opencv-python>=4.8.0
numpy>=1.21.0
PyYAML>=6.0
```

### System Requirements
- **Windows**: Compatible with Windows 10/11
- **Memory**: Minimum 8GB RAM recommended
- **Storage**: 5GB+ free space for training data and models
- **GPU**: Optional NVIDIA GPU with CUDA for faster training

## Installation

1. Ensure the main turret application dependencies are installed
2. The trainer uses the same virtual environment as the main app
3. No additional installation required - the trainer is included

## Dataset Preparation

### YOLO Dataset Format
Your dataset must follow the standard YOLO format:

```
dataset/
├── images/
│   ├── train/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   └── val/
│       ├── image1.jpg
│       ├── image2.jpg
│       └── ...
├── labels/
│   ├── train/
│   │   ├── image1.txt
│   │   ├── image2.txt
│   │   └── ...
│   └── val/
│       ├── image1.txt
│       ├── image2.txt
│       └── ...
└── data.yaml
```

### data.yaml Format
```yaml
train: images/train
val: images/val
nc: 2  # number of classes
names: ['class1', 'class2']  # class names
```

### Label Format
Each label file corresponds to an image and contains:
```
<class_id> <x_center> <y_center> <width> <height>
```

Where coordinates are normalized (0-1) relative to image dimensions.

## Usage

### Launching from Main App
1. Open the main turret application
2. Switch to a YOLO detection mode (2, 4, 5, or 9)
3. Click the "Open YOLO Trainer" button in the YOLO settings panel
4. The trainer window will open as a separate application

### Standalone Usage
```bash
cd yolo_trainer
python yolo_trainer_window.py
```

## Training Workflow

1. **Select Dataset**: Browse to your prepared dataset folder
2. **Validate Dataset**: Click "Validate Dataset" to check structure
3. **Configure Training**:
   - Choose base model (yolov8n.pt recommended for starters)
   - Set epochs (50-200 typical)
   - Adjust batch size based on your GPU memory
   - Set image size (640 recommended)
4. **Set Output**: Choose where to save training results
5. **Start Training**: Click "Start Training" and monitor progress
6. **Export Model**: Once training completes, export the model for use

## Training Tips

### For Beginners
- Start with yolov8n.pt (fastest, smallest)
- Use 50-100 epochs initially
- Batch size 16 works on most systems
- Image size 640 is a good balance

### For Performance
- Use yolov8x.pt for maximum accuracy (requires more resources)
- Increase epochs to 200+ for complex datasets
- Larger batch sizes can speed up training (if GPU allows)
- Use CUDA if available for 10-50x speedup

### Memory Management
- Reduce batch size if you get CUDA out of memory errors
- Use CPU training if GPU memory is insufficient
- Close other applications during training

## Troubleshooting

### Common Issues

**"Ultralytics not available"**
- Install ultralytics: `pip install ultralytics`

**"Dataset validation failed"**
- Ensure data.yaml exists and is properly formatted
- Check that images/ and labels/ folders exist
- Verify label files have correct YOLO format

**"CUDA out of memory"**
- Reduce batch size
- Use smaller image size (416 or 512)
- Switch to CPU training
- Close other GPU-intensive applications

**"Training stuck"**
- Check system resources (CPU/GPU usage)
- Reduce workers if using multiple CPU cores
- Restart the application

### Windows-Specific Issues

**Torch DLL errors**
- The trainer automatically sets environment variables for stability
- If issues persist, run the main app first to initialize Torch

**Antivirus interference**
- Add exclusions for the training output directory
- Temporarily disable real-time scanning during training

## Model Integration

After training, your model will be saved as `best.pt` in the training output directory.

To use in the main turret app:
1. Export the model using the "Export Model" button
2. Copy the .pt file to the `YOLO_MODELS/` folder in the main app directory
3. Select the model in the YOLO settings panel
4. The model will be loaded automatically

## Advanced Configuration

### Custom Training Parameters
The trainer exposes most YOLO training parameters. For advanced users, you can modify the training config in the code.

### Multi-GPU Training
Set device to "cuda" and the trainer will use all available GPUs.

### Resume Training
If training is interrupted, you can resume by setting `resume: true` in advanced config (not exposed in UI yet).

## Support

For issues specific to the YOLO trainer:
1. Check the training log for error messages
2. Validate your dataset structure
3. Ensure sufficient system resources
4. Try with a smaller dataset first

For general YOLO questions, refer to the Ultralytics documentation: https://docs.ultralytics.com/

## Version History

- **1.0.0**: Initial release with basic training functionality
- Future: Dataset creation tools, advanced validation, model comparison